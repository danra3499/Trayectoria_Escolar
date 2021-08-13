return render_template('docentes.html')


def start_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    return app
