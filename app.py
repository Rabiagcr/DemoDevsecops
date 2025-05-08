from flask import Flask
def createapp_():
    app=Flask(__name__)
    from.run import main
    app.register_blueprint(main)
    return app
