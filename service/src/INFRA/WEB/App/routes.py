import os
import ast
from flask_restx import Api, Resource, reqparse, fields 
from flask import Flask, request,render_template, make_response
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
ENV_PATH = os.path.join(ROOT_DIR, ('.env'))

app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC)
api = Api(app) 
 
dotenv_path = Path(ENV_PATH)
load_dotenv(dotenv_path=dotenv_path)
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
        data = request.get_json(force=True)
        # return FSConnect(decryptdata())
        return FSConnect(data)
from src.BUSINESS.User.SignIn import FSSignIn
@api.route('/User/SignIn')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class SignIn(Resource):
    def post(self):
        """Método para logonear un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSSignIn(data)
from src.BUSINESS.User.SignUp import FSSignUp
@api.route('/User/SignUp')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class SignUp(Resource):
    def post(self):
        """Método para registrar un usuario
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSSignUp(data) 
from src.BUSINESS.User.Forgot import FSForgot
@api.route('/User/Forgot')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class Forgot(Resource):
    def post(self):
        """Método para recuperar contraseña Backend
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        form = RecoveryForm(request.form)
        if  form.validate():
            parser = reqparse.RequestParser()
            parser.add_argument('confirmation')
            data = parser.parse_args()
            input = {'password':request.form['password'], 'confirmation':data['confirmation']}
            FSForgot(input)
        headers = {'Content-Type': 'text/html'} 
        return make_response(render_template('success.html'),200,headers) 
    def get(self):
        """Método para recuperar contraseña Frontend
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        form = RecoveryForm(request.form)
        parser = reqparse.RequestParser()
        parser.add_argument('confirmation')
        data = parser.parse_args()
        headers = {'Content-Type': 'text/html'} 
        return make_response(render_template('recovery.html', form=form, data=data),200,headers) 
 
     
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
@api.route('/Client/PlayTour/<slug>')
@api.param('slug', 'video playlist')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class PlayTour(Resource):
    def get(self, slug):
        """Método para reproducir un tour

        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """        
        return FSPlayTour(slug) 
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
#region Quote
from src.BUSINESS.Quote.QuoteEdit import FSQuoteEdit
@api.route('/Quote/Edit')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class QuoteEdit(Resource):
    def post(self):
        """Método para Editar un Presupuesto
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSQuoteEdit(data) 
from src.BUSINESS.Quote.NewQuote import FSNewQuote
@api.route('/Quote/NewQuote')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class NewQuote(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSNewQuote(data) 
    
from src.BUSINESS.Quote.ProcessQuote import FSProcessQuote
@api.route('/Quote/ProcessQuote')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class ProcessQuote(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSProcessQuote(data) 
from src.BUSINESS.Quote.PromoteQuote import FSPromoteQuote
@api.route('/Quote/PromoteQuote')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class PromoteQuote(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSPromoteQuote(data) 
    
from src.BUSINESS.Quote.UpdateQuote import FSUpdateQuote
@api.route('/Quote/UpdateQuote')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class UpdateQuote(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSUpdateQuote(data) 
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
#region TrvExp
from src.BUSINESS.TrvExp.AssignTravelExpert import FSAssignTravelExpert
@api.route('/TrvExp/AssignTravelExpert')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class AssignTravelExpert(Resource):
    def post(self):
        """Método para salir de session
        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSAssignTravelExpert(data) 
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
    
#endregion