**Project README**

This repository contains a client-server program developed in Python using the Django framework for the server-side application. The client-server communication is established via sockets, and the data sent from the client to the server is encrypted.

### Installation Steps

1. **Clone the Project**
   ```
   git clone https://github.com/Accult/client_server_prog.git
   ```

2. **Navigate to the Project Directory**
   ```
   cd client_server_prog
   ```

3. **Create a Virtual Environment**
   ```
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. **Install Required Packages**
   ```
   pip install -r requirements.txt
   ```

6. **Create and Configure .env File**
   - Create a `.env` file based on the `.env-example` template.
   - Fill in the required environment variables such as database credentials and encryption keys.

7. **Run Migrations**
   ```
   python manage.py migrate
   ```

8. **Create a Superuser**
   ```
   python manage.py createsuperuser
   ```

9. **Start the Django Development Server**
   ```
   python manage.py runserver
   ```

   Access the Django admin panel at `http://localhost:8000/admin` to ensure that user data input is stored in the database.


   **Encryption Key**

The project has a key.txt file that is used by default to encrypt and decrypt data
To create a new key, run the command

```
python key_generator.py
```
Next, enter the file name in the terminal in the format <name>.txt
To use the new key you have created, you need to add KEY_FILE= <name>.txt to the .env file


10. **Run the Server**
    In a new console window, run the server script:
   ```
   python core/server.py
   ```

11. **Run the Client Interface**
    In another console window, run following command:
   ```
   python core/gui.py

   ```

Follow the instructions in the client interface to input user data. This data will be encrypted and sent to the server for decryption and storage in the database.

### Additional Notes

- Ensure that both the server and client scripts are running simultaneously to establish communication.
