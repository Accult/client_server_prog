import socket
import pickle


def main():
    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = input("Enter your age: ")
        data = f"{first_name},{last_name},{age}"

        encrypted_data = pickle.dumps(data)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 12345))

        client_socket.sendall(encrypted_data)

        client_socket.close()

        print("Data submitted successfully!")


if __name__ == "__main__":
    main()
