from typing import Any, Dict
import requests


def login_and_assert(url: str, data: Dict[str, Any]):
    """Realiza o login e testa os dados retornados

    Args:
        url (str): endereço de login
        data (Dict[str, Any]): dados da requisição de login
    """

    response = requests.post(url, data)
    response_data = response.json()

    assert response.status_code == 200
    assert response_data.get("message") == "Login realizado com sucesso"
    assert "Bearer " in response_data.get("authorization")


def test_login_admin(base_url: str, dados_reais_admin: Dict[str, Any]):
    data = {"email": dados_reais_admin.get("email"),
            "password": dados_reais_admin.get("password")}
    url = f"{base_url}/login"
    login_and_assert(url, data)


def test_login(base_url: str, dados_reais: Dict[str, Any]):
    data = {"email": dados_reais.get("email"),
            "password": dados_reais.get("password")}
    url = f"{base_url}/login"
    login_and_assert(url, data)
