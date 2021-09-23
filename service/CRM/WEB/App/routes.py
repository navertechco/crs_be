from flask import request
from flask_restplus import Namespace, Resource
from flask import Flask
# from flask_restplus import Api
# from .routes import routes

app = Flask(__name__)
# api = Api(app)
# api.add_namespace(routes)

# routes = Namespace('api', description='api')




from CRM.User.SingIn import FSSingIn
@app.route('/CRM/User/SingIn',methods='POST')
def SingIn():
    return FSSingIn(request.get_json(force=True).get("username"), request.get_json(force=True).get("password"))

from CRM.User.Register import FSRegister
@app.route('/CRM/User/Register',methods='POST')
def Register():
    return FSRegister(request.get_json(force=True).get("username"), request.get_json(force=True).get("password"))

from CRM.User.ResetPassword import FSResetPassword
@app.route('/CRM/User/ResetPassword',methods='POST')
def ResetPassword():
    return FSResetPassword(request.get_json(force=True).get("username"))

from CRM.User.ForgotUsername import FSForgotUsername
@app.route('/CRM/User/ForgotUsername',methods='POST')
def ForgotUsername():
    return FSForgotUsername(request.get_json(force=True).get("email"))

from CRM.User.ForgotPassword import FSForgotPassword
@app.route('/CRM/User/ForgotPassword',methods='POST')
def ForgotPassword():
    return FSForgotPassword(request.get_json(force=True).get("email"))

from CRM.User.Logout import FSLogout
@app.route('/CRM/User/Logout',methods='POST')
def Logout():
    return FSLogout()

from CRM.Agent.CreateTour import FSCreateTour
@app.route('/CRM/Agent/CreateTour',methods='POST')
def CreateTour():
    return FSCreateTour(request.get_json(force=True).get("data"))

from CRM.Agent.DeleteTour import FSDeleteTour
@app.route('/CRM/Agent/DeleteTour',methods='POST')
def DeleteTour():
    return FSDeleteTour(request.get_json(force=True).get("tour_id"))

from CRM.Agent.GetTourDetail import FSGetTourDetail
@app.route('/CRM/Agent/GetTourDetail',methods='POST')
def GetTourDetail():
    return FSGetTourDetail(request.get_json(force=True).get("tour_id"))

from CRM.Agent.UpdateTour import FSUpdateTour
@app.route('/CRM/Agent/UpdateTour',methods='POST')
def UpdateTour():
    return FSUpdateTour(request.get_json(force=True).get("data"))

from CRM.Agent.FindTour import FSFindTour
@app.route('/CRM/Agent/FindTour',methods='POST')
def FindTour():
    return FSFindTour(request.get_json(force=True).get("tour_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.Agent.GetTourList import FSGetTourList
@app.route('/CRM/Agent/GetTourList',methods='POST')
def GetTourList():
    return FSGetTourList()

from CRM.Agent.CreatePoll import FSCreatePoll
@app.route('/CRM/Agent/CreatePoll',methods='POST')
def CreatePoll():
    return FSCreatePoll(request.get_json(force=True).get("data"))

from CRM.Agent.DeletePoll import FSDeletePoll
@app.route('/CRM/Agent/DeletePoll',methods='POST')
def DeletePoll():
    return FSDeletePoll(request.get_json(force=True).get("poll_id"))

from CRM.Agent.GetPollDetail import FSGetPollDetail
@app.route('/CRM/Agent/GetPollDetail',methods='POST')
def GetPollDetail():
    return FSGetPollDetail(request.get_json(force=True).get("poll_id"))

from CRM.Agent.UpdatePoll import FSUpdatePoll
@app.route('/CRM/Agent/UpdatePoll',methods='POST')
def UpdatePoll():
    return FSUpdatePoll(request.get_json(force=True).get("data"))

from CRM.Agent.FindPoll import FSFindPoll
@app.route('/CRM/Agent/FindPoll',methods='POST')
def FindPoll():
    return FSFindPoll(request.get_json(force=True).get("poll_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.Agent.GetPollList import FSGetPollList
@app.route('/CRM/Agent/GetPollList',methods='POST')
def GetPollList():
    return FSGetPollList()

from CRM.ExpDeveloper.CreateSupplier import FSCreateSupplier
@app.route('/CRM/ExpDeveloper/CreateSupplier',methods='POST')
def CreateSupplier():
    return FSCreateSupplier(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.DeleteSupplier import FSDeleteSupplier
@app.route('/CRM/ExpDeveloper/DeleteSupplier',methods='POST')
def DeleteSupplier():
    return FSDeleteSupplier(request.get_json(force=True).get("supplier_id"))

from CRM.ExpDeveloper.UpdateSupplier import FSUpdateSupplier
@app.route('/CRM/ExpDeveloper/UpdateSupplier',methods='POST')
def UpdateSupplier():
    return FSUpdateSupplier(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.FindSupplier import FSFindSupplier
@app.route('/CRM/ExpDeveloper/FindSupplier',methods='POST')
def FindSupplier():
    return FSFindSupplier(request.get_json(force=True).get("supplier_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.ExpDeveloper.GetSupplierList import FSGetSupplierList
@app.route('/CRM/ExpDeveloper/GetSupplierList',methods='POST')
def GetSupplierList():
    return FSGetSupplierList()

from CRM.ExpDeveloper.CreateDestiny import FSCreateDestiny
@app.route('/CRM/ExpDeveloper/CreateDestiny',methods='POST')
def CreateDestiny():
    return FSCreateDestiny(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.DeleteDestiny import FSDeleteDestiny
@app.route('/CRM/ExpDeveloper/DeleteDestiny',methods='POST')
def DeleteDestiny():
    return FSDeleteDestiny(request.get_json(force=True).get("destiny_id"))

from CRM.ExpDeveloper.GetDestinyDetail import FSGetDestinyDetail
@app.route('/CRM/ExpDeveloper/GetDestinyDetail',methods='POST')
def GetDestinyDetail():
    return FSGetDestinyDetail(request.get_json(force=True).get("destiny_id"))

from CRM.ExpDeveloper.UpdateDestiny import FSUpdateDestiny
@app.route('/CRM/ExpDeveloper/UpdateDestiny',methods='POST')
def UpdateDestiny():
    return FSUpdateDestiny(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.FindDestiny import FSFindDestiny
@app.route('/CRM/ExpDeveloper/FindDestiny',methods='POST')
def FindDestiny():
    return FSFindDestiny(request.get_json(force=True).get("destiny_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.ExpDeveloper.GetDestinyList import FSGetDestinyList
@app.route('/CRM/ExpDeveloper/GetDestinyList',methods='POST')
def GetDestinyList():
    return FSGetDestinyList()

from CRM.ExpDeveloper.CreateActivity import FSCreateActivity
@app.route('/CRM/ExpDeveloper/CreateActivity',methods='POST')
def CreateActivity():
    return FSCreateActivity(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.DeleteActivity import FSDeleteActivity
@app.route('/CRM/ExpDeveloper/DeleteActivity',methods='POST')
def DeleteActivity():
    return FSDeleteActivity(request.get_json(force=True).get("activity_id"))

from CRM.ExpDeveloper.GetActivityDetail import FSGetActivityDetail
@app.route('/CRM/ExpDeveloper/GetActivityDetail',methods='POST')
def GetActivityDetail():
    return FSGetActivityDetail(request.get_json(force=True).get("activity_id"))

from CRM.ExpDeveloper.UpdateActivity import FSUpdateActivity
@app.route('/CRM/ExpDeveloper/UpdateActivity',methods='POST')
def UpdateActivity():
    return FSUpdateActivity(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.FindActivity import FSFindActivity
@app.route('/CRM/ExpDeveloper/FindActivity',methods='POST')
def FindActivity():
    return FSFindActivity(request.get_json(force=True).get("activity_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.ExpDeveloper.GetActivityList import FSGetActivityList
@app.route('/CRM/ExpDeveloper/GetActivityList',methods='POST')
def GetActivityList():
    return FSGetActivityList()

from CRM.ExpDeveloper.CreateExperience import FSCreateExperience
@app.route('/CRM/ExpDeveloper/CreateExperience',methods='POST')
def CreateExperience():
    return FSCreateExperience(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.DeleteExperience import FSDeleteExperience
@app.route('/CRM/ExpDeveloper/DeleteExperience',methods='POST')
def DeleteExperience():
    return FSDeleteExperience(request.get_json(force=True).get("experience_id"))

from CRM.ExpDeveloper.GetExperienceDetail import FSGetExperienceDetail
@app.route('/CRM/ExpDeveloper/GetExperienceDetail',methods='POST')
def GetExperienceDetail():
    return FSGetExperienceDetail(request.get_json(force=True).get("experience_id"))

from CRM.ExpDeveloper.UpdateExperience import FSUpdateExperience
@app.route('/CRM/ExpDeveloper/UpdateExperience',methods='POST')
def UpdateExperience():
    return FSUpdateExperience(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.FindExperience import FSFindExperience
@app.route('/CRM/ExpDeveloper/FindExperience',methods='POST')
def FindExperience():
    return FSFindExperience(request.get_json(force=True).get("experience_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.ExpDeveloper.GetExperienceList import FSGetExperienceList
@app.route('/CRM/ExpDeveloper/GetExperienceList',methods='POST')
def GetExperienceList():
    return FSGetExperienceList()

from CRM.ExpDeveloper.CreateVideo import FSCreateVideo
@app.route('/CRM/ExpDeveloper/CreateVideo',methods='POST')
def CreateVideo():
    return FSCreateVideo(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.DeleteVideo import FSDeleteVideo
@app.route('/CRM/ExpDeveloper/DeleteVideo',methods='POST')
def DeleteVideo():
    return FSDeleteVideo(request.get_json(force=True).get("video_id"))

from CRM.ExpDeveloper.UpdateVideo import FSUpdateVideo
@app.route('/CRM/ExpDeveloper/UpdateVideo',methods='POST')
def UpdateVideo():
    return FSUpdateVideo(request.get_json(force=True).get("data"))

from CRM.ExpDeveloper.FindVideo import FSFindVideo
@app.route('/CRM/ExpDeveloper/FindVideo',methods='POST')
def FindVideo():
    return FSFindVideo(request.get_json(force=True).get("video_id"), request.get_json(force=True).get("contact_id"), request.get_json(force=True).get("props"))

from CRM.ExpDeveloper.GetVideoList import FSGetVideoList
@app.route('/CRM/ExpDeveloper/GetVideoList',methods='POST')
def GetVideoList():
    return FSGetVideoList()

from CRM.TravelExpert.CreateUpSelling import FSCreateUpSelling
@app.route('/CRM/TravelExpert/CreateUpSelling',methods='POST')
def CreateUpSelling():
    return FSCreateUpSelling(request.get_json(force=True).get("data"))

from CRM.TravelExpert.DeleteUpSelling import FSDeleteUpSelling
@app.route('/CRM/TravelExpert/DeleteUpSelling',methods='POST')
def DeleteUpSelling():
    return FSDeleteUpSelling(request.get_json(force=True).get("upselling_id"))

from CRM.TravelExpert.GetUpSellingDetail import FSGetUpSellingDetail
@app.route('/CRM/TravelExpert/GetUpSellingDetail',methods='POST')
def GetUpSellingDetail():
    return FSGetUpSellingDetail(request.get_json(force=True).get("upselling_id"))

from CRM.TravelExpert.UpdateUpSelling import FSUpdateUpSelling
@app.route('/CRM/TravelExpert/UpdateUpSelling',methods='POST')
def UpdateUpSelling():
    return FSUpdateUpSelling(request.get_json(force=True).get("data"))

from CRM.TravelExpert.FindUpSelling import FSFindUpSelling
@app.route('/CRM/TravelExpert/FindUpSelling',methods='POST')
def FindUpSelling():
    return FSFindUpSelling(request.get_json(force=True).get("upselling_id"), request.get_json(force=True).get("props"))

from CRM.TravelExpert.GetUpSellingList import FSGetUpSellingList
@app.route('/CRM/TravelExpert/GetUpSellingList',methods='POST')
def GetUpSellingList():
    return FSGetUpSellingList()

from CRM.TravelExpert.CreateQuote import FSCreateQuote
@app.route('/CRM/TravelExpert/CreateQuote',methods='POST')
def CreateQuote():
    return FSCreateQuote(request.get_json(force=True).get("data"))

from CRM.TravelExpert.DeleteQuote import FSDeleteQuote
@app.route('/CRM/TravelExpert/DeleteQuote',methods='POST')
def DeleteQuote():
    return FSDeleteQuote(request.get_json(force=True).get("quote_id"))

from CRM.TravelExpert.GetQuoteDetail import FSGetQuoteDetail
@app.route('/CRM/TravelExpert/GetQuoteDetail',methods='POST')
def GetQuoteDetail():
    return FSGetQuoteDetail(request.get_json(force=True).get("quote_id"))

from CRM.TravelExpert.UpdateQuote import FSUpdateQuote
@app.route('/CRM/TravelExpert/UpdateQuote',methods='POST')
def UpdateQuote():
    return FSUpdateQuote(request.get_json(force=True).get("data"))

from CRM.TravelExpert.FindQuote import FSFindQuote
@app.route('/CRM/TravelExpert/FindQuote',methods='POST')
def FindQuote():
    return FSFindQuote(request.get_json(force=True).get("quote_id"), request.get_json(force=True).get("props"))

from CRM.TravelExpert.GetQuoteList import FSGetQuoteList
@app.route('/CRM/TravelExpert/GetQuoteList',methods='POST')
def GetQuoteList():
    return FSGetQuoteList()

from CRM.TravelExpert.CancelTour import FSCancelTour
@app.route('/CRM/TravelExpert/CancelTour',methods='POST')
def CancelTour():
    return FSCancelTour(request.get_json(force=True).get("tour_id"))

from CRM.Admin.CreateUser import FSCreateUser
@app.route('/CRM/Admin/CreateUser',methods='POST')
def CreateUser():
    return FSCreateUser(request.get_json(force=True).get("data"))

from CRM.Admin.DeleteUser import FSDeleteUser
@app.route('/CRM/Admin/DeleteUser',methods='POST')
def DeleteUser():
    return FSDeleteUser(request.get_json(force=True).get("user_id"))

from CRM.Admin.GetUserDetail import FSGetUserDetail
@app.route('/CRM/Admin/GetUserDetail',methods='POST')
def GetUserDetail():
    return FSGetUserDetail(request.get_json(force=True).get("user_id"))

from CRM.Admin.UpdateUser import FSUpdateUser
@app.route('/CRM/Admin/UpdateUser',methods='POST')
def UpdateUser():
    return FSUpdateUser(request.get_json(force=True).get("data"))

from CRM.Admin.FindUser import FSFindUser
@app.route('/CRM/Admin/FindUser',methods='POST')
def FindUser():
    return FSFindUser(request.get_json(force=True).get("user_id"), request.get_json(force=True).get("props"))

from CRM.Admin.GetUserList import FSGetUserList
@app.route('/CRM/Admin/GetUserList',methods='POST')
def GetUserList():
    return FSGetUserList()