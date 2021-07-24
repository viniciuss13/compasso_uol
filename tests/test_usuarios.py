from typing import Any, Dict
import pytest
import pytest
from utils import cadastrar_usuario, filtrar_usuarios


@pytest.mark.parametrize("admin", [True, False])
def test_cadastro_usuario(base_url: str, falso_nome: str, falso_email: str, falsa_senha: str, admin: bool):
    response = cadastrar_usuario(f"{base_url}/usuarios", falso_nome,
                                 falso_email, falsa_senha, admin)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data.get("message") == "Cadastro realizado com sucesso"
    assert response_data.get("_id") is not None


def test_listar_usuarios_cadastrados(base_url: str, dados_reais: Dict[str, Any]):
    response = filtrar_usuarios(f"{base_url}/usuarios",
                                id=dados_reais.get("_id"))

    dados_reais["administrador"] = str(dados_reais["administrador"]).lower()
    response_data = response.json()

    assert response.status_code == 200
    assert response_data.get("quantidade") == 1
    assert response_data.get("usuarios").pop() == dados_reais
