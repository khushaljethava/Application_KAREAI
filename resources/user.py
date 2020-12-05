from flask_restful import Resource, reqparse
from model.user import UserModel, RevokedTokenModel


from flask_jwt_extended import (
        create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
        get_jwt_identity, get_raw_jwt
)

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('username', help='Username cannot be blank', required=True)
reg_parser.add_argument('fullname')
reg_parser.add_argument('email', help='Email cannot be blank', required=True)
reg_parser.add_argument('mobile', help='Mobile cannot be blank', required=True)
reg_parser.add_argument('gander')
reg_parser.add_argument('age')


log_parser = reqparse.RequestParser()
log_parser.add_argument('mobile', help='Mobile cannot be blank' , required=True)

class UserRegistration(Resource):

    def post(self):
        data = reg_parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        if UserModel.find_by_mobile(data['mobile']):
            return {'message': 'Mobile Number {} already exists'.format(data['mobile'])}
        if UserModel.find_by_email(data['email']):
            return {'message': 'Email {} already exists'.format(data['email'])}


        new_user = UserModel(
        username=data['username'],
        fullname=data['fullname'],
        email=data['email'],
        mobile=data['mobile'],
        gander=data['gander'],
        age=data['age'])

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
            'message': 'User {} was created successfully'.format(data['username']),
             'access_token': access_token,
            'refresh_token': refresh_token
            }
        except:
            return {'message':'Something went wrong'}, 500

class UserLogin(Resource):

    def post(self):
        data = log_parser.parse_args()
        current_user = UserModel.find_by_mobile(data['mobile'])
        if not current_user:
            return {'message': 'User {} doess\'t exist'.format(data['mobile'])}

        if UserModel.find_by_mobile(data['mobile']):
            access_token = create_access_token(identity = data['mobile'])
            refresh_token = create_refresh_token(identity = data['mobile'])
            return {'message': 'Logged in as {}'.format(data['mobile']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong Credentialscd '}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message':'Access token has been revoked'}
        except:
            return {'message':'Something went wrong'}, 500


class UserLogoutRefersh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message':'Something went wrong'}, 500


class TokenRefersh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}



class SecretResources(Resource):
    @jwt_required
    def get(self):
        return {'answers':45}
