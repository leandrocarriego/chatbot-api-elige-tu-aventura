def test_server_is_running(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200