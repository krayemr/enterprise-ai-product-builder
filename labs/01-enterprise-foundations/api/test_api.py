from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_security_request_requires_review():
    response = client.post(
        "/requests",
        json={
            "request_type": "security",
            "description": "Production credentials may have been exposed.",
        },
    )

    assert response.status_code == 200
    assert response.json()["workflow"] == "security_review_required"


def test_invalid_request_type_is_rejected():
    response = client.post(
        "/requests",
        json={
            "request_type": "banana",
            "description": "This is an otherwise valid description.",
        },
    )

    assert response.status_code == 422

def test_compliance_request_requires_review():
    response = client.post(
        "/requests",
        json={
            "request_type": "compliance",
            "description": "This request requires regulatory compliance review.",
        },
    )

    assert response.status_code == 200
    assert response.json()["workflow"] == "compliance_review_required"