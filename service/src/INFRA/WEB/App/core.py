"""core module."""
from .libs import *

dotenv_path = Path(ENV_PATH)
load_dotenv(dotenv_path=dotenv_path)
app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)
config = NaverConfig(app)
pksalt = config.core.myVariables["PKSALT"]
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy()
resource_fields = api.model('Resource', {
    'data': fields.Raw,
})
