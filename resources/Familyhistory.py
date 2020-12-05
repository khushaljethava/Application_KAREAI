from run import db
from flask_restful import Resource, reqparse
from model.Familyhistory import FamilyHistoryModel
from flask_jwt_extended import jwt_required


class FamilyHistory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Member', help=' Member cannot be blank', required=True)
    parser.add_argument('Alcoholism', help='Alcoholism cannot be blank', required=True)
    parser.add_argument('Allergies', help='Allergies cannot be blank', required=True)
    parser.add_argument('Anesthesia', help='Anesthesia cannot be blank', required=True)
    parser.add_argument('Anxiety', help='Anxiety cannot be blank', required=True)
    parser.add_argument('Arthritis', help='Arthritis cannot be blank', required=True)
    parser.add_argument('Asthma', help='Asthma cannot be blank', required=True)
    parser.add_argument('ADHD', help='ADHD cannot be blank', required=True)
    parser.add_argument('Birth_Defects', help='Birth_Defects cannot be blank', required=True)
    parser.add_argument('Blood_Problem', help=' Blood_Problem cannot be blank', required=True)
    parser.add_argument('Bone_Joint_Problems', help='Bone_Joint_Problems cannot be blank', required=True)
    parser.add_argument('Breast_Disease', help='Breast_Disease cannot be blank', required=True)
    parser.add_argument('Cancer', help='Cancer cannot be blank', required=True)
    parser.add_argument('Chicken_Pox', help='Chicken_Pox cannot be blank', required=True)
    parser.add_argument('Colitis', help='Colitis cannot be blank', required=True)
    parser.add_argument('Depression', help='Depression cannot be blank', required=True)
    parser.add_argument('Diabetes', help='Diabetes cannot be blank', required=True)
    parser.add_argument('ENT_Problems', help='ENT_Problems cannot be blank', required=True)
    parser.add_argument('Eating_Disorders', help=' Eating_Disorders cannot be blank', required=True)
    parser.add_argument('Eczema', help='Eczema cannot be blank', required=True)
    parser.add_argument('Epilepsy', help='Epilepsy cannot be blank', required=True)
    parser.add_argument('Fertility', help='Fertility cannot be blank', required=True)
    parser.add_argument('Gallbladder', help='Gallbladder cannot be blank', required=True)
    parser.add_argument('Gynecology', help='Gynecology cannot be blank', required=True)
    parser.add_argument('Fever', help='Fever cannot be blank', required=True)
    parser.add_argument('Headaches', help='Headaches cannot be blank', required=True)
    parser.add_argument('Heart_Problems', help='Heart_Problems cannot be blank', required=True)
    parser.add_argument('Heart_Attack_Over_60', help='Heart_Attack_Over_60 cannot be blank', required=True)
    parser.add_argument('Heart_Attack_Under_60', help='Heart_Attack_Under_60 cannot be blank', required=True)
    parser.add_argument('Heart_Murmur', help='Heart_Murmur cannot be blank', required=True)
    parser.add_argument('Hepatitis', help='Hepatitis cannot be blank', required=True)
    parser.add_argument('High_Blood_Pressure', help='High_Blood_Pressure cannot be blank', required=True)
    parser.add_argument('High_Cholestorol', help='High_Cholestorol cannot be blank', required=True)

    @jwt_required
    def get(self,user_id,Member):
        familyhistory = FamilyHistoryModel.find_by_id(user_id)
        familyhistory_member = FamilyHistoryModel.find_by_member(Member)
        if familyhistory_member:
            return familyhistory_member.json()
        return {'message': 'Item not found' }, 404

    @jwt_required
    def post(self, user_id, Member):
        if FamilyHistoryModel.find_by_id(user_id) and FamilyHistoryModel.find_by_member(Member):
            return {'message': 'Item already exists'}
        else:

            data = FamilyHistory.parser.parse_args()

            familyhistory = FamilyHistoryModel(user_id, **data)

            try:

                familyhistory.save_to_db()

            except:

                return {'message': 'An Error occurred in Family History'}

            return familyhistory.json(), 201

    @jwt_required
    def put(self,user_id, Member):
        data = FamilyHistory.parser.parse_args()
        familyhistory = FamilyHistoryModel.find_by_id(user_id)

        if familyhistory:
            familyhistory.Member = data['Member']
            familyhistory.Alcoholism = data['Alcoholism']
            familyhistory.Allergies = data['Allergies']
            familyhistory.Anesthesia = data['Anesthesia']
            familyhistory.Anxiety = data['Anxiety']
            familyhistory.Arthritis = data['Arthritis']
            familyhistory.Asthma = data['Asthma']
            familyhistory.ADHD = data['ADHD']
            familyhistory.Birth_Defects = data['Birth_Defects']
            familyhistory.Blood_Problem = data['Blood_Problem']
            familyhistory.Bone_Joint_Problems = data['Bone_Joint_Problems']
            familyhistory.Breast_Disease = data['Breast_Disease']
            familyhistory.Cancer = data['Cancer']
            familyhistory.Chicken_Pox = data['Chicken_Pox']
            familyhistory.Colitis = data['Colitis']
            familyhistory.Depression = data['Depression']
            familyhistory.Diabetes = data['Diabetes']
            familyhistory.ENT_Problems = data['ENT_Problems']
            familyhistory.Eating_Disorders = data['Eating_Disorders']
            familyhistory.Eczema = data['Eczema']
            familyhistory.Epilepsy = data['Epilepsy']
            familyhistory.Fertility = data['Fertility']
            familyhistory.Gallbladder = data['Gallbladder']
            familyhistory.Gynecology = data['Gynecology']
            familyhistory.Fever = data['Fever']
            familyhistory.Headaches = data['Headaches']
            familyhistory.Heart_Problems = data['Heart_Problems']
            familyhistory.Heart_Attack_Over_60 = data['Heart_Attack_Over_60']
            familyhistory.Heart_Attack_Under_60 = data['Heart_Attack_Under_60']
            familyhistory.Heart_Murmur = data['Heart_Murmur']
            familyhistory.Hepatitis = data['Hepatitis']
            familyhistory.High_Blood_Pressure = data['High_Blood_Pressure']
            familyhistory.High_Cholestorol = data['High_Cholestorol']

        else:

            familyhistory = FamilyHistoryModel(user_id, **data)

        familyhistory.save_to_db()

        return familyhistory.json(), 201

    @jwt_required
    def delete(self, user_id, Member):
        familyhistory = FamilyHistoryModel.find_by_id(user_id)
        if familyhistory:
            familyhistory.delete_from_db()
            return {'message': 'Item deleted successfully.'}
        return {'message': 'Item not found'}
