from src.models.entities.Materia import Materia
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloAlumno import Modelo_alumno
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

        usuario = Usuario(None, user, None, None, password, None)
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
    return render_template('index.html', title='home')
    alumnos = Modelo_alumno.obtener_alumnos(db)
    materias_semestre1 = Modelo_materia.obtener_materias_por_semestre(db, 1)
    materias_semestre2 = Modelo_materia.obtener_materias_por_semestre(db, 2)
    materias_semestre3 = Modelo_materia.obtener_materias_por_semestre(db, 3)
    materias_semestre4 = Modelo_materia.obtener_materias_por_semestre(db, 4)
    materias_semestre5 = Modelo_materia.obtener_materias_por_semestre(db, 5)
    materias_semestre6 = Modelo_materia.obtener_materias_por_semestre(db, 6)
    materias_semestre7 = Modelo_materia.obtener_materias_por_semestre(db, 7)
    materias_semestre8 = Modelo_materia.obtener_materias_por_semestre(db, 8)
    data = {
        'alumnos': alumnos,
        'materias1': materias_semestre1,
        'materias2': materias_semestre2,
        'materias3': materias_semestre3,
        'materias4': materias_semestre4,
        'materias5': materias_semestre5,
        'materias6': materias_semestre6,
        'materias7': materias_semestre7,
        'materias8': materias_semestre8,
    }
    return render_template('index.html', title='home', data=data)




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

@app.route('/agregar_docentes')
def agregar_docentes():
    if request.method == 'POST':
        Profesión = request.form['Profesión']
        Nombre = request.form['Nombre']
        Telefono = request.form['Telefono']
        Email = request.form['Email']
        Materias_impartidas = request.form.get('Materias_impartidas')
        Horas = request.form.get('Horas')
    return render_template('docentes.html')


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
