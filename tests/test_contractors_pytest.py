from datetime import datetime, timezone


def test_get_contractors_seeded(client):
    resp = client.get("/contractors/")
    assert resp.status_code == 200
    data = resp.json()
    # Seed inserts 10 contractor rows
    assert isinstance(data, list)
    assert len(data) == 10


def test_create_contractor_sqlite(client):
    created_at = datetime.now(timezone.utc).isoformat()
    resp = client.post(
        "/contractors/",
        params={
            "name": "NewCo",
            "created_at": created_at,
            "email": "newco@example.com",
            "phone_no": "1230009999",
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "NewCo"
    assert body["email"] == "newco@example.com"
    assert body["phone_no"] == "1230009999"

    # Ensure count increased
    get_resp = client.get("/contractors/")
    assert get_resp.status_code == 200
    assert len(get_resp.json()) == 11


def test_update_contractor_sqlite(client):
    # Update existing seeded contractor id=1 (autoincrement starts at 1 in SQLite)
    new_created_at = datetime.now(timezone.utc).isoformat()
    put_resp = client.put(
        "/contractors/1",
        params={
            "name": "Updated Name",
            "created_at": new_created_at,
            "email": "updated@example.com",
            "phone_no": "9998887777",
        },
    )
    assert put_resp.status_code == 200
    updated = put_resp.json()
    assert updated["id"] == 1
    assert updated["name"] == "Updated Name"
    assert updated["email"] == "updated@example.com"
    assert updated["phone_no"] == "9998887777"


