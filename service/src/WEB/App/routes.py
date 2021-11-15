from flask import request
from flask_restx import Namespace, Resource
from flask import Flask
# from flask_restx import Api
# from .routes import routes

app = Flask(__name__)
# api = Api(app)
# api.add_namespace(routes)

# routes = Namespace('api', description='api')




from CRS.User.SingIn import FSSingIn
@app.route('/CRS/User/SingIn',methods='POST')
def SingIn():
    return FSSingIn(request.get_json(force=True).get("username"), request.get_json(force=True).get("password"))

from CRS.User.SingUp import FSSingUp
@app.route('/CRS/User/SingUp',methods='POST')
def SingUp():
    return FSSingUp(request.get_json(force=True).get("username"), request.get_json(force=True).get("password"))

from CRS.User.Reset import FSReset
@app.route('/CRS/User/Reset',methods='POST')
def Reset():
    return FSReset(request.get_json(force=True).get("username"))

from CRS.User.Forgot import FSForgot
@app.route('/CRS/User/Forgot',methods='POST')
def Forgot():
    return FSForgot(request.get_json(force=True).get("email"))

from CRS.User.ListPermission import FSListPermission
@app.route('/CRS/User/ListPermission',methods='POST')
def ListPermission():
    return FSListPermission(request.get_json(force=True).get("email"))

from CRS.User.ListMenu import FSListMenu
@app.route('/CRS/User/ListMenu',methods='POST')
def ListMenu():
    return FSListMenu(request.get_json(force=True).get("data"))

from CRS.User.ListParam import FSListParam
@app.route('/CRS/User/ListParam',methods='POST')
def ListParam():
    return FSListParam(request.get_json(force=True).get("data"))

from CRS.User.EditProfile import FSEditProfile
@app.route('/CRS/User/EditProfile',methods='POST')
def EditProfile():
    return FSEditProfile(request.get_json(force=True).get("data"))

from CRS.User.ListAllAlert import FSListAllAlert
@app.route('/CRS/User/ListAllAlert',methods='POST')
def ListAllAlert():
    return FSListAllAlert(request.get_json(force=True).get("data"))

from CRS.User.ListAllCatalogue import FSListAllCatalogue
@app.route('/CRS/User/ListAllCatalogue',methods='POST')
def ListAllCatalogue():
    return FSListAllCatalogue(request.get_json(force=True).get("data"))

from CRS.User.GetScreen import FSGetScreen
@app.route('/CRS/User/GetScreen',methods='POST')
def GetScreen():
    return FSGetScreen(request.get_json(force=True).get("data"))

from CRS.User.GetTheme import FSGetTheme
@app.route('/CRS/User/GetTheme',methods='POST')
def GetTheme():
    return FSGetTheme(request.get_json(force=True).get("data"))

from CRS.Agent.JoinPoll import FSJoinPoll
@app.route('/CRS/Agent/JoinPoll',methods='POST')
def JoinPoll():
    return FSJoinPoll(request.get_json(force=True).get("data"))

from CRS.Agent.ListAllContact import FSListAllContact
@app.route('/CRS/Agent/ListAllContact',methods='POST')
def ListAllContact():
    return FSListAllContact(request.get_json(force=True).get("data"))

from CRS.Agent.ListContactDetail import FSListContactDetail
@app.route('/CRS/Agent/ListContactDetail',methods='POST')
def ListContactDetail():
    return FSListContactDetail(request.get_json(force=True).get("data"))

from CRS.Agent.CreateContact import FSCreateContact
@app.route('/CRS/Agent/CreateContact',methods='POST')
def CreateContact():
    return FSCreateContact(request.get_json(force=True).get("data"))

from CRS.Agent.EditContact import FSEditContact
@app.route('/CRS/Agent/EditContact',methods='POST')
def EditContact():
    return FSEditContact(request.get_json(force=True).get("data"))

from CRS.Agent.ListAllOpportunity import FSListAllOpportunity
@app.route('/CRS/Agent/ListAllOpportunity',methods='POST')
def ListAllOpportunity():
    return FSListAllOpportunity(request.get_json(force=True).get("data"))

from CRS.Agent.ListOpportunityDetail import FSListOpportunityDetail
@app.route('/CRS/Agent/ListOpportunityDetail',methods='POST')
def ListOpportunityDetail():
    return FSListOpportunityDetail(request.get_json(force=True).get("data"))

from CRS.Agent.CreateOpportunity import FSCreateOpportunity
@app.route('/CRS/Agent/CreateOpportunity',methods='POST')
def CreateOpportunity():
    return FSCreateOpportunity(request.get_json(force=True).get("data"))

from CRS.Agent.EditOpportunity import FSEditOpportunity
@app.route('/CRS/Agent/EditOpportunity',methods='POST')
def EditOpportunity():
    return FSEditOpportunity(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllMedia import FSListAllMedia
@app.route('/CRS/ExpDeveloper/ListAllMedia',methods='POST')
def ListAllMedia():
    return FSListAllMedia(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListMediaDetail import FSListMediaDetail
@app.route('/CRS/ExpDeveloper/ListMediaDetail',methods='POST')
def ListMediaDetail():
    return FSListMediaDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateMedia import FSCreateMedia
@app.route('/CRS/ExpDeveloper/CreateMedia',methods='POST')
def CreateMedia():
    return FSCreateMedia(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditMedia import FSEditMedia
@app.route('/CRS/ExpDeveloper/EditMedia',methods='POST')
def EditMedia():
    return FSEditMedia(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllCatalogue import FSListAllCatalogue
@app.route('/CRS/ExpDeveloper/ListAllCatalogue',methods='POST')
def ListAllCatalogue():
    return FSListAllCatalogue(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListCatalogueDetail import FSListCatalogueDetail
@app.route('/CRS/ExpDeveloper/ListCatalogueDetail',methods='POST')
def ListCatalogueDetail():
    return FSListCatalogueDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateCatalogue import FSCreateCatalogue
@app.route('/CRS/ExpDeveloper/CreateCatalogue',methods='POST')
def CreateCatalogue():
    return FSCreateCatalogue(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditCatalogue import FSEditCatalogue
@app.route('/CRS/ExpDeveloper/EditCatalogue',methods='POST')
def EditCatalogue():
    return FSEditCatalogue(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllTour import FSListAllTour
@app.route('/CRS/ExpDeveloper/ListAllTour',methods='POST')
def ListAllTour():
    return FSListAllTour(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListTourDetail import FSListTourDetail
@app.route('/CRS/ExpDeveloper/ListTourDetail',methods='POST')
def ListTourDetail():
    return FSListTourDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateTour import FSCreateTour
@app.route('/CRS/ExpDeveloper/CreateTour',methods='POST')
def CreateTour():
    return FSCreateTour(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditTour import FSEditTour
@app.route('/CRS/ExpDeveloper/EditTour',methods='POST')
def EditTour():
    return FSEditTour(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllPoll import FSListAllPoll
@app.route('/CRS/ExpDeveloper/ListAllPoll',methods='POST')
def ListAllPoll():
    return FSListAllPoll(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListPollDetail import FSListPollDetail
@app.route('/CRS/ExpDeveloper/ListPollDetail',methods='POST')
def ListPollDetail():
    return FSListPollDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreatePoll import FSCreatePoll
@app.route('/CRS/ExpDeveloper/CreatePoll',methods='POST')
def CreatePoll():
    return FSCreatePoll(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditPoll import FSEditPoll
@app.route('/CRS/ExpDeveloper/EditPoll',methods='POST')
def EditPoll():
    return FSEditPoll(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllSupplier import FSListAllSupplier
@app.route('/CRS/ExpDeveloper/ListAllSupplier',methods='POST')
def ListAllSupplier():
    return FSListAllSupplier(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListSupplierDetail import FSListSupplierDetail
@app.route('/CRS/ExpDeveloper/ListSupplierDetail',methods='POST')
def ListSupplierDetail():
    return FSListSupplierDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateSupplier import FSCreateSupplier
@app.route('/CRS/ExpDeveloper/CreateSupplier',methods='POST')
def CreateSupplier():
    return FSCreateSupplier(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditSupplier import FSEditSupplier
@app.route('/CRS/ExpDeveloper/EditSupplier',methods='POST')
def EditSupplier():
    return FSEditSupplier(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllExperience import FSListAllExperience
@app.route('/CRS/ExpDeveloper/ListAllExperience',methods='POST')
def ListAllExperience():
    return FSListAllExperience(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListExperienceDetail import FSListExperienceDetail
@app.route('/CRS/ExpDeveloper/ListExperienceDetail',methods='POST')
def ListExperienceDetail():
    return FSListExperienceDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateExperience import FSCreateExperience
@app.route('/CRS/ExpDeveloper/CreateExperience',methods='POST')
def CreateExperience():
    return FSCreateExperience(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditExperience import FSEditExperience
@app.route('/CRS/ExpDeveloper/EditExperience',methods='POST')
def EditExperience():
    return FSEditExperience(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllDestiny import FSListAllDestiny
@app.route('/CRS/ExpDeveloper/ListAllDestiny',methods='POST')
def ListAllDestiny():
    return FSListAllDestiny(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListDestinyDetail import FSListDestinyDetail
@app.route('/CRS/ExpDeveloper/ListDestinyDetail',methods='POST')
def ListDestinyDetail():
    return FSListDestinyDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateDestiny import FSCreateDestiny
@app.route('/CRS/ExpDeveloper/CreateDestiny',methods='POST')
def CreateDestiny():
    return FSCreateDestiny(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditDestiny import FSEditDestiny
@app.route('/CRS/ExpDeveloper/EditDestiny',methods='POST')
def EditDestiny():
    return FSEditDestiny(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllActivity import FSListAllActivity
@app.route('/CRS/ExpDeveloper/ListAllActivity',methods='POST')
def ListAllActivity():
    return FSListAllActivity(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListActivityDetail import FSListActivityDetail
@app.route('/CRS/ExpDeveloper/ListActivityDetail',methods='POST')
def ListActivityDetail():
    return FSListActivityDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateActivity import FSCreateActivity
@app.route('/CRS/ExpDeveloper/CreateActivity',methods='POST')
def CreateActivity():
    return FSCreateActivity(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditActivity import FSEditActivity
@app.route('/CRS/ExpDeveloper/EditActivity',methods='POST')
def EditActivity():
    return FSEditActivity(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllService import FSListAllService
@app.route('/CRS/ExpDeveloper/ListAllService',methods='POST')
def ListAllService():
    return FSListAllService(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListServiceDetail import FSListServiceDetail
@app.route('/CRS/ExpDeveloper/ListServiceDetail',methods='POST')
def ListServiceDetail():
    return FSListServiceDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateService import FSCreateService
@app.route('/CRS/ExpDeveloper/CreateService',methods='POST')
def CreateService():
    return FSCreateService(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditService import FSEditService
@app.route('/CRS/ExpDeveloper/EditService',methods='POST')
def EditService():
    return FSEditService(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListAllProduct import FSListAllProduct
@app.route('/CRS/ExpDeveloper/ListAllProduct',methods='POST')
def ListAllProduct():
    return FSListAllProduct(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.ListProductDetail import FSListProductDetail
@app.route('/CRS/ExpDeveloper/ListProductDetail',methods='POST')
def ListProductDetail():
    return FSListProductDetail(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.CreateProduct import FSCreateProduct
@app.route('/CRS/ExpDeveloper/CreateProduct',methods='POST')
def CreateProduct():
    return FSCreateProduct(request.get_json(force=True).get("data"))

from CRS.ExpDeveloper.EditProduct import FSEditProduct
@app.route('/CRS/ExpDeveloper/EditProduct',methods='POST')
def EditProduct():
    return FSEditProduct(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListAllOpportunity import FSListAllOpportunity
@app.route('/CRS/TrvExp/ListAllOpportunity',methods='POST')
def ListAllOpportunity():
    return FSListAllOpportunity(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListOpportunityDetail import FSListOpportunityDetail
@app.route('/CRS/TrvExp/ListOpportunityDetail',methods='POST')
def ListOpportunityDetail():
    return FSListOpportunityDetail(request.get_json(force=True).get("data"))

from CRS.TrvExp.CreateOpportunity import FSCreateOpportunity
@app.route('/CRS/TrvExp/CreateOpportunity',methods='POST')
def CreateOpportunity():
    return FSCreateOpportunity(request.get_json(force=True).get("data"))

from CRS.TrvExp.EditOpportunity import FSEditOpportunity
@app.route('/CRS/TrvExp/EditOpportunity',methods='POST')
def EditOpportunity():
    return FSEditOpportunity(request.get_json(force=True).get("data"))

from CRS.TrvExp.PromoteContact import FSPromoteContact
@app.route('/CRS/TrvExp/PromoteContact',methods='POST')
def PromoteContact():
    return FSPromoteContact(request.get_json(force=True).get("data"))

from CRS.TrvExp.PromoteQuote import FSPromoteQuote
@app.route('/CRS/TrvExp/PromoteQuote',methods='POST')
def PromoteQuote():
    return FSPromoteQuote(request.get_json(force=True).get("data"))

from CRS.TrvExp.PromoteOpportunity import FSPromoteOpportunity
@app.route('/CRS/TrvExp/PromoteOpportunity',methods='POST')
def PromoteOpportunity():
    return FSPromoteOpportunity(request.get_json(force=True).get("data"))

from CRS.TrvExp.PromoteSale import FSPromoteSale
@app.route('/CRS/TrvExp/PromoteSale',methods='POST')
def PromoteSale():
    return FSPromoteSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListAllSale import FSListAllSale
@app.route('/CRS/TrvExp/ListAllSale',methods='POST')
def ListAllSale():
    return FSListAllSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListSaleDetail import FSListSaleDetail
@app.route('/CRS/TrvExp/ListSaleDetail',methods='POST')
def ListSaleDetail():
    return FSListSaleDetail(request.get_json(force=True).get("data"))

from CRS.TrvExp.CreateSale import FSCreateSale
@app.route('/CRS/TrvExp/CreateSale',methods='POST')
def CreateSale():
    return FSCreateSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.EditSale import FSEditSale
@app.route('/CRS/TrvExp/EditSale',methods='POST')
def EditSale():
    return FSEditSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListAllSale import FSListAllSale
@app.route('/CRS/TrvExp/ListAllSale',methods='POST')
def ListAllSale():
    return FSListAllSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListSaleDetail import FSListSaleDetail
@app.route('/CRS/TrvExp/ListSaleDetail',methods='POST')
def ListSaleDetail():
    return FSListSaleDetail(request.get_json(force=True).get("data"))

from CRS.TrvExp.CreateSale import FSCreateSale
@app.route('/CRS/TrvExp/CreateSale',methods='POST')
def CreateSale():
    return FSCreateSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.EditSale import FSEditSale
@app.route('/CRS/TrvExp/EditSale',methods='POST')
def EditSale():
    return FSEditSale(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListAllProblem import FSListAllProblem
@app.route('/CRS/TrvExp/ListAllProblem',methods='POST')
def ListAllProblem():
    return FSListAllProblem(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListProblemDetail import FSListProblemDetail
@app.route('/CRS/TrvExp/ListProblemDetail',methods='POST')
def ListProblemDetail():
    return FSListProblemDetail(request.get_json(force=True).get("data"))

from CRS.TrvExp.CreateProblem import FSCreateProblem
@app.route('/CRS/TrvExp/CreateProblem',methods='POST')
def CreateProblem():
    return FSCreateProblem(request.get_json(force=True).get("data"))

from CRS.TrvExp.EditProblem import FSEditProblem
@app.route('/CRS/TrvExp/EditProblem',methods='POST')
def EditProblem():
    return FSEditProblem(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListAllTour import FSListAllTour
@app.route('/CRS/TrvExp/ListAllTour',methods='POST')
def ListAllTour():
    return FSListAllTour(request.get_json(force=True).get("data"))

from CRS.TrvExp.ListTourDetail import FSListTourDetail
@app.route('/CRS/TrvExp/ListTourDetail',methods='POST')
def ListTourDetail():
    return FSListTourDetail(request.get_json(force=True).get("data"))

from CRS.TrvExp.CreateTour import FSCreateTour
@app.route('/CRS/TrvExp/CreateTour',methods='POST')
def CreateTour():
    return FSCreateTour(request.get_json(force=True).get("data"))

from CRS.TrvExp.EditTour import FSEditTour
@app.route('/CRS/TrvExp/EditTour',methods='POST')
def EditTour():
    return FSEditTour(request.get_json(force=True).get("data"))

from CRS.Admin.DeleteSupplier import FSDeleteSupplier
@app.route('/CRS/Admin/DeleteSupplier',methods='POST')
def DeleteSupplier():
    return FSDeleteSupplier(request.get_json(force=True).get("data"))

from CRS.Admin.DeleteTour import FSDeleteTour
@app.route('/CRS/Admin/DeleteTour',methods='POST')
def DeleteTour():
    return FSDeleteTour(request.get_json(force=True).get("data"))

from CRS.Admin.DeletePoll import FSDeletePoll
@app.route('/CRS/Admin/DeletePoll',methods='POST')
def DeletePoll():
    return FSDeletePoll(request.get_json(force=True).get("data"))

from CRS.Admin.DeleteReport import FSDeleteReport
@app.route('/CRS/Admin/DeleteReport',methods='POST')
def DeleteReport():
    return FSDeleteReport(request.get_json(force=True).get("data"))

from CRS.Admin.DeleteUser import FSDeleteUser
@app.route('/CRS/Admin/DeleteUser',methods='POST')
def DeleteUser():
    return FSDeleteUser(request.get_json(force=True).get("data"))

from CRS.Admin.ListAllUser import FSListAllUser
@app.route('/CRS/Admin/ListAllUser',methods='POST')
def ListAllUser():
    return FSListAllUser(request.get_json(force=True).get("data"))

from CRS.Admin.ListUserDetail import FSListUserDetail
@app.route('/CRS/Admin/ListUserDetail',methods='POST')
def ListUserDetail():
    return FSListUserDetail(request.get_json(force=True).get("data"))

from CRS.Admin.CreateUser import FSCreateUser
@app.route('/CRS/Admin/CreateUser',methods='POST')
def CreateUser():
    return FSCreateUser(request.get_json(force=True).get("data"))

from CRS.Admin.EditUser import FSEditUser
@app.route('/CRS/Admin/EditUser',methods='POST')
def EditUser():
    return FSEditUser(request.get_json(force=True).get("data"))

from CRS.Admin.ListAllReport import FSListAllReport
@app.route('/CRS/Admin/ListAllReport',methods='POST')
def ListAllReport():
    return FSListAllReport(request.get_json(force=True).get("data"))

from CRS.Admin.ListReportDetail import FSListReportDetail
@app.route('/CRS/Admin/ListReportDetail',methods='POST')
def ListReportDetail():
    return FSListReportDetail(request.get_json(force=True).get("data"))

from CRS.Admin.CreateReport import FSCreateReport
@app.route('/CRS/Admin/CreateReport',methods='POST')
def CreateReport():
    return FSCreateReport(request.get_json(force=True).get("data"))

from CRS.Admin.EditReport import FSEditReport
@app.route('/CRS/Admin/EditReport',methods='POST')
def EditReport():
    return FSEditReport(request.get_json(force=True).get("data"))

from CRS.System.ValidatePoll import FSValidatePoll
@app.route('/CRS/System/ValidatePoll',methods='POST')
def ValidatePoll():
    return FSValidatePoll(request.get_json(force=True).get("data"))

from CRS.System.LogPoll import FSLogPoll
@app.route('/CRS/System/LogPoll',methods='POST')
def LogPoll():
    return FSLogPoll(request.get_json(force=True).get("data"))

from CRS.System.ValidateUser import FSValidateUser
@app.route('/CRS/System/ValidateUser',methods='POST')
def ValidateUser():
    return FSValidateUser(request.get_json(force=True).get("data"))

from CRS.System.LogUser import FSLogUser
@app.route('/CRS/System/LogUser',methods='POST')
def LogUser():
    return FSLogUser(request.get_json(force=True).get("data"))

from CRS.System.ValidateOpportunity import FSValidateOpportunity
@app.route('/CRS/System/ValidateOpportunity',methods='POST')
def ValidateOpportunity():
    return FSValidateOpportunity(request.get_json(force=True).get("data"))

from CRS.System.LogOpportunity import FSLogOpportunity
@app.route('/CRS/System/LogOpportunity',methods='POST')
def LogOpportunity():
    return FSLogOpportunity(request.get_json(force=True).get("data"))

from CRS.System.ValidateQuote import FSValidateQuote
@app.route('/CRS/System/ValidateQuote',methods='POST')
def ValidateQuote():
    return FSValidateQuote(request.get_json(force=True).get("data"))

from CRS.System.LogQuote import FSLogQuote
@app.route('/CRS/System/LogQuote',methods='POST')
def LogQuote():
    return FSLogQuote(request.get_json(force=True).get("data"))

from CRS.System.ValidateSale import FSValidateSale
@app.route('/CRS/System/ValidateSale',methods='POST')
def ValidateSale():
    return FSValidateSale(request.get_json(force=True).get("data"))

from CRS.System.LogSale import FSLogSale
@app.route('/CRS/System/LogSale',methods='POST')
def LogSale():
    return FSLogSale(request.get_json(force=True).get("data"))

from CRS.System.ValidatePay import FSValidatePay
@app.route('/CRS/System/ValidatePay',methods='POST')
def ValidatePay():
    return FSValidatePay(request.get_json(force=True).get("data"))

from CRS.System.LogPay import FSLogPay
@app.route('/CRS/System/LogPay',methods='POST')
def LogPay():
    return FSLogPay(request.get_json(force=True).get("data"))

from CRS.System.ValidateConsumption import FSValidateConsumption
@app.route('/CRS/System/ValidateConsumption',methods='POST')
def ValidateConsumption():
    return FSValidateConsumption(request.get_json(force=True).get("data"))

from CRS.System.LogConsumption import FSLogConsumption
@app.route('/CRS/System/LogConsumption',methods='POST')
def LogConsumption():
    return FSLogConsumption(request.get_json(force=True).get("data"))

from CRS.System.ValidateContact import FSValidateContact
@app.route('/CRS/System/ValidateContact',methods='POST')
def ValidateContact():
    return FSValidateContact(request.get_json(force=True).get("data"))

from CRS.System.LogContact import FSLogContact
@app.route('/CRS/System/LogContact',methods='POST')
def LogContact():
    return FSLogContact(request.get_json(force=True).get("data"))

from CRS.System.ValidateProspect import FSValidateProspect
@app.route('/CRS/System/ValidateProspect',methods='POST')
def ValidateProspect():
    return FSValidateProspect(request.get_json(force=True).get("data"))

from CRS.System.LogProspect import FSLogProspect
@app.route('/CRS/System/LogProspect',methods='POST')
def LogProspect():
    return FSLogProspect(request.get_json(force=True).get("data"))

from CRS.System.ValidateClient import FSValidateClient
@app.route('/CRS/System/ValidateClient',methods='POST')
def ValidateClient():
    return FSValidateClient(request.get_json(force=True).get("data"))

from CRS.System.LogClient import FSLogClient
@app.route('/CRS/System/LogClient',methods='POST')
def LogClient():
    return FSLogClient(request.get_json(force=True).get("data"))

from CRS.System.ValidateTour import FSValidateTour
@app.route('/CRS/System/ValidateTour',methods='POST')
def ValidateTour():
    return FSValidateTour(request.get_json(force=True).get("data"))

from CRS.System.LogTour import FSLogTour
@app.route('/CRS/System/LogTour',methods='POST')
def LogTour():
    return FSLogTour(request.get_json(force=True).get("data"))

from CRS.System.ValidateExperience import FSValidateExperience
@app.route('/CRS/System/ValidateExperience',methods='POST')
def ValidateExperience():
    return FSValidateExperience(request.get_json(force=True).get("data"))

from CRS.System.LogExperience import FSLogExperience
@app.route('/CRS/System/LogExperience',methods='POST')
def LogExperience():
    return FSLogExperience(request.get_json(force=True).get("data"))

from CRS.System.ValidateDestiny import FSValidateDestiny
@app.route('/CRS/System/ValidateDestiny',methods='POST')
def ValidateDestiny():
    return FSValidateDestiny(request.get_json(force=True).get("data"))

from CRS.System.LogDestiny import FSLogDestiny
@app.route('/CRS/System/LogDestiny',methods='POST')
def LogDestiny():
    return FSLogDestiny(request.get_json(force=True).get("data"))

from CRS.System.ValidateActivity import FSValidateActivity
@app.route('/CRS/System/ValidateActivity',methods='POST')
def ValidateActivity():
    return FSValidateActivity(request.get_json(force=True).get("data"))

from CRS.System.LogActivity import FSLogActivity
@app.route('/CRS/System/LogActivity',methods='POST')
def LogActivity():
    return FSLogActivity(request.get_json(force=True).get("data"))

from CRS.System.ValidateService import FSValidateService
@app.route('/CRS/System/ValidateService',methods='POST')
def ValidateService():
    return FSValidateService(request.get_json(force=True).get("data"))

from CRS.System.LogService import FSLogService
@app.route('/CRS/System/LogService',methods='POST')
def LogService():
    return FSLogService(request.get_json(force=True).get("data"))

from CRS.System.ValidateProduct import FSValidateProduct
@app.route('/CRS/System/ValidateProduct',methods='POST')
def ValidateProduct():
    return FSValidateProduct(request.get_json(force=True).get("data"))

from CRS.System.LogProduct import FSLogProduct
@app.route('/CRS/System/LogProduct',methods='POST')
def LogProduct():
    return FSLogProduct(request.get_json(force=True).get("data"))

from CRS.System.ValidateProblem import FSValidateProblem
@app.route('/CRS/System/ValidateProblem',methods='POST')
def ValidateProblem():
    return FSValidateProblem(request.get_json(force=True).get("data"))

from CRS.System.LogProblem import FSLogProblem
@app.route('/CRS/System/LogProblem',methods='POST')
def LogProblem():
    return FSLogProblem(request.get_json(force=True).get("data"))

from CRS.System.SendSms import FSSendSms
@app.route('/CRS/System/SendSms',methods='POST')
def SendSms():
    return FSSendSms(request.get_json(force=True).get("data"))

from CRS.System.LogSms import FSLogSms
@app.route('/CRS/System/LogSms',methods='POST')
def LogSms():
    return FSLogSms(request.get_json(force=True).get("data"))

from CRS.System.SendEmail import FSSendEmail
@app.route('/CRS/System/SendEmail',methods='POST')
def SendEmail():
    return FSSendEmail(request.get_json(force=True).get("data"))

from CRS.System.LogEmail import FSLogEmail
@app.route('/CRS/System/LogEmail',methods='POST')
def LogEmail():
    return FSLogEmail(request.get_json(force=True).get("data"))

from CRS.System.SendAlert import FSSendAlert
@app.route('/CRS/System/SendAlert',methods='POST')
def SendAlert():
    return FSSendAlert(request.get_json(force=True).get("data"))

from CRS.System.LogAlert import FSLogAlert
@app.route('/CRS/System/LogAlert',methods='POST')
def LogAlert():
    return FSLogAlert(request.get_json(force=True).get("data"))

from CRS.System.SendNotification import FSSendNotification
@app.route('/CRS/System/SendNotification',methods='POST')
def SendNotification():
    return FSSendNotification(request.get_json(force=True).get("data"))

from CRS.System.LogNotification import FSLogNotification
@app.route('/CRS/System/LogNotification',methods='POST')
def LogNotification():
    return FSLogNotification(request.get_json(force=True).get("data"))

from CRS.System.LoadTemplate import FSLoadTemplate
@app.route('/CRS/System/LoadTemplate',methods='POST')
def LoadTemplate():
    return FSLoadTemplate(request.get_json(force=True).get("data"))

from CRS.System.BlockUser import FSBlockUser
@app.route('/CRS/System/BlockUser',methods='POST')
def BlockUser():
    return FSBlockUser(request.get_json(force=True).get("data"))

from CRS.System.LogBlocked import FSLogBlocked
@app.route('/CRS/System/LogBlocked',methods='POST')
def LogBlocked():
    return FSLogBlocked(request.get_json(force=True).get("data"))