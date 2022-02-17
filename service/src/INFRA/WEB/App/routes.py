import os
import ast
from flask_restx import Api, Resource, reqparse, fields 
from flask import Flask, request,render_template, make_response
from flask import  flash,  redirect, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from naver_web import *
from naver_config import NaverConfig
from naver_core import *
from dotenv import load_dotenv
from pathlib import Path
from .recoveryform import RecoveryForm
 

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
#ENV LOCAL
ENV_PATH = os.path.join(ROOT_DIR, ('.env'))
dotenv_path = Path(ENV_PATH)
load_dotenv(dotenv_path=dotenv_path)




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



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

def removeBytePrefix(value):
    """Method to remove the byte prefix from the response
    Args:
        value (value): value to be decorated
        
    Returns:
        value: Replaced value
    """
    return str(value).replace("b'","").replace("'","")

def decryptdata(): 
    data = request.headers.get('token')
    tokendecrypted = decrypt(encrypt(pksalt, pksalt), pksalt)
    salt = removeBytePrefix(tokendecrypted.decode('utf8'))
    jdata = removeBytePrefix(request.get_json(force=True)['data']).encode('utf8')
    res = decrypt(jdata, salt).decode('utf8')
    jsondata = ast.literal_eval(jsonConvert(res))
    data = {"data":jsondata}
    return data

def encrypted(function):
    """Method decorator to encrypt the response
    Args:
        function (function): Function to be decorated
    Returns:
        function: Decorated function
    """    
    def wrapper(data):
        
        f= function
        res = f(data)
        res['data']=str(encrypt(str(res['data']), pksalt))
        return res
    return wrapper






@app.route('/Admin/UploadCatalog', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('empty.html')
         
    # return render_template('upload.html')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''



#region admin
from src.BUSINESS.Admin.CreateCatalog import FSCreateCatalog
@api.route('/Admin/CreateCatalog')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}'})
class CreateCatalog(Resource):
    def post(self):
        """Método para crear catalogo
        Returns:
            json: {"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        input = request.get_json(force=True)
        return FSCreateCatalog(input)
#endregion
 

#region process
from src.BUSINESS.System.ProcessOptions import FSProcessOptions
@api.route('/System/ProcessOptions')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class ProcessOptions(Resource):
    def post(self):
        """Método para procesar opciones de inclusión
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSProcessOptions(data)
#endregion


#region catalog
from src.BUSINESS.System.FindCatalog import FSFindCatalog
@api.route('/System/FindCatalog')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class FindCatalog(Resource):
    def post(self):
        """Método para mostrar catálogos
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSFindCatalog(data)
#endregion
#region user
from src.BUSINESS.User.Confirm import FSConfirm
@api.route('/User/Confirm')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class Confirm(Resource):
    def get(self):
        """Método para Confirmar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        parser = reqparse.RequestParser()
        parser.add_argument('confirmation')
        data = parser.parse_args()
        return FSConfirm(data)
    
from src.BUSINESS.User.Connect import FSConnect
@api.route('/User/Connect')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class Connect(Resource):
    def head(self):
        """Método Inicial para conectar un usuario
        Returns:
            header: {"state":True/False, "data":salt}
        """
        res = FSConnect(None)
        return True, 201, {'token': removeBytePrefix(str(res))}
    # @encrypted
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        try:
            data = request.get_json(force=True)
            # return FSConnect(decryptdata())
            return FSConnect(data) 
        except Exception as e:
            print(e)
            return ErrorResponse(e) 
        
     
from src.BUSINESS.User.Logout import FSLogout
@api.route('/User/Logout')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class Logout(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSLogout(data) 
#endregion
#region Client
from src.BUSINESS.Client.PlayTour import FSPlayTour
import binascii
 
@api.route('/Client/PlayTour/<slug>')
@api.param('slug', 'video playlist')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class PlayTour(Resource):
    def get(self, slug):
        """Método para reproducir un tour

        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """ 
        headers = {'Content-Type': 'text/html'} 
        res = FSPlayTour(slug)     
        if res is None:
            return make_response(render_template('empty.html'),200,headers)  
        # data = json.dumps(res) 
        # hash = binascii.hexlify(data.encode('utf-8'))
        return make_response(render_template('playlist.html',  data=res),200,headers) 
    
from src.BUSINESS.Client.ClientEdit import FSClientEdit
@api.route('/Client/Edit')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class ClientEdit(Resource):
    def post(self):
        """Método para Editar un cliente
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSClientEdit(data) 
#endregion
#region Tour
from src.BUSINESS.Tour.FindTour import FSFindTour
@api.route('/Tour/FindTour')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}'})
class FindTour(Resource):
    def post(self): 
        """_summary_

        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSFindTour(input) 
    
from src.BUSINESS.Tour.CalculateNetRate import FSCalculateNetRate
@api.route('/Tour/CalculateNetRate')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}'})
class CalculateNetRate(Resource):
    def post(self): 
        """_summary_

        Returns:
            _type_: _description_
        """
        input = request.get_json(force=True)
        return FSCalculateNetRate(input) 
from src.BUSINESS.Tour.TourEdit import FSTourEdit
@api.route('/Tour/Edit')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}'})
class TourEdit(Resource):
    def post(self):
        """Método para Editar un Presupuesto
        Returns:
            json: {"state":True/False, "input":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        input = request.get_json(force=True)
        return FSTourEdit(input) 
    
from src.BUSINESS.Tour.NewTour import FSNewTour
@api.route('/Tour/NewTour')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class NewTour(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSNewTour(data) 
    
from src.BUSINESS.Tour.ProcessTour import FSProcessTour
@api.route('/Tour/ProcessTour')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class ProcessTour(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSProcessTour(data) 
from src.BUSINESS.Tour.PromoteTour import FSPromoteTour
@api.route('/Tour/PromoteTour')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class PromoteTour(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSPromoteTour(data) 
    
from src.BUSINESS.Tour.UpdateTour import FSUpdateTour
@api.route('/Tour/UpdateTour')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class UpdateTour(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSUpdateTour(data) 
#endregion
#region File
from src.BUSINESS.File.MakeEmail import FSMakeEmail
@api.route('/Email/MakeEmail')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class MakeEmail(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSMakeEmail(data) 
from src.BUSINESS.File.MakePdf import FSMakePdf
@api.route('/Email/MakePdf')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class MakePdf(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSMakePdf(data) 
    
from src.BUSINESS.File.MakePlaylist import FSMakePlaylist
@api.route('/Email/MakePlaylist')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class MakePlaylist(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSMakePlaylist(data) 
#endregion
 
#region Agent
from src.BUSINESS.Agent.Start import FSStart
@api.route('/Agent/Start')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class Start(Resource):
    def head(self):
        """Método Inicial para conectar un usuario
        Returns:
            header: {"state":True/False, "data":salt}
        """
        res = FSStart(None)
        return True, 201, {'token': removeBytePrefix(str(res))}
    # @encrypted
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSStart(decryptdata())
        return FSStart(data)

from src.BUSINESS.Agent.GetExperience import FSGetExperience
@api.route('/Agent/GetExperience')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class GetExperience(Resource):
    # @encrypted
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSGetExperience(decryptdata())
        return FSGetExperience(data)    


from src.BUSINESS.Agent.GetDestination import FSGetDestination
@api.route('/Agent/GetDestination')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class GetDestination(Resource):
    # @encrypted
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSGetDestination(decryptdata())
        return FSGetDestination(data)    
    
from src.BUSINESS.Agent.Query import FSQuery
@api.route('/Agent/Query')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class Query(Resource):
    # @encrypted
    def post(self):
        """Método para conectar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        # return FSQuery(decryptdata())
        return FSQuery(data) 
#endregion6