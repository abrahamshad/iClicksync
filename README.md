# iClicksync

iClicksync is a Django-based web application that allows users to create, share, and retrieve code snippets and files. The application supports file upload, password protection, and expiration times for shared content.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/abrahamshad/iclicksync.git
    cd iclicksync
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## Usage

Once the development server is running, open your browser and navigate to `http://127.0.0.1:8000/`.

### Creating a New Paste

- Navigate to `/create/` to create a new paste.
- Fill in the title, content, expiration time, and optionally, upload a file and set a password.
- Submit the form to generate a unique code for your paste.

### Retrieving a Paste

- To retrieve a paste, go to `/retrieve/<paste_code>/`.
- If the paste is password-protected, you will be prompted to enter the password.
- You can view or download the associated file if available.

### Searching for a Paste

- Enter the unique code of the paste in the search box on the homepage to quickly find and retrieve it.

## Contributing

Contributions are welcome! If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
