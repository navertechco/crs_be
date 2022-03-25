"""cosntants module."""
import os

ROUTES_PATH = os.path.abspath(__file__)
APP_DIR = os.path.dirname(ROUTES_PATH)
WEB_DIR = os.path.dirname(APP_DIR)
INFRA_DIR = os.path.dirname(WEB_DIR)
SRC_DIR = os.path.dirname(INFRA_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
STATIC = os.path.join(WEB_DIR, ('static/'))
TEMPLATE_FOLDER = os.path.join(STATIC, ('templates/'))
UPLOAD_FOLDER = os.path.join(STATIC, ('uploads/'))
ALLOWED_EXTENSIONS = {'xlsx', 'csv'}
ENV_PATH = os.path.join(ROOT_DIR, ('.env'))
