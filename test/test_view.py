# from db.models import app
from app import app


def test_get_all_users():
    response = app.test_client().get('/users')
    assert response.status_code == 200
    assert type(response.json) == list


