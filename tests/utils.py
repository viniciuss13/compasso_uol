from typing import Optional
import requests


def cadastrar_usuario(url: str, nome: str, email: str, senha: str, admin: bool) -> requests.Response:
    data = {"nome": nome,
            "email": email,
            "password": senha,
            "administrador": str(admin).lower()}
    
    return requests.post(url, data)


def filtrar_usuarios(url: str, id: Optional[str] = None, nome: Optional[str] = None,
                     email: Optional[str] = None, senha: Optional[str] = None, admin: Optional[bool] = None) -> requests.Response:
    data = {}
    if id:
        data.update({"_id": id})
    if nome:
        data.update({"nome": nome})
    if email:
        data.update({"email": email})
    if senha:
        data.update({"password": senha})
    if admin:
        data.update({"administrador": str(admin).lower()})

    return requests.get(url, data)
