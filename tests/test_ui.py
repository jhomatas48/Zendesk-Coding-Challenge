import os
import tempfile


from flask import Flask
import json

from main import app
from tests.credentials import credentials
import base64

app.config['TESTING'] = True
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

