from flask import Flask
from routes import task_routes
from database import Base, engine

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

app.register_blueprint(task_routes, url_prefix="/v1")

if __name__ == "__main__":
    app.run(debug=True)
