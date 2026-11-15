#verification
from healthapp import app

def test_home_page():
    app.config["TESTING"] = True

    client = app.test_client()

    response = client.get("/")

    assert response.status_code ==200

    assert response.data.decode() == "Welcome to DevOps CI/CD Project!"


def test_health_endpoint():
    app.config["TESTING"] = True

    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["message"] == "Application is running successfully"
