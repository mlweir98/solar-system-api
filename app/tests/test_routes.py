def test_all_planet_returns_empty_list(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_by_id_returns_planet1(client, create_two_planets):
    response = client.get("/planets/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "jupiter",
        "description": "smokey",
        "color": "red"
    }

def test_create_planet_returns_201(client): 
    response = client.post("/planets", json = {
        "name":"neptune",
        "color":"gray",
        "description":"this one is cool"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {"message": "neptune was successfully created"}

def test_put_planet_returns_200(client, create_two_planets):
    response = client.put("/planets/1",json = {
        "name":"pluto",
        "color":"gray",
        "description":"smol"
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "pluto successfully updated"

def test_delete_planet_returns_200(client, create_two_planets):
    response = client.delete("/planets/2")
    response_body = response.get_json()

    assert response.status_code == 200 
    assert response_body == "jupiter was deleted successfully"