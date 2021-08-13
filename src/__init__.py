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
import datetime

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
fecha = datetime.date.today()


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
        materias = Modelo_materia.materia_docente(db, 1284373821)
        data = []
        for i in range(1, 8):
            objeto = 'materia_semestre'+str(i)
            objeto = Modelo_materia.obtener_materias_por_semestre(db, i)
            data.append(objeto)
        return render_template('index.html', title='home', alumnos=alumnos, data=data, materias=materias)
    else:
        return redirect(url_for('login'))


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
def docentes():
    return render_template('docentes.html')


@app.route('/agregar_docentes', methods=['POST'])
def agregar_docentes():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellido_p = request.form['apellido_p']
        apellido_m = request.form['apellido_m']
        cur = db.connection.cursor()
        cur.execute("INSERT INTO docente (nombres, apellido_p, apellido_m) VALUES (%s, %s, %s)",
                    (nombres, apellido_p, apellido_m))
        db.connection.commit()
        flash('Registro exitoso')
        return redirect(url_for('docentes'))
    else:
        return render_template('docentes.html')
    # return render_template('docentes.html')


#@app.route('/edit_docentes/<id>', methods=['POST', 'GET'])
#def edit_docentes(id):
 #   cur = db.connection.cursor()
  #  cur.execute('SELECT * FROM registro WHERE id = %s', (id))
   # data = cur.fetchall()
   # cur.close()
    #print(data[0])
    #return render_template('docentes.html', contact=data[0])


#@app.route('/update_docentes/<id>', methods=['POST'])
#def update_docentes(id):
 #   if request.method == 'POST':
  #      profesión = request.form['Profesión']
   #     nombre = request.form['Nombre']
    #    telefono = request.form['Telefono']
     #   email = request.form['Email']
      #  materias = request.form['Materias_impartidas']
 #       horas = request.form['Horas']
 #       cur = db.connection.cursor()
 #       cur.execute("""
  #         UPDATE registro
   #        SET Profesión = %s,
    #            Nombre = %s,
     #           Telefono = %s,
      #          Email = %s,
       #         Materias_impartidas = %s,
        #        Horas = %s
         #  WHERE id = %s
    #""", (profesión, nombre, telefono, email, materias, horas, id))
    #flash('Registro actualizado correctamente')
    #db.connection.commit()
    #return redirect(url_for('docentes.html'))


#@app.route('/delete_docentes/<string:id>', methods=['POST', 'GET'])
#def delete_docentes(id):
 #   cur = db.connection.cursor()
  #  cur.execute('DELETE FROM registro WHERE id = {0}'.format(id))
   # db.connection.commit()
    #flash('Registro eliminado correctamente')
    #return redirect(url_for('docentes.html'))


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


# return render_template('docentes.html')


# def start_app(config):
#     app.config.from_object(config)
#     csrf.init_app(app)
#     return app


@app.route('/grupos')
def grupos():
    grupos = Modelo_grupo.obtener_grupos(db)
    return render_template('grupos.html', data=grupos)


@app.route('/materias')
def materias():
    materias = Modelo_materia.obtener_nombre_materia(db, 1)
    return render_template('materias.html', data=materias)


@app.route('/materia')
def materia():
    alumnos = Modelo_alumno.obtener_alumnos(db)
    return render_template('evaluar.html', data=alumnos)


@app.route('/evaluar', methods=['POST', 'GET'])
@login_required
def evaluar():
    if request.method == 'POST':
        parcial = request.form.getlist('parcial')
        id_materia = request.form.getlist('materia')
        id_alumno = request.form.getlist('id_alumno')
        calificacion = request.form.getlist('calificacion')
        for i in range(1, len(parcial)+1):
            Modelo_evaluacion.evaluar(
                db, parcial[i], fecha, id_materia[i], id_alumno[i], calificacion[i])
        return redirect(url_for('evaluar'))
    else:
        return render_template('alumnos.html')


def start_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    return app
