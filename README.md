# Blog Platform

A simple blog platform built using Flask for the backend and styled with Bootstrap for a clean, responsive user interface. This platform supports user authentication, creating, editing, and viewing blog posts.

---

## Features

- User authentication (register, login, logout)
- Create, view, edit, and delete blog posts
- Responsive design using Bootstrap
- Secure password storage with hashing

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap (CSS/JS)
- **Database**: SQLite (via SQLAlchemy ORM)

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/username/blog-platform.git
   cd blog-platform
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Flask:
   ```bash
   pip install flask flask-sqlalchemy flask-wtf flask-bcrypt
   ```

4. Run the development server:
   ```bash
   flask run
   ```

5. Open the app in your browser at `http://127.0.0.1:5000`.

---

## Project Structure

```
blog-platform/
│
├── app.py                # Main application entry point
├── models.py             # Database models
├── views.py              # Route handlers (views)
├── auth.py               # Authentication routes
├── templates/            # HTML templates
├── instance/             # Holds configuration and database file
└── .gitignore            # Ignored files for Git
```

---

## Future Enhancements

- Add user profiles with avatars
- Implement a comments section for posts
- Add pagination for posts
- Create an admin dashboard for managing content

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
