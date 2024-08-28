def test_select_option(client):
    response = client.post('api/v1/choose', json={"option_id": 1})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "description" in json_data
    assert "options" in json_data

def test_missing_option_id(client):
    response = client.post('/api/v1/choose', json={"option_id": "string"})
    assert response.status_code == 422
    json_data = response.get_json()
    assert json_data[0]["msg"] == "Input should be a valid integer, unable to parse string as an integer"

def test_invalid_option(client):
    response = client.post('api/v1/choose', json={"option_id": 999})
    assert response.status_code == 404
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data["error"] == "Invalid option"
