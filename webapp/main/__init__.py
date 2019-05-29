def create_module_main(app, **kwargs):
    from .controllers import main_blueprint
    app.register_blueprint(main_blueprint)