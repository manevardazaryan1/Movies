<a id='top'></a>

# Movies

## Movies project - Django.

![Movies collage](static_files/static/images/README-Collage/Movies-Collage.jpg "Movies app")

## Features

- Search for movies (or actors)
- Add actor
- Add movie

## To run this application, you'll need the following software installed on your system:

- **Git:** Ensure you have Git installed on your system. You can download it from https://git-scm.com/downloads.
- **Python:** Verify that you have Python 3.x installed. Check the version using python3 --version in your terminal. If you don't have it, download the appropriate installer from https://www.python.org/downloads/.
- **pip:** Pip is the package installer for Python. Use python3 -m ensurepip to install it if necessary.

## To run this application follow these steps

1. **Clone this repository:**
   git clone [https://github.com/manevardazaryan1/Movies]

2. **Create a Virtual Environment (Recommended):**
    **Using venv (Python 3.3+):**
    cd [REPOSITORY_NAME]  # Navigate to your project directory
    python3 -m venv venv  # Create a virtual environment named 'venv'
    source venv/bin/activate  # Activate the virtual environment

    **Using virtualenv (Older Python versions or external package manager):**
    cd [REPOSITORY_NAME]  # Navigate to your project directory
    virtualenv venv  # Create a virtual environment named 'venv'
    source venv/bin/activate  # Activate the virtual environment

3. **Install Dependencies:**
    pip install -r requirements.txt

4. **Run Database Migrations:**
    python manage.py migrate

5. **Start the Development Server:**
    python manage.py runserver

This command starts the Django development server, typically running at http://127.0.0.1:8000/ by default. You can access your Django application in a web browser at this URL.

[Tap to Top ⬆](#top)