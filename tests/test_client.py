import json


def test_index_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_webhook(test_client):
    data = {'text': 'Foo bar'}
    response = test_client.post('/hitch-slack', data=json.dumps(data))
    assert response.status_code == 200
