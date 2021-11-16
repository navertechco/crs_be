
from flask_restx import Api, Resource, reqparse, fields
from flask import Flask, request 
from flask import render_template, make_response
import os, json
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(ROOT_DIR, os.path.abspath('service/assets/html/')) 
STATIC = os.path.join(ROOT_DIR, os.path.abspath('service/assets/')) 
ENV = os.path.join(ROOT_DIR, os.path.abspath('service/.env')) 
app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
api = Api(app) 
from .recoveryform import RecoveryForm
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from naver_web import *
from naver_config import NaverConfig
from naver_core import *
import ast 
 
from dotenv import load_dotenv
from pathlib import Path
 

dotenv_path = Path(ENV)
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
from src.User.Confirm import FSConfirm
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
    
from src.User.Connect import FSConnect
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
from src.User.SignIn import FSSignIn
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
from src.User.SignUp import FSSignUp
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
from src.User.Forgot import FSForgot
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
 
     
from src.User.Logout import FSLogout
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

from src.Client.EditDemographics import FSEditDemographics
@api.route('/Client/EditDemographics')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class EditDemographics(Resource):
    def post(self):
        """Método para salir de session

        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSEditDemographics(data) 
#endregion

#region Quote

from src.Quote.NewQuote import FSNewQuote
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
    
from src.Quote.ProccessQuote import FSProccessQuote
@api.route('/Quote/ProccessQuote')
@api.doc(body=resource_fields, responses={400:"Error: BAD REQUEST",200:'{"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}'})
class ProccessQuote(Resource):
    def post(self):
        """Método para salir de session

        Returns:
            json: {"state":True/False, "data":any, "message":if error ? str : None , "code":if error ? str : None}
        """
        data = request.get_json(force=True)
        return FSProccessQuote(data) 

from src.Quote.PromoteQuote import FSPromoteQuote
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
    
from src.Quote.UpdateQuote import FSUpdateQuote
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

from src.File.MakeEmail import FSMakeEmail
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


from src.File.MakePdf import FSMakePdf
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
    
from src.File.MakePlaylist import FSMakePlaylist
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

from src.TrvExp.AssignTravelExpert import FSAssignTravelExpert
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


from src.Agent.Start import FSStart
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