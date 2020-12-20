from flask import Flask
from flask_restful import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  except RuntimeError as e:
    print(e)

app = Flask(__name__)
api = Api(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

UPLOAD_FOLDER = '/static/uploads/'


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Kareai:Devil@54645@localhost/newdata'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:54645@localhost/karenew'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Kareai123@localhost/KAREAIDB'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'D3evil4'
app.config['JWT_SECRET_KEY'] = 'J3evil4'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh']

db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.before_first_request
def create_table():
    db.create_all()

from resources.user import UserRegistration, UserLogin, UserLogoutAccess, UserLogoutRefersh, TokenRefersh
from resources.Preexistingcondition import PreexistingCondition
from resources.Familyhistory import FamilyHistory
from resources.LabReportUpload import LabReportUpload
from resources.Labreport import LabReport
from resources.Retina import RetinaUpload
from model.user import RevokedTokenModel
from resources.ReferenceRange import ReferenceRange
from resources.SymptomChecker import SymptomChecker
from resources.Blood_Glucose import BloodGlucose
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefersh, '/logout/refresh')
api.add_resource(TokenRefersh, '/token/refresh')
#api.add_resource(SecretResources, '/secret')
api.add_resource(PreexistingCondition,'/preexisting/<int:PC_user_id>') # user_id
api.add_resource(FamilyHistory,'/familyhistory/<int:FH_user_id>/<string:FH_Member>') #
api.add_resource(LabReport, '/labreport/<int:LR_user_id>')
api.add_resource(LabReportUpload, '/labreportupload/<int:LR_user_id>')
api.add_resource(RetinaUpload, '/retinaupload/<int:RU_user_id>')
api.add_resource(ReferenceRange,'/reference/<int:user_id>')
api.add_resource(SymptomChecker, '/symptomcheck/<int:UI_user_id>')
api.add_resource(BloodGlucose, '/bloodglucose/<int:BG_user_id>')


if __name__ == '__main__':
    app.run()
