"""
На любом асинхронном движке сделать HTTP-сервис,
который будет принимать число, возвращать его факториал и писать access.log.
Предложить способ демонизации процесса сервера.
"""

import math
from fastapi import FastAPI, status, HTTPException
from fastapi.testclient import TestClient


app = FastAPI()


@app.get("/{n}")
async def get_factorial(n: int):
    if n < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="send a positive numbers only, please"
        )
    return math.factorial(n)



client = TestClient(app)


def test_get_factorial_0():
    response = client.get("/0")
    assert response.status_code == 200
    assert response.text == '1'


def test_get_factorial_10():
    response = client.get("/10")
    assert response.status_code == 200
    assert response.text == '3628800'


def test_get_factorial_neg_int():
    response = client.get("/-1")
    assert response.status_code == 400
    assert response.text == '{"detail":"send a positive numbers only, please"}'
