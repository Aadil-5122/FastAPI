# FastAPI

This repository provides a step-by-step introduction to FastAPI, a modern, high-performance web framework for building APIs with Python. The tutorial is organized into several directories, each focusing on different aspects of API development.

## Directory Structure

### 1. `basicIntro`
Contains basic code to introduce the audience to FastAPI.

- `main.py`: Entry point of the FastAPI application.
- `pathParameter.py`: Demonstrates the usage of path parameters in API endpoints.
- `queryParameter.py`: Explains how to use query parameters in API endpoints.
- `requestBody.py`: Illustrates handling request bodies in API requests.

### 2. `blogIntro`
Provides an overview of the basic structure for creating blogs and users.

- `database.py`: Manages the database connection and interactions.
- `hashing.py`: Contains functions for hashing passwords.
- `main.py`: Entry point of the application.
- `models.py`: Defines data models for blogs and users.
- `schemas.py`: Contains Pydantic schemas for serialization and validation.

### 3. `blogAPIRoute`
Introduces level 1 refactoring by organizing routes into a sub-directory.

- `routers/user.py`: Handles user-related API routes.
- `routers/blog.py`: Manages blog-related API routes.
- `database.py`: Manages the database connection and interactions.
- `hashing.py`: Contains functions for hashing passwords.
- `main.py`: Entry point of the application.
- `models.py`: Defines data models for blogs and users.
- `schemas.py`: Contains Pydantic schemas for serialization and validation.

### 4. `blogRepo`
Introduces level 2 refactoring by adding a repository sub-directory.

- `repository/user.py`: Contains functions for user-related database operations.
- `repository/blog.py`: Contains functions for blog-related database operations.
- `database.py`: Manages the database connection and interactions.
- `hashing.py`: Contains functions for hashing passwords.
- `main.py`: Entry point of the application.
- `models.py`: Defines data models for blogs and users.
- `schemas.py`: Contains Pydantic schemas for serialization and validation.

### 5. `blogAuth`
Focuses on authentication of endpoints and implements a login system using JWT Tokens.

- `token.py`: Contains functions for token generation and validation.
- `oauth2.py`: Implements OAuth2 authentication.
- `routers/authentication.py`: Defines authentication routes.
- `database.py`: Manages the database connection and interactions.
- `hashing.py`: Contains functions for hashing passwords.
- `main.py`: Entry point of the application.
- `models.py`: Defines data models for blogs and users.
- `schemas.py`: Contains Pydantic schemas for serialization and validation.

## Getting Started

To run the tutorial, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Navigate to the desired directory (e.g., `basicIntro`, `blogIntro`, etc.).
3. Execute the `main.py` file to start the FastAPI application.

## Contributing

Feel free to contribute to this tutorial by opening issues, suggesting improvements, or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 😊

## Acknowledgements

This repository was inspired by the teachings of @sarthaksavvy.

...
