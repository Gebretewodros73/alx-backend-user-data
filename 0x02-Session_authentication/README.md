# 0x02. Session authentication

## Tasks

### Task 0: Et moi et moi et moi!

- **Description:** Copy all your work of the 0x06. Basic authentication project in this new folder.
- **Details:**
  - You implemented a Basic authentication for giving you access to all User endpoints.
  - Add a new endpoint: GET /users/me to retrieve the authenticated User object.
- **Instructions:**
  - Copy folders models and api from the previous project 0x06. Basic authentication
  - Update @app.before_request in api/v1/app.py
  - Update method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py

### Task 1: Empty session

- **Description:** Create a class SessionAuth that inherits from Auth.
- **Details:**
  - Validate if everything inherits correctly without any overloading
- **Instructions:**
  - Create SessionAuth class
  - Update api/v1/app.py for using SessionAuth instance

### Task 2: Create a session

- **Description:** Update SessionAuth class to create a Session ID for a user_id.
- **Details:**
  - Create a class attribute user_id_by_session_id initialized by an empty dictionary
- **Instructions:**
  - Update SessionAuth class with create_session method

### Task 3: User ID for Session ID

- **Description:** Update SessionAuth class to return a User ID based on a Session ID.
- **Details:**
  - Create an instance method def user_id_for_session_id(self, session_id: str = None) -> str
- **Instructions:**
  - Update SessionAuth class with user_id_for_session_id method

### Task 4: Session cookie

- **Description:** Update api/v1/auth/auth.py to return a cookie value from a request.
- **Details:**
  - Create the method def session_cookie(self, request=None)
- **Instructions:**
  - Update api/v1/auth/auth.py with session_cookie method

### Task 5: Before request

- **Description:** Update the @app.before_request method in api/v1/app.py.
- **Details:**
  - Add the URL path /api/v1/auth_session/login/ in the list of excluded paths
- **Instructions:**
  - Update @app.before_request in api/v1/app.py

### Task 6: Use Session ID for identifying a User

- **Description:** Update SessionAuth class to return a User instance based on a cookie value.
- **Details:**
  - Create an instance method def current_user(self, request=None)
- **Instructions:**
  - Update SessionAuth class with current_user method

### Task 7: New view for Session Authentication

- **Description:** Create a new Flask view that handles all routes for the Session authentication.
- **Details:**
  - Create a route POST /auth_session/login
- **Instructions:**
  - Create a new view in api/v1/views/session_auth.py

### Task 8: Logout

- **Description:** Update the class SessionAuth by adding a new method def destroy_session(self, request=None).
- **Details:**
  - Create the method to delete the user session / logout
- **Instructions:**
  - Update the class SessionAuth and add the route DELETE /api/v1/auth_session/logout in api/v1/views/session_auth.py
