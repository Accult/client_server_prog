**Project README**

This repository contains a client-server program developed in Python using the Django framework for the server-side application. The client-server communication is established via sockets, and the data sent from the client to the server is encrypted.

### Installation Steps

1. **Clone the Project**
   ```
   git clone https://github.com/Accult/client_server_prog.git
   ```

2. **Create a Virtual Environment**
   ```
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Required Packages**
   ```
   pip install -r requirements.txt
   ```

5. **Create and Configure .env File**
   - Create a `.env` file based on the `.env-example` template.
   - Fill in the required environment variables such as database credentials and encryption keys.

6. **Run Migrations**
   ```
   python manage.py migrate
   ```

7. **Create a Superuser**
   ```
   python manage.py createsuperuser
   ```

8. **Start the Django Development Server**
   ```
   python manage.py runserver
   ```

   Access the Django admin panel at `http://localhost:8000/admin` to ensure that user data input is stored in the database.

9. **Run the Server**
   In a new console window, run the server script:
   ```
   python core/server.py
   ```

10. **Run the Client**
    In another console window, run the client script:
   ```
   python core/client.py
   ```

    Follow the instructions in the client console to input user data. This data will be encrypted and sent to the server for decryption and storage in the database.

### Additional Notes

- Ensure that both the server and client scripts are running simultaneously to establish communication.