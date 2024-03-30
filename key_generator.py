from cryptography.fernet import Fernet


class KeyGenerator:
    """
    A class for generating and loading encryption keys.

    Attributes:
        key_file (str): The path to the key file.
    """

    def __init__(self, key_file):
        self.key_file = key_file

    def generate_key(self):
        """
        Generate a new encryption key and save it to the key file.
        """
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)

    def load_key(self) -> bytes:
        """
        Load the encryption key from the key file.

        Returns:
            bytes: The encryption key.
        """
        with open(self.key_file, "rb") as key_file:
            return key_file.read()


if __name__ == "__main__":
    key_generator = KeyGenerator(input("Enter key file: "))
    key_generator.generate_key()
