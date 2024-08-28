def test_start_adventure(client):
    response = client.post("api/v1/start")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "description" in json_data
    assert "options" in json_data
    assert len(json_data["options"]) == 3
