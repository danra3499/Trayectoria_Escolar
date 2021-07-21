from flask import Flask, render_template, redirect, request, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloAlumno import Modelo_alumno
from .models.ModeloEvaluacion import Modelo_evaluacion
from .models.ModeloMateria import Modelo_materia
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        password = request.form['password']

        usuario = Usuario(None, user, None, None, password, None)
        logged = ModeloUsuario.login(db, usuario)

        if logged != None:
            login_user(logged)
            flash(BIENVENIDA, 'success')
            return redirect(url_for('index'))

        else:
            flash(LOGIN_NO_VALIDO, 'warning')
            return render_template('/auth/login.html', title='Login')

    else:
        return render_template('/auth/login.html', title='Login')


@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@login_required
@app.route('/')
def index():
    return render_template('index.html', title='home')


# @app.route('/password/<password>')
# def generate_password(password):
#     return generate_password_hash(password)

# CRUD DE ALUMNOS Y MAESTROS

@app.route('/agregar_alumno', methods=['POST', 'GET'])
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


@app.route('/agregar_materia', methods=['POST', 'GET'])
def agregar_materia():
    if request.method == 'POST':
        nombre = request.form['nombre']
        creditos = request.form['creditos']
        semestre = request.form['semestre']
        Modelo_materia.agregar(db, nombre, creditos, semestre)
        return redirect(url_for('agregar_materia'))
    else:
        return render_template('materias.html')


@app.route('/evaluar', methods=['POST', 'GET'])
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
