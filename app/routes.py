from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

#creating a post
@planets_bp.route("", methods = ["POST"])
def create_new_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        color = request_body["color"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response({"message": f"{new_planet.name} was successfully created"}, 201)


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

