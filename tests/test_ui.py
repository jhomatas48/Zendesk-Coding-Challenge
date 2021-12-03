import os
import tempfile


from flask import Flask
import json

from main import app
from tests.credentials import credentials
import base64

client = app.test_client()

creds = credentials()
email = creds['email']
password = creds['password']
subdomain = creds['subdomain']
name = creds['name']
domain = subdomain + ".zendesk.com"
print('hi')
combined = email + ':' + password
encoded_u = base64.b64encode(combined.encode()).decode()
auth = "Basic " + encoded_u

def test_start():
    url = '/'
    response = client.get(url)
    assert response.get_data() is not None
    assert response.status_code == 302

def test_login():
    url = '/login'
    response = client.get(url)
    assert response.status_code == 200
    response_post = client.post(url)
    assert response_post.status_code == 200



'''
def test_post_route__success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/post/test'

    mock_request_headers = {
        'authorization-sha256': '123'
    }

    mock_request_data = {
        'request_id': '123',
        'payload': {
            'py': 'pi',
            'java': 'script'
        }
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200


def test_post_route__failure__unauthorized():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/post/test'

    mock_request_headers = {}

    mock_request_data = {
        'request_id': '123',
        'payload': {
            'py': 'pi',
            'java': 'script'
        }
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 401


def test_post_route__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/post/test'

    mock_request_headers = {
        'authorization-sha256': '123'
    }

    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 400
'''