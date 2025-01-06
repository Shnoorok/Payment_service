import pytest

@pytest.mark.asyncio
async def test_create_payment(async_client):
    response = await async_client.post("/payments/", json={"amount": 100.0, "currency": "USD"})
    assert response.status_code == 200
    data = response.json()
    assert "payment_id" in data
    assert data['status'] == "Pending"

@pytest.mark.asyncio
async def test_get_payment_status(async_client):
    # Создаем платеж
    create_response = await async_client.post("/payments/", json={"amount": 100.0, "currency": "USD"})
    assert create_response.status_code == 200
    payment_id = create_response.json()['payment_id']

    # Проверяем статус
    response = await async_client.get(f"/payments/{payment_id}")
    assert response.status_code == 200
    data = response.json()
    assert data['payment_id'] == payment_id
    assert data['status'] == "Pending"

@pytest.mark.asyncio
async def test_get_nonexistent_payment_status(async_client):
    response = await async_client.get("/payments/nonexistent-id")
    assert response.status_code == 404

