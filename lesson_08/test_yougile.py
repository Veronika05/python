import pytest
import requests

base_url = "https://ru.yougile.com"
token = "wvitR+NlnD1YaUdIw91XT3wTAtReBMsCd5Wqz8lQF8UTZX7EVNuSrU82QvC6Djf1"


def test_create_project_positive():
    body = {"title": "SkyPro"}
    my_header = {'Authorization': f"Bearer {token}", 'Content-Type': 'application/json'}
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers=my_header )
    resp_body = resp.json()
    assert resp_body["id"] is not None
    assert resp.status_code == 201

def test_create_untitled_project_negative():
    body = {"title": ""}
    my_header = {'Authorization': f"Bearer {token}", 'Content-Type': 'application/json'}
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers=my_header )
    resp_body = resp.json()
    assert resp.status_code == 400

def test_put_project_positive():
    #создать проект
    body = {"title": "SkyPro"}
    my_header = {'Authorization': f"Bearer {token}", 'Content-Type': 'application/json'}
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers=my_header )
    resp_body = resp.json()
    project_id = resp_body["id"]
    assert resp.status_code == 201

    body = {"title": "Python"}
    resp = requests.put(f'{base_url}/api-v2/projects/{project_id}', json=body, headers=my_header)
    assert resp.status_code == 200
    
    #Получить проект по ID
    resp = requests.get(f'{base_url}/api-v2/projects/{project_id}', headers=my_header)
    resp_body = resp.json()
    assert resp_body["title"] == "Python"

def test_put_project_negative():
    body = {"title": "SkyPro"}
    my_header = {'Authorization': f"Bearer {token}", 'Content-Type': 'application/json'}
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers=my_header )
    resp_body = resp.json()
    project_id = resp_body["id"]
    assert resp.status_code == 201

    body = {"title": ""}
    resp = requests.put(f'{base_url}/api-v2/projects/{project_id}', json=body, headers=my_header)
    assert resp.status_code == 400

    resp = requests.get(f'{base_url}/api-v2/projects/{project_id}', headers=my_header)
    resp_body = resp.json()
    assert resp_body["title"] == "SkyPro"

def test_get_project_positive():
    body = {"title": "SkyPro"}
    my_header = {'Authorization': f"Bearer {token}", 'Content-Type': 'application/json'}
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers=my_header )
    resp_body = resp.json()
    project_id = resp_body["id"]
    assert resp.status_code == 201

    resp = requests.get(f'{base_url}/api-v2/projects/{project_id}', headers=my_header)
    resp_body = resp.json()
    assert resp_body["title"] == "SkyPro"
    assert resp.status_code == 200

def test_get_project_negative():
    #запрос без header
    body = {"title": "SkyPro"}
    my_header = {'Authorization': f"Bearer {token}", 'Content-Type': 'application/json'}
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers=my_header )
    resp_body = resp.json()
    project_id = resp_body["id"]
    assert resp.status_code == 201

    resp = requests.get(f'{base_url}/api-v2/projects/{project_id}')
    assert resp.status_code == 401




















    

    