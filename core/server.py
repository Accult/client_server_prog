import socket
import pickle
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "client_server_prog.settings")
import django

django.setup()
from core.models import User


def handle_data(data):
    decrypted_data = pickle.loads(data)

    first_name, last_name, age = decrypted_data.split(",")

    user = User(first_name=first_name, last_name=last_name, age=age)
    user.save()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("Server is listening...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    encrypted_data = client_socket.recv(1024)
    if not encrypted_data:
        break

    handle_data(encrypted_data)

    print("Data added to the database successfully!")

    client_socket.close()
