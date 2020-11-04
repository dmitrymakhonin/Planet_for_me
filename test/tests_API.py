import pytest
import requests
# я бы думал что сравнивать нужно с информацие с БД, но пока что просто список соответствующий информации со страницы

url = ["https://reqres.in/api/users?page=2"]

@pytest.mark.parametrize("url", url)
def test_check_list(url):
    data = [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"},
            {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg"},
            {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg"},
            {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg"},
            {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"},
            {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg"}]
    result= requests.get(url)
    assert result.status_code==200
    v = result.json()["data"]
    assert sorted(v, key=lambda x: x["id"])== sorted(data, key=lambda x: x["id"])

def test_add_user():
    data = [{"id": 33, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
             "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"}]
    url = "https://reqres.in/api/users"
    result = requests.post(url,json=data)
    assert result.status_code==201
    assert result.json()==data

