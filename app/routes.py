from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app.models.moon import Moon
from app import db


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix = "/moons")

#creating a post
@planets_bp.route("", methods = ["POST"])
def create_new_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response({"message": f"{new_planet.name} was successfully created"}, 201)

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    color_query = request.args.get("color")

    if color_query and name_query:
        planets = Planet.query.filter_by(color = color_query, name = name_query)
    elif color_query:
        planets = Planet.query.filter_by(color = color_query)
    elif name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()

    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_dict())
        
    return jsonify(planets_response), 200

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{model_id} invalid is not valid {type(model_id)}"}, 404))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@planets_bp.route("/<planet_id>",methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict(), 200

@planets_bp.route("/<planet_id>",methods = ["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.color = request_body["description"]
    planet.powers = request_body["color"]

    db.session.commit()

    return make_response(jsonify(f"{planet.name} successfully updated"))

@planets_bp.route("/<planet_id>",methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"{planet.name} was deleted successfully")), 200

@moons_bp.route("", methods = ["POST"])
def create_moon():

    request_body = request.get_json()
    new_moon = Moon(
        name = request_body["name"]
    )
    

    db.session.add(new_moon)
    db.session.commit()

    return jsonify(f"Moon {new_moon.name} was succesfully created"), 201

@moons_bp.route("", methods = ["GET"])
def get_all_moons():
    moons = Moon.query.all()
    moon_response = []

    for moon in moons:
        moon_response.append({
            "id": moon.id,
            "name": moon.name
        })
    
    return jsonify(moon_response), 200

#nested routes
@planets_bp.route("/<planet_id>/moons", methods = ["POST"])
def create_moon_for_specific_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    new_moon = Moon(
        name = request_body["name"],
        planet = planet 
    )

    db.session.add(new_moon)
    db.session.commit()

    return jsonify(f"Planet {new_moon.planet.name} has {new_moon.name} was successfully created"), 201

"""
planets= [
        Planet(1, "Pluto", "Small", "redish-white"), 
        Planet(2, "Saturn", "Rings", "yellow"), 
        Planet(3, "Uranus", "Beautiful", "grumdrop blue")
        ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def list_all_planets():
    planets_list = []
    for planet in planets:
        planets_list.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })
    return jsonify(planets_list)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def list_specific_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
    "id": planet.id,
    "name": planet.name,
    "description": planet.description,
    "color": planet.color
}

    

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    
    except:
        abort(make_response({"message":f"{planet_id} is not a valid planet"}, 400))
    
    for planet in planets:
        if planet_id == planet.id:
            return planet

    abort(make_response({"message":f"{planet_id} was not found"}, 404))
"""

