import json

import requests
from jsonschema import validate

from schemas.user_schema import user_get, user_post, user_patch, user_positive

url = "https://reqres.in/api/users"


def test_method_post_create_user():
    name = "Ivan"
    job = "tester"

    response = requests.post(url, json={"name": name, "job": job})
    body = response.json()
    assert response.status_code == 201
    assert body["name"] == name
    assert body["job"] == job
    validate(instance=body, schema=user_post)


def test_method_get_users():
    response = requests.get(f"{url}/?page=2")
    body = response.json()
    assert response.status_code == 200
    assert "data" in body
    validate(instance=body, schema=user_get)


def test_method_put_update_user():
    payload = {"name": "morpheus", "job": "tester"}
    response = requests.put(f"{url}/2", data=json.dumps(payload), headers={"Content-Type": "application/json"})
    body = response.json()
    assert response.status_code == 200
    assert body["job"] == "tester"


def test_method_delete_user():
    response = requests.delete(f"{url}/users/2")
    assert response.status_code == 204
    assert response.text == ""


def test_method_get_user_positive():
    user_id = 2
    response = requests.get(f"{url}/{user_id}")
    body = response.json()["data"]
    assert response.status_code == 200
    assert body["id"] == user_id
    validate(instance=body, schema=user_positive)


def test_method_get_user_negative():
    response = requests.get(f"{url}/23")
    assert response.status_code == 404


def test_method_patch_update_user():
    user_id = 2
    name = "Ivan"
    job = "tester"

    response = requests.patch(f"{url}/{user_id}", json={"name": name, "job": job})
    body = response.json()
    assert response.status_code == 200
    assert body["name"] == name
    assert body["job"] == job
    validate(instance=body, schema=user_patch)
