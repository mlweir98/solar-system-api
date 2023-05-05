import pytest
from app.models.planet import Planet
from app import create_app
from app import db
from flask.signals import request_finished


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def create_two_planets(app):

    # Act
    planet_1 = Planet(name="pluto",description="smol",color="blue")
    planet_2 = Planet(name="jupiter", description="smokey", color="red")

    db.session.add_all([planet_1,planet_2])

    db.session.commit()