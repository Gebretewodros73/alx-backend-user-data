# User Authentication Service

This repository contains an implementation of a user authentication service using Flask, SQLAlchemy, and Bcrypt.

## Tasks

### Task 0: User model

Create a SQLAlchemy model named User with attributes: id, email, hashed_password, session_id, and reset_token.

### Task 1: Create User

Implement the `add_user` method in the `DB` class to add a user to the database.

### Task 2: Find User

Implement the `find_user_by` method in the `DB` class to find a user based on arbitrary keyword arguments.

### Task 3: Update User

Implement the `update_user` method in the `DB` class to update user attributes.

### Task 4: Hash Password

Define a `_hash_password` method in the `auth` module to hash passwords using bcrypt.

### Task 5: Register User

Implement the `register_user` method in the `Auth` class to register a user and hash their password.

### Task 6: Basic Flask App

Set up a basic Flask app with a single GET route ("/") returning a JSON payload.

### Task 7: Register User (Flask)

Implement the endpoint to register a user (POST /users) and handle user existence.

### Task 8: Credentials Validation

Implement the `valid_login` method in the `Auth` class for validating login credentials.

### Task 9: Generate UUIDs

Implement a `_generate_uuid` function in the `auth` module to generate UUIDs.

### Task 10: Get Session ID

Implement the `create_session` method in the `Auth` class to create a session for a user.

### Task 11: Log In

Implement a login function for the POST /sessions route, creating a session for a user.

### Task 12: Find User by Session ID

Implement the `get_user_from_session_id` method in the `Auth` class.

### Task 13: Destroy Session

Implement the `destroy_session` method in the `Auth` class.

### Task 14: Log Out

Implement a logout function for the DELETE /sessions route.

### Task 15: User Profile

Implement a profile function for the GET /profile route.

### Task 16: Generate Reset Password Token

Implement the `get_reset_password_token` method in the `Auth` class.

### Task 17: Get Reset Password Token

Implement a function for the POST /reset_password route to generate and return a reset token.

### Task 18: Update Password

Implement the `update_password` method in the `Auth` class.

### Task 19: Update Password End-Point

Implement the update_password function for the PUT /reset_password route.

### Task 20: End-to-End Integration Test

Create a main module with functions for integration testing various endpoints using the `requests` module.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/alx-backend-user-data.git
```

1. Navigate to the project directory:

```bash
cd alx-backend-user-data/0x03-user_authentication_service
```

2. Follow the instructions for each task in the provided README.md.

## Rum

1. Run the Flask app:

```bash
python app.py
```

Open a new terminal and run the integration tests:

```bash
python main.py
```

If everything is correct, there should be no output.
