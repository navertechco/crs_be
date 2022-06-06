"""cosntants module."""
import os

ROUTES_PATH = os.path.abspath(__file__)
APP_DIR = os.path.dirname(ROUTES_PATH)
web_DIR = os.path.dirname(APP_DIR)
infra_DIR = os.path.dirname(web_DIR)
SRC_DIR = os.path.dirname(infra_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
STATIC = os.path.join(web_DIR, ("static/"))
TEMPLATE_FOLDER = os.path.join(STATIC, ("templates/"))
UPLOAD_FOLDER = os.path.join(STATIC, ("uploads/"))
ALLOWED_EXTENSIONS = {"xlsx", "csv"}
ENV_PATH = os.path.join(ROOT_DIR, (".env"))
TOKEN="gAAAAABhjtSOlFafpsgJ70Sx11gM7Iv_6RuTpnOs1UWf4ELEnYC1gsvx7E2OZjRAUkkflPMXqR7ua7MtC7Y3LCWoB8uo5lmBV-Sns1lIpIy0YPuPXhdPx96We9xqbRcEylp8Fz91PAQf"
MAINTENANCE = Exception("Sorry, We are in maintenance")