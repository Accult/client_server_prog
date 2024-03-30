import socket
import json
from cryptography.fernet import Fernet
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "client_server_prog.settings")
import django

django.setup()
from core.models import User
from client_server_prog.settings import FERNET_KEY, SOCKET_HOST, SOCKET_PORT
from core.serializers import UserSerializer


def handle_data(data, key, client_socket):
    """
    Decrypts the received data, validates it, and saves it to the database or sends error messages back to the client.

    Args:
        data (bytes): The encrypted data received from the client.
        key (bytes): The encryption key.
        client_socket (socket.socket): The socket object representing the client connection.

    Returns:
        None
    """
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data).decode()
    json_data = json.loads(decrypted_data)

    serializer = UserSerializer(data=json_data)
    if serializer.is_valid():
        User.objects.create(**json_data)
        client_socket.sendall("Data processed successfully!".encode())
    else:
        error_messages = [
            f"{field}: {error_msg}" for field, errors in serializer.errors.items() for error_msg in errors
        ]

        error_message = "\n".join(error_messages)
        client_socket.sendall(error_message.encode())


def main():
    """
    Sets up a server socket, listens for incoming connections, and handles the received data.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SOCKET_HOST, SOCKET_PORT))
    server_socket.listen(1)

    print("Server is listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")

        encrypted_data = client_socket.recv(1024)
        if not encrypted_data:
            break

        handle_data(encrypted_data, FERNET_KEY, client_socket)
        client_socket.close()


if __name__ == "__main__":
    main()
