"""
This script runs the src application using a development server.
"""
import os
from os import environ
from src.WEB import app
from dotenv import load_dotenv
from pathlib import Path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.join(ROOT_DIR, '.env') 


if __name__ == '__main__':
    dotenv_path = Path(ENV)
    load_dotenv(dotenv_path=dotenv_path)

    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        HOST = environ.get('SERVER_HOST', 'localhost')
    except ValueError:
        PORT = 5001
        HOST = "0.0.0.0"
    app.run(host="0.0.0.0", port=PORT)
