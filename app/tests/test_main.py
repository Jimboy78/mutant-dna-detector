import pytest
from app.main import app


@pytest.fixture
def client():
    # Configura tu aplicación para las pruebas
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_mutant_route(client):
    dna = {"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]}
    response = client.post('/mutant/', json=dna)
    assert response.status_code == 200


def test_human_route(client):
    dna = {"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CTCCTA", "TCACTG"]}
    response = client.post('/mutant/', json=dna)
    assert response.status_code == 403


def test_mutant_route_large(client):
    dna = {"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG", "GGGGTG"]}
    response = client.post('/mutant/', json=dna)
    assert response.status_code == 200


def test_human_route_small(client):
    dna = {"dna": ["ATGC", "CAGT", "TTAT", "AGAA"]}
    response = client.post('/mutant/', json=dna)
    assert response.status_code == 403
