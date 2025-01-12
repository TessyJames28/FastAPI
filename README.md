# Blog Application

This is a blog application built using **FastAPI**, SQLAlchemy, and OAuth2 for authentication. The app allows users to create, read, update, and delete blog posts while providing secure user authentication and relationship mapping between users and blogs.

---

## Features

- User Registration and Authentication using **OAuth2**.
- CRUD functionality for blog posts:
  - **Create**: Add a new blog post.
  - **Read**: Retrieve blog posts.
  - **Update**: Edit existing blog posts.
  - **Delete**: Remove blog posts.
- User-blog relationships using SQLAlchemy ORM.
- Pydantic models for data validation.

---

## Technologies Used

- **Python**: Backend development.
- **FastAPI**: API framework for building web applications.
- **SQLAlchemy**: ORM for database interaction.
- **SQLite/MySQL/PostgreSQL**: Database management (select one as per your setup).
- **Pydantic**: Data validation.
- **OAuth2**: Authentication mechanism.

---

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- Python (>= 3.9)
- Pip
- Virtualenv (optional)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/TessyJames28/FastAPI.git
   cd blog-app

## API Endpoints

### Authentication
- **POST** `/token` - Obtain an access token.

### Users
- **POST** `/users/` - Register a new user.
- **GET** `/users/{id}` - Retrieve a specific user.

### Blogs
- **GET** `/blogs/` - Retrieve all blogs.
- **POST** `/blogs/` - Create a new blog.
- **GET** `/blogs/{id}` - Retrieve a specific blog.
- **PUT** `/blogs/{id}` - Update a blog.
- **DELETE** `/blogs/{id}` - Delete a blog.
