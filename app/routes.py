from flask import Blueprint, jsonify

# Perform following setup steps for the Solar System API repo to get started on this Flask project:

# 1. Create a virtual environment and activate it
# 1. Install the dependencies
# 1. Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
# 1. Create a list of `Planet` instances

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


