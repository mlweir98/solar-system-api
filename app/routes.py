from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

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
    planet_id = int(planet_id)
    for planet in planets:
        if planet_id == planet.id:
            return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        }


# 1. ...to get one existing `planet`, so that I can see the `id`, `name`, 
# `description`, and other data of the `planet`.
# 1. ... such that trying to get one non-existing `planet` 
# responds with get a `404` response, so that I know the `planet` resource was not found.
# 1. ... such that trying to get one `planet` with an invalid 
#     `planet_id` responds with get a `400` response, so that I know the `planet_id` was invalid.