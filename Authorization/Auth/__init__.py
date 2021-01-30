from flask import Flask
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

client = app.test_client()

engine = create_engine("postgresql://postgres:postgres@localhost:5432/OpenEdu")

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


from .Core.views import core


app.register_blueprint(core)
