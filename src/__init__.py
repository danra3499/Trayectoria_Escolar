from src.models.entities.Alumno import Alumno
from werkzeug.datastructures import RequestCacheControl
from src.models.entities.Grupo import Grupo
from src.models.entities.Materia import Materia
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash


from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloAlumno import Modelo_alumno
from .models.ModeloDocentes import Modelo_docente
from .models.ModeloEvaluacion import Modelo_evaluacion
from .models.ModeloMateria import Modelo_materia
from .models.ModeloGrupo import Modelo_grupo
from .models.entities.Usuario import Usuario
from .models.ModeloIndices import Modelo_agregar_alumno
from .models.ModeloIndices import Modelo_actualizar_indices
from .models.ModeloIndices import Modelo_indice
from .models.ModeloIndices import Modelo_indiceIAC
from .models.ModeloIndices import Modelo_indiceIPE
from .models.ModeloIndices import Modelo_indiceIDE
from .models.ModeloIndices import Modelo_indiceISE
from .models.ModeloIndices import Modelo_indiceIRE
from .models.ModeloIndices import Modelo_indice_alumno
from .models.ModeloPeriodos import Modelo_periodo
from .consts import *
from datetime import date

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
fecha = date.today()


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.get_id(db, id)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        password = request.form['password']
        usuario = Usuario(None, user, None, None, None, password, None)
        logged = ModeloUsuario.login(db, usuario)
        if logged != None:
            login_user(logged)
            flash(BIENVENIDA, 'success')
            return redirect(url_for('home'))
        else:
            flash(LOGIN_NO_VALIDO, 'warning')
            return render_template('/auth/login.html', title='Login')
    else:
        return render_template('/auth/login.html', title='Login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    if current_user.is_authenticated:
        alumnos = Modelo_alumno.obtener_alumnos(db)
        # alumnos = Modelo_alumno.obtener_alumnos_grupo(db, grupo)
        materias = Modelo_materia.materia_docente(db, current_user.usuario)
        data = []
        for i in range(1, 25):
            objeto = 'materia_semestre'+str(i)
            objeto = Modelo_materia.obtener_materias_por_semestre(db, i)
            data.append(objeto)
        return render_template('index.html', title='home', alumnos=alumnos, data=data, materias=materias)
    else:
        return redirect(url_for('login'))

"""-----------------------------------------USUARIOS------------------------------------------------------"""
@app.route('/usuarios')
@login_required
def usuario():
    data = ModeloUsuario.consultar_usuarios(db)
    return render_template('usuarios.html', data=data)


@app.route('/agregar_usuario', methods=['POST'])
@login_required
def agregar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        password = generate_password_hash(request.form['password'])
        tipo_usuario = request.form.get('tipo_usuario')
        ModeloUsuario.agregar_usuario(
            db, usuario, nombres, apellido_p, apellido_m, password, tipo_usuario)
        return redirect(url_for('usuario'))
    else:
        return render_template('usuario.html')


@app.route('/editar_usuario/<usuario>', methods=['POST', 'GET'])
@login_required
def editar_usuario(usuario):
    cursor = db.connection.cursor()
    query = """SELECT * FROM usuario WHERE usuario = '{0}'""".format(usuario)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_usuario.html', usuarios=data[0])


@app.route('/actualizar_usuario/<usuario>', methods=['POST'])
@login_required
def actualizar_usuario(usuario):
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        password = generate_password_hash(request.form['password'])
        tipo_usuario = request.form.get('tipo_usuario')
        ModeloUsuario.editar_usuario(
            db, usuario, nombres, apellido_p, apellido_m, tipo_usuario)
        return redirect(url_for('usuario'))
    else:
        return render_template('usuario.html')


@app.route('/eliminar_usuario/<usuario>', methods=['POST', 'GET'])
@login_required
def eliminar(usuario):
    ModeloUsuario.eliminar_usuario(db, usuario)
    flash('Registro eliminado correctamente')
    return redirect(url_for('usuario'))

"""----------------------------------------------ALUMNO----------------------------------------------"""
@app.route('/alumnos')
@login_required
def alumno():
    data = Modelo_alumno.obtener_alumnos(db)
    return render_template('alumnos.html', data=data)



@app.route('/agregar_alumno', methods=['POST', 'GET'])
@login_required
def agregar_alumno():
    alumnos = Modelo_alumno.obtener_alumnos(db)
    if request.method == 'POST':
        numero_control = request.form['numero_control']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        genero = request.form.get('genero')
        status = request.form.get('status')
        grupo = request.form['grupo']

        Modelo_alumno.add(db, numero_control, nombres, apellido_p,
                          apellido_m, genero, status, grupo)

        Modelo_agregar_alumno.add_Alum_Ind(db, numero_control)

        return redirect(url_for('agregar_alumno'))
    else:
        return render_template('alumnos.html', data=alumnos)
        

@app.route('/editar_alumno/<id>', methods=['POST', 'GET'])
@login_required
def editar_alumno(id):
    cursor = db.connection.cursor()
    query = """SELECT * FROM alumno WHERE id = '{0}'""".format(id)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_alumno.html', alumno=data[0])


@app.route('/actualizar_alumno/<id>', methods=['POST'])
@login_required
def actualizar_alumno(id):  
    if request.method == 'POST':
        numero_control = request.form['numero_control']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        genero = request.form.get('genero')
        status = request.form.get('status')
        grupo = request.form['grupo']
        Modelo_alumno.editar_alumno(db, numero_control, nombres, apellido_p, apellido_m, genero, status, grupo)
        return redirect(url_for('alumno'))
    else:
        return render_template('alumnos.html')

@app.route('/eliminar_alumno/<id>', methods=['POST', 'GET'])
@login_required
def eliminar_alumno(id):
    Modelo_alumno.eliminar_alumno(db, id)
    flash('Registro eliminado correctamente')
    return redirect(url_for('alumno'))

"""-----------------------------------------------DOCENTE-----------------------------------------------"""

@app.route('/docente')
@login_required
def docentes():
    docente = Modelo_docente.obtener_docentes(db)
    return render_template('docentes.html', data=docente)


@app.route('/agregar_docentes', methods=['POST', 'GET'])
@login_required
def agregar_docentes():
    if request.method == 'POST':
        n_control = request.form['n_control']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        Modelo_docente.agregar_docente(
            db, n_control, nombres, apellido_p, apellido_m)
        return redirect(url_for('docentes'))
    else:
        return render_template('docentes.html', data=docentes)
    # return render_template('docentes.html')


@app.route('/editar_docente/<id>', methods=['POST', 'GET'])
@login_required
def editar_docente(id):
    cursor = db.connection.cursor()
    query = """SELECT * FROM docente WHERE id = '{0}'""".format(id)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_docente.html', docente=data[0])


@app.route('/actualizar_docente/<id>', methods=['POST'])
@login_required
def actualizar_docente(id):
    if request.method == 'POST':
        n_control = request.form['n_control']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        tipo_usuario = request.form.get('tipo_usuario')
        Modelo_docente.editar_docente(
            db, n_control, nombres, apellido_p, apellido_m)
        return redirect(url_for('docentes'))
    else:
        return render_template('docentes.html')


@app.route('/eliminar_docente/<id>', methods=['POST', 'GET'])
@login_required
def eliminar_docente(id):
    Modelo_docente.eliminar_docente(db, id)
    flash('Registro eliminado correctamente')
    return redirect(url_for('docentes'))

"""--------------------------------------MATERIAS------------------------------------------------------"""    

@app.route('/materias')
@login_required
def materias():
    materia = Modelo_materia.obtener_materias(db)
    return render_template('materia_ventana.html', data=materia)

@app.route('/agregar_materia', methods=['POST', 'GET'])
@login_required
def agregar_materia():
    if request.method == 'POST':
        id = request.form['id']
        clave = request.form['clave']
        nombre = request.form['nombre']
        creditos = request.form['n_creditos']
        grupo = request.form['id_grupo']
        docente = request.form['id_docente']
        Modelo_materia.agregar_materia(db, id, clave, nombre, creditos, grupo, docente)
        return redirect(url_for('materias'))
    else:
        return render_template('materia_ventana.html')

@app.route('/editar_materia/<id>', methods=['POST', 'GET'])
@login_required
def editar_materia(id):
    cursor = db.connection.cursor()
    query = """SELECT * FROM materia WHERE id = '{0}'""".format(id)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_materias.html', materia=data[0])


@app.route('/actualizar_materia/<id>', methods=['POST'])
@login_required
def actualizar_materia(id):
    if request.method == 'POST':
        id = request.form['id']
        clave = request.form['clave']
        nombre = request.form['nombre']
        creditos = request.form['n_creditos']
        grupo = request.form['id_grupo']
        docente = request.form.get('id_docente')
        Modelo_materia.editar_materia(
            db, id, clave, nombre, creditos, grupo, docente)
        return redirect(url_for('materias'))
    else:
        return render_template('materia_ventana.html')


@app.route('/eliminar_materia/<id>', methods=['POST', 'GET'])
@login_required
def eliminar_materia(id):
    Modelo_materia.eliminar_materia(db, id)
    flash('Registro eliminado correctamente')
    return redirect(url_for('materias'))


"""#--------------------------------------GRUPOS------------------------------------------------------------"""

@app.route('/grupos')
@login_required
def grupos():
    grupos = Modelo_grupo.obtener_grupos(db)
    return render_template('grupos.html', data=grupos)

@app.route('/grupos_indices')
@login_required
def grupos_indices():
    grupos_indices = Modelo_grupo.obtener_grupos(db)
    return render_template('grupos_indices.html', data=grupos_indices)

# @app.route('/materias')
# @login_required
# def materias():
#     materias = Modelo_materia.obtener_nombre_materia(db, 1)
#     return render_template('materias.html', data=materias)


@app.route('/materia/<grupo>')
@login_required
def materia(grupo):
    # materias = Modelo_materia.obtener_nombre_materia(db, 1)
    materias = Modelo_materia.materia_grupo(db, grupo)
    return render_template('materias.html', data=materias)

@app.route('/materia2/<grupo>')
@login_required
def materia2(grupo):
    # materias = Modelo_materia.obtener_nombre_materia(db, 1)
    materias = Modelo_materia.materia_por_grupo(db, grupo)
    return render_template('materias2.html', data=materias)

# @app.route('/materia')
# @login_required
# def materia():
#     alumnos = Modelo_alumno.obtener_alumnos(db)
#     return render_template('evaluar.html', data=alumnos)

@app.route('/lista/<grupo>')
@login_required
def lista(grupo):
    listas = Modelo_alumno.obtener_alumnos_grupo(db,grupo)
    return render_template('lista_grupos.html', data=listas)

@app.route('/lista2/<id>')
@login_required
def lista2(id):
    alumn = Modelo_evaluacion.obtener_promedio_alumnos(db,id)
    cmal = Modelo_evaluacion.calificacion_materia_alumnos(db,id)
    return render_template('lista_calificaciones.html', alumn=alumn, cmal=cmal)

"""---------------------------EVALUACIONES---------------------------"""


@app.route('/evaluar/<id>', methods=['POST', 'GET'])
@login_required
def evaluar(id):
    alumnos = Modelo_materia.alumnos_materia_id(db, id)
    materias = Modelo_materia.obtener_materias_id(db, id)
    evaluacion = Modelo_evaluacion.obtener_calificacion_grupos(db, id)
    alumn = Modelo_evaluacion.obtener_promedio_alumnos(db, id)
    

    return render_template('evaluar.html', data=alumnos, materias=materias, evaluacion = evaluacion,alumn=alumn, fecha=fecha)

@app.route('/evaluar/<id>/evaluar_alumno/<id_alumno>', methods=['POST', 'GET'])
@login_required
def evaluar_alumno(id,id_alumno):
    hoy = date.today()
    materias = Modelo_materia.obtener_materias_id(db, id)
    alumnos = Modelo_alumno.obtener_alumno_id(db,id_alumno)
    alumcal = Modelo_evaluacion.obtener_calificacion_por_alumnos(db, id, id_alumno)
    actipe = Modelo_actualizar_indices.actual_IPE(db, id_alumno)
    actiao = Modelo_actualizar_indices.actual_IAO(db, id_alumno)
    actiac = Modelo_actualizar_indices.actual_IAC(db, id_alumno)
    actide = Modelo_actualizar_indices.actual_IDE(db, id_alumno)
    actise = Modelo_actualizar_indices.actual_ISE(db, id_alumno)
    actire = Modelo_actualizar_indices.actual_IRE(db, id_alumno)

    return render_template('evaluar_alumno.html', data=alumnos,materias=materias,alumcal=alumcal,fecha=hoy,actipe=actipe, actiao=actiao, actiac=actiac, actide=actide, actise=actise, actire=actire)

@app.route('/capturar_evaluacion', methods=['POST', 'GET'])
@login_required
def capturar_evaluacion():
    if request.method == 'POST':
        parcial = request.form['parcial']
        fecha = request.form['fecha']
        calificacion = request.form['calificacion']
        tipo_evaluacion = request.form.get('tipo_evaluacion')
        id_materia = request.form['materia']
        id_alumno = request.form['id_alumno']
        Modelo_evaluacion.capturar_evaluaciones(
            db, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno)
        return redirect(url_for('evaluar_alumno', id=id_materia, id_alumno=id_alumno))
    else:
        return render_template('evaluar_alumno.html', data=evaluar_alumno)

@app.route('/editar_cal/<parcial>/<id_materia>/<id_alumno>', methods=['POST', 'GET'])
@login_required
def editar_cal(parcial, id_materia, id_alumno):
    cursor = db.connection.cursor()
    query = """SELECT * FROM evaluacion WHERE parcial = '{0}' and id_materia = '{1}' 
               and id_alumno = '{2}'""".format(parcial, id_materia, id_alumno)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_calificaciones.html', evaluacion=data[0])

@app.route('/actualizar_cal/<id>', methods=['POST'])
@login_required
def actualizar_cal(id):
    if request.method == 'POST':
        id = request.form['id_cal']
        alumno = request.form['id_alumno']
        parcial = request.form['parcial']
        calificacion = request.form['calificacion']
        tipo_evaluacion = request.form.get('tipo_evaluacion')
        id_materia = request.form['id_materia']
        Modelo_evaluacion.editar_cal(
            db, id, parcial, calificacion, tipo_evaluacion)
        return redirect(url_for('evaluar_alumno', id=id_materia, id_alumno=alumno))
    else:
        return render_template('evaluar_alumno.html', data=evaluar_alumno)

@app.route('/eliminar_cal/<parcial>/<id_materia>/<id_alumno>', methods=['POST', 'GET'])
@login_required
def eliminar_cal(parcial,id_materia,id_alumno):
    Modelo_evaluacion.eliminar_cal(db, parcial, id_materia, id_alumno)
    return redirect(url_for('evaluar_alumno', id=id_materia, id_alumno=id_alumno))

"""---------------------------FIN DE EVALUACIONES---------------------------"""


def pagina_no_encontrada(error):
    return render_template('error/404.html'), 7


def pagina_no_autorizada(error):
    return render_template(url_for('login'))


def start_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, pagina_no_autorizada)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

"""---------------------------Indices-------------------------------------------"""

@app.route('/indices')
@login_required
def indices():
    data = Modelo_indice.obtener_indice(db)
    IndicesIAC = Modelo_indiceIAC.obtener_indiceIAC(db)
    IndicesIPE = Modelo_indiceIPE.obtener_indiceIPE(db)
    IndicesIDE = Modelo_indiceIDE.obtener_indiceIDE(db)
    IndicesISE = Modelo_indiceISE.obtener_indiceISE(db)
    IndicesIRE = Modelo_indiceIRE.obtener_indiceIRE(db)
    return render_template('indices.html',  data=data, IndicesIAC=IndicesIAC, IndicesIPE=IndicesIPE, IndicesIDE = IndicesIDE, IndicesISE = IndicesISE, IndicesIRE = IndicesIRE)


@app.route('/alumnos_indices/<grupo>')
@login_required
def alumnos_indices(grupo):
    data = Modelo_indice_alumno.obtener_indice_alumnos(db, grupo)
    return render_template('lista_alum_indices.html', data=data )

"""------------------------------------------IAO------------------------------"""
@app.route('/editar_indice_IAO/<id_IAO>', methods=['POST','GET'])
@login_required
def editar_indice_IAO(id_IAO):
    cursor = db.connection.cursor()
    query = """SELECT * FROM iao WHERE id_IAO = '{0}'""".format(id_IAO)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_IAO.html', iao=data[0])


@app.route('/actualizar_IAO/<id_IAO>', methods=['POST'])
@login_required
def actualizar_IAO(id_IAO):
    if request.method == 'POST':
        id_IAO = request.form['id_IAO']
        nivel_IAO = request.form['nivel_IAO']
        categoria_IAO = request.form['categoria_IAO']
        Modelo_indice.editar_IAO(
        db, id_IAO, nivel_IAO, categoria_IAO)
        return redirect(url_for('indices'))
    else:
        return render_template('indices.html')

"""-------------------------------------IAC----------------------------------------"""
@app.route('/editar_indice_IAC/<id_IAC>', methods=['POST','GET'])
@login_required
def editar_indice_IAC(id_IAC):
    cursor = db.connection.cursor()
    query = """SELECT * FROM iac WHERE id_IAC = '{0}'""".format(id_IAC)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_IAC.html', iac=data[0])

@app.route('/actualizar_IAC/<id_IAC>', methods=['POST'])
@login_required
def actualizar_IAC(id_IAC):
    if request.method == 'POST':
        id_IAC = request.form['id_IAC']
        nivel_IAC = request.form['nivel_IAC']
        categoria_IAC = request.form['categoria_IAC']
        Modelo_indiceIAC.editar_IAC(
        db, id_IAC, nivel_IAC, categoria_IAC)
        return redirect(url_for('indices'))
    else:
        return render_template('indices.html')

"""------------------------------------IPE------------------------------------------"""
@app.route('/editar_indice_IPE/<id_IPE>', methods=['POST', 'GET'])
@login_required
def editar_indice_IPE(id_IPE):
    cursor = db.connection.cursor()
    query = """SELECT * FROM ipe WHERE id_IPE = '{0}'""".format(id_IPE)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_IPE.html', ipe=data[0])

@app.route('/actualizar_IPE/<id_IPE>', methods=['POST'])
@login_required
def actualizar_IPE(id_IPE):
    if request.method == 'POST':
        id_IPE = request.form['id_IPE']
        nivel_IPE = request.form['nivel_IPE']
        categoria_IPE = request.form['categoria_IPE']
        Modelo_indiceIPE.editar_IPE(
        db, id_IPE, nivel_IPE, categoria_IPE)
        return redirect(url_for('indices'))
    else:
        return render_template('indices.html')

"""----------------------------------ISE-----------------------------------------------"""

@app.route('/editar_indice_ISE/<id_ISE>', methods=['POST', 'GET'])
@login_required
def editar_indice_ISE(id_ISE):
    cursor = db.connection.cursor()
    query = "SELECT * FROM ise WHERE id_ISE = '{0}'".format(id_ISE)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('editar_ISE.html', ise=data[0])
    
@app.route('/actualizar_ISE/<id_ISE>' , methods=['POST'])
@login_required
def actualizar_ISE(id_ISE):
    if request.method == 'POST':
        id_ISE = request.form['id_ISE']
        nivel_ISE = request.form['nivel_ISE']
        categoria_ISE = request.form['categoria_ISE']
        Modelo_indiceISE.editar_ISE(
        db, id_ISE, nivel_ISE, categoria_ISE)
        return redirect(url_for('indices'))
    else:
        return render_template('indices.html')
        
"""----------------------------------Calificaciones-------------------------------"""

@app.route('/calificaciones')
@login_required
def calificaciones():
    grupos = Modelo_grupo.obtener_grupos(db)
    return render_template('calificaciones.html', data=grupos)


"""-----------------------------------Periodos-----------------------------------"""

@app.route('/periodos')
@login_required 
def periodos():
    periodo = Modelo_periodo.obtener_periodos(db)
    return render_template('periodos.html', data=periodo)

@app.route('/gruposper')
@login_required
def gruposper():
    grupos = Modelo_grupo.obtener_grupos(db)
    return render_template('gruposper.html', data=grupos)

