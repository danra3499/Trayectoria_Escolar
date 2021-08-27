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
        materias = Modelo_materia.materia_docente(db, current_user.usuario)
        data = []
        for i in range(1, 8):
            objeto = 'materia_semestre'+str(i)
            objeto = Modelo_materia.obtener_materias_por_semestre(db, i)
            data.append(objeto)
        return render_template('index.html', title='home', alumnos=alumnos, data=data, materias=materias)
    else:
        return redirect(url_for('login'))


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


@app.route('/edit/<usuario>', methods=['POST', 'GET'])
@login_required
def edit(usuario):
    cursor = db.connection.cursor()
    query = """SELECT * FROM usuario WHERE usuario = '{0}'""".format(usuario)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('edit_usuario.html', usuarios=data[0])


@app.route('/update/<usuario>', methods=['POST'])
@login_required
def update(usuario):
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        # password = generate_password_hash(request.form['password'])
        tipo_usuario = request.form.get('tipo_usuario')
        ModeloUsuario.editar_usuario(
            db, usuario, nombres, apellido_p, apellido_m, tipo_usuario)
        return redirect(url_for('usuario'))
    else:
        return render_template('usuario.html')


@app.route('/delete/<usuario>', methods=['POST', 'GET'])
@login_required
def delete(usuario):
    ModeloUsuario.eliminar_usuario(db, usuario)
    flash('Registro eliminado correctamente')
    return redirect(url_for('usuario'))


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
        semestre = request.form['semestre']
        grupo = request.form['grupo']

        Modelo_alumno.add(db, numero_control, nombres, apellido_p,
                          apellido_m, genero, status, semestre, grupo)
        return redirect(url_for('agregar_alumno'))
    else:
        return render_template('alumnos.html', data=alumnos)


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


@app.route('/agregar_materia', methods=['POST', 'GET'])
@login_required
def agregar_materia():
    if request.method == 'POST':
        nombre = request.form['nombre']
        creditos = request.form['creditos']
        semestre = request.form['semestre']
        Modelo_materia.agregar(db, nombre, creditos, semestre)
        return redirect(url_for('agregar_materia'))
    else:
        return render_template('materias.html')


@app.route('/grupos')
@login_required
def grupos():
    grupos = Modelo_grupo.obtener_grupos(db)
    return render_template('grupos.html', data=grupos)


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

# @app.route('/materia')
# @login_required
# def materia():
#     alumnos = Modelo_alumno.obtener_alumnos(db)
#     return render_template('evaluar.html', data=alumnos)


@app.route('/evaluar/<id>', methods=['POST', 'GET'])
@login_required
def evaluar(id):
    alumnos = Modelo_materia.alumnos_materia_id(db, id)
    return render_template('evaluar.html', data=alumnos, fecha=fecha)


@app.route('/evaluar_alumno/<id>', methods=['POST', 'GET'])
@login_required
def evaluar_alumno(id):
    hoy = date.today()
    cursor = db.connection.cursor()
    query = """SELECT * FROM alumno WHERE id = '{0}'""".format(id)
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('evaluar_alumno.html', data=data[0], fecha=hoy)

# @app.route('/editar_docente/<id>', methods=['POST', 'GET'])
# @login_required
# def editar_docente(id):
#     cursor = db.connection.cursor()
#     query = """SELECT * FROM docente WHERE id = '{0}'""".format(id)
#     cursor.execute(query)
#     data = cursor.fetchall()
#     return render_template('editar_docente.html', docente=data[0])


@app.route('/capturar_evaluacion', methods=['POST'])
@login_required
def capturar_evaluacion():
    fecha = date.today()
    if request.method == 'POST':
        parcial = request.form['parcial']
        fecha = fecha
        calificacion = request.form['calificacion']
        tipo_evaluacion = request.form['tipo_evaluacion']
        id_materia = request.form['id_materia']
        id_alumno = request.form['n_control']
        Modelo_evaluacion.evaluar(
            db, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno)
        return render_template('evaluar.html')
    else:
        return render_template('evaluar.html')


def pagina_no_encontrada(error):
    return render_template('error/404.html'), 404


def pagina_no_autorizada(error):
    return render_template(url_for('login'))


def start_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, pagina_no_autorizada)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
