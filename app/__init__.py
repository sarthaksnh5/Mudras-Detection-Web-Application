from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['UPLOAD_FOLDER_IMAGES'] = 'uploads/images'
    app.config['UPLOAD_FOLDER_VIDEOS'] = 'uploads/videos'

    from . import routes
    routes.init_app(app)

    return app
