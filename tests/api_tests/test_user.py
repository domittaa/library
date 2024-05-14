from fastapi.testclient import TestClient

from source_code.app import app

client = TestClient(app)


def test_create_user(db_session):
    data = {
        "first_name": "Test1",
        "last_name": "Test1",
        "email": "test1@test.pl",
        "phone": 111111111,
        "address": "Wroclaw",
        "date_joined": "2024-05-10",
    }
    response = client.post("/users/", json=data)
    assert response.status_code == 200
    assert response.json()["email"] == data["email"]

    # mock_db_session.add.assert_called()
    # mock_db_session.commit.assert_called()
