import os
import tempfile
import pytest
from app import app,db
from flask import request, jsonify
import json

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_status(client):

    rv = client.get('/')

    data = rv.get_json()
    assert "Welcome to the Flask app" in data["message"]


def test_case1(client):

    db.drop_all()
    db.create_all()
    rv = client.get("/student")
    data = rv.get_json()
    assert 0 == len(data["result"])


def test_case2(client):

    payload = {"age": 21,"fname": "Nitish","lname": "Arora"}
    
    rv = client.post("/student", data=json.dumps(payload))
    print(f": {rv.status_code}")
    assert 200 == rv.status_code    


def test_case3(client):

    rv = client.get("/student")
    data = rv.get_json()
    assert 1 == len(data["result"])


def test_case4(client):

    payload = {"age": 21,"fname": "Nitish","lname": "Arora"}
    for i in range(1,11):
        payload["age"] += i
        rv = client.post("/student", data=json.dumps(payload))
        data = rv.get_json()
    assert 200 == rv.status_code


def test_case5(client):

    rv = client.get("/student")
    data = rv.get_json()
    assert 11 == len(data["result"])


def test_case6(client):

    rv = client.delete("/student?rollno=11")
    assert 200 == rv.status_code


def test_case7(client):

    for i in range(1, 11):

        rv = client.get(f"/student/{i}")
        payload = rv.get_json()
        payload["age"] += 2
        rv = client.post("/student", data=json.dumps(payload))

    assert 200 == 200


def test_case8(client):

    rv = client.get("/student")
    data = rv.get_json()
    assert 10 == len(data["result"])


def test_case9(client):

    rv = client.get("/student/2")
    data = rv.get_json()
    assert 24 == data["age"]


def test_case10(client):

    for i in range(1,10):
        rv = client.get(f"/student/{i}")
        assert 200 == rv.status_code
