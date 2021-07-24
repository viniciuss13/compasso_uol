from typing import Any, Dict
import pytest
from faker import Faker
from faker.providers import internet, misc
from utils import cadastrar_usuario


fake: Faker = Faker()
fake.add_provider(internet)
fake.add_provider(misc)


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://serverest.dev"


@pytest.fixture()
def falso_email() -> str:
    return fake.ascii_company_email()


@pytest.fixture()
def falsa_senha() -> str:
    return fake.password()


@pytest.fixture()
def falso_nome() -> str:
    return fake.name()


@pytest.fixture()
def dados_reais_admin(base_url, falso_nome, falso_email, falsa_senha) -> Dict[str, Any]:
    """Fornece dados de um usuário administrador cadastrado no sistema
    """

    data = {"nome": falso_nome,
            "email": falso_email,
            "password": falsa_senha,
            "administrador": True}
    response = cadastrar_usuario(f"{base_url}/usuarios", *data.values())
    assert response.status_code == 201

    data.update({"_id": response.json().get("_id")})

    return data


@pytest.fixture()
def dados_reais(base_url, falso_nome, falso_email, falsa_senha) -> Dict[str, Any]:
    """Fornece dados de um usuário cadastrado no sistema
    """

    data = {"nome": falso_nome,
            "email": falso_email,
            "password": falsa_senha,
            "administrador": False}
    response = cadastrar_usuario(f"{base_url}/usuarios", *data.values())
    assert response.status_code == 201

    data.update({"_id": response.json().get("_id")})

    return data
