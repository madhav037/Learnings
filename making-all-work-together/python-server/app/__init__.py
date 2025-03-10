from flask import Flask
# from flask_pymongo import PyMongo
# from app.routes.user_routes import user_bp

# mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app
    # MongoDB connection
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/my_database_name"  # Replace 'my_database_name' with your database name
    # mongo.init_app(app)
    
    # Register blueprints
    # app.register_blueprint(user_bp, url_prefix='/api/user')
    
    return app
