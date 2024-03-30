import socket
import json
from cryptography.fernet import Fernet
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "client_server_prog.settings")
import django

django.setup()
from client_server_prog.settings import FERNET_KEY, SOCKET_HOST, SOCKET_PORT


def send_data(data) -> str:
    """
    Функція для відправки даних до сервера та отримання відповіді.

    Parameters:
        data (dict): Словник з даними, які потрібно відправити на сервер.

    Returns:
        str: Результат відправлення даних до сервера.
    """

    json_data = json.dumps(data).encode()

    cipher_suite = Fernet(FERNET_KEY)
    encrypted_data = cipher_suite.encrypt(json_data)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SOCKET_HOST, SOCKET_PORT))
    client_socket.sendall(encrypted_data)
    response = client_socket.recv(1024).decode()
    client_socket.close()

    return response
