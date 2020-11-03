from run import db
from flask_restful import Resource, reqparse
from model.Preexistingcondition import PreConditionModel
from flask_jwt_extended import jwt_required


class PreexistingCondition(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Race', help=' Race cannot be blank', required=True)
    parser.add_argument('Smoking', help='Smoking cannot be blank', required=True)
    parser.add_argument('Alcohol', help='Alcohol cannot be blank', required=True)
    parser.add_argument('Diabetes', help='Diabetes cannot be blank', required=True)
    parser.add_argument('Hear', help='Hear cannot be blank', required=True)
    parser.add_argument('Blood_Pressure', help='Blood_Pressure cannot be blank', required=True)
    parser.add_argument('Chest_Pain', help='Chest_Pain cannot be blank', required=True)
    parser.add_argument('Stroke', help='Stroke cannot be blank', required=True)
    parser.add_argument('Kidney', help='Kidney cannot be blank', required=True)
    parser.add_argument('Blood_Clot', help='Blood_Clot cannot be blank', required=True)
    parser.add_argument('Metal_implants', help='Metal_implants cannot be blank', required=True)
    parser.add_argument('Asthma', help='Asthma cannot be blank', required=True)
    parser.add_argument('Cancer', help='Cancer cannot be blank', required=True)
    parser.add_argument('Difficulty_Swallowing', help='Difficulty_Swallowing cannot be blank', required=True)
    parser.add_argument('Vascular_Problems', help='Vascular_Problems cannot be blank', required=True)
    parser.add_argument('Peripheral_Neuropathy', help='Peripheral_Neuropathy cannot be blank', required=True)
    parser.add_argument('Weightloss', help='Weightloss cannot be blank', required=True)
    parser.add_argument('Double_Vision', help='Double_Vision cannot be blank', required=True)
    parser.add_argument('Night_Sweats', help='Night_Sweats cannot be blank', required=True)
    parser.add_argument('Night_Pain', help='Night_Pain cannot be blank', required=True)
    parser.add_argument('Neurologic_Condition', help='Neurologic_Condition cannot be blank', required=True)
    parser.add_argument('Skin_Disease', help='Skin_Disease cannot be blank', required=True)
    parser.add_argument('Spinal_Cord_Injury', help='Spinal_Cord_Injury cannot be blank', required=True)
    parser.add_argument('Degenerative_Joint_Disease', help='Degenerative_Joint_Disease cannot be blank', required=True)
    parser.add_argument('Sexual_Dysfunction', help='Sexual_Dysfunction cannot be blank', required=True)
    parser.add_argument('Bladder', help='Bladder cannot be blank', required=True)
    parser.add_argument('Groin_Numbness', help='Groin_Numbness cannot be blank', required=True)
    parser.add_argument('Arthritis', help='Arthritis cannot be blank', required=True)
    parser.add_argument('Osteoporosis', help='Osteoporosis cannot be blank', required=True)
    parser.add_argument('Phsychological_Problems', help='Phsychological_Problems cannot be blank', required=True)
    parser.add_argument('Seizures', help='Seizures cannot be blank', required=True)
    parser.add_argument('Dizziness', help='Dizziness cannot be blank', required=True)

    parser.add_argument('Ringing_in_Ears', help='Ringing_in_Ears cannot be blank', required=True)
    parser.add_argument('Allergy_to_Latex', help='Allergy_to_Latex cannot be blank', required=True)
    parser.add_argument('Head_Injury', help='Head_Injury cannot be blank', required=True)
    parser.add_argument('Obesity', help='Obesity cannot be blank', required=True)
    parser.add_argument('Chronic_Pain', help='Chronic_Pain cannot be blank', required=True)
    parser.add_argument('Fractures', help='Fractures cannot be blank', required=True)
    parser.add_argument('Infection_Dissease', help='Infection_Dissease cannot be blank', required=True)
    parser.add_argument('Fever', help='Fever cannot be blank', required=True)
    parser.add_argument('Lower_Extremety', help='Lower_Extremety cannot be blank', required=True)
    parser.add_argument('Nausea', help='Nausea cannot be blank', required=True)


    @jwt_required
    def get(self, user_id):
        preexistingcondition = PreConditionModel.find_by_id(user_id)
        if  preexistingcondition:
            return preexistingcondition.json()
        return {'message': 'Item not found'}, 404
    @jwt_required
    def post(self, user_id):
        if PreConditionModel.find_by_id(user_id):
            return {'message': 'Item already exists'}

        data = PreexistingCondition.parser.parse_args()
        preexistingcondition = PreConditionModel(user_id, **data)

        try:

            preexistingcondition.save_to_db()

        except:

            return {'message': 'An error occurred' }
        return preexistingcondition.json(), 201

    @jwt_required
    def delete(self,user_id):
        preexistingcondition = PreConditionModel.find_by_id(user_id)
        if preexistingcondition:
            preexistingcondition.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': ' Item not Found'}

    @jwt_required
    def put(self, user_id):
        data = PreexistingCondition.parser.parse_args()

        preexistingcondition = PreConditionModel.find_by_id(user_id)
        if preexistingcondition:
                preexistingcondition.Race = data['Race']
                preexistingcondition.Smoking = data['Smoking']
                preexistingcondition.Alcohol = data['Alcohol']
                preexistingcondition.Diabetes = data['Diabetes']
                preexistingcondition.Hear = data['Hear']
                preexistingcondition.Blood_Pressure = data['Blood_Pressure']
                preexistingcondition.Chest_Pain = data['Chest_Pain']
                preexistingcondition.Stroke = data['Stroke']
                preexistingcondition.Kidney  = data['Kidney']
                preexistingcondition.Blood_Clot = data['Blood_Clot']
                preexistingcondition.Metal_implants = data['Metal_implants']
                preexistingcondition.Asthma = data['Asthma']
                preexistingcondition.Cancer = data['Cancer']
                preexistingcondition.Difficulty_Swallowing = data['Difficulty_Swallowing']
                preexistingcondition.Vascular_Problems = data['Vascular_Problems']
                preexistingcondition.Peripheral_Neuropathy = data['Peripheral_Neuropathy']
                preexistingcondition.Weightloss = data['Weightloss']
                preexistingcondition.Double_Vision = data['Double_Vision']
                preexistingcondition.Night_Sweats = data['Night_Sweats']
                preexistingcondition.Night_Pain = data['Night_Pain']
                preexistingcondition.Neurologic_Condition = data['Neurologic_Condition']
                preexistingcondition.Skin_Disease = data['Skin_Disease']
                preexistingcondition.Spinal_Cord_Injury = data['Spinal_Cord_Injury']
                preexistingcondition.Degenerative_Joint_Disease = data['Degenerative_Joint_Disease']
                preexistingcondition.Sexual_Dysfunction = data['Sexual_Dysfunction']
                preexistingcondition.Bladder = data['Bladder']
                preexistingcondition.Groin_Numbness = data['Groin_Numbness']
                preexistingcondition.Arthritis = data['Arthritis']
                preexistingcondition.Osteoporosis = data['Osteoporosis']
                preexistingcondition.Phsychological_Problems = data['Phsychological_Problems']
                preexistingcondition.Seizures = data['Seizures']
                preexistingcondition.Dizziness = data['Dizziness']
                preexistingcondition.Ringing_in_Ears = data['Ringing_in_Ears']
                preexistingcondition.Allergy_to_Latex   = data['Allergy_to_Latex']
                preexistingcondition.Head_Injury = data['Head_Injury']
                preexistingcondition.Obesity = data['Obesity']
                preexistingcondition.Chronic_Pain = data['Chronic_Pain']
                preexistingcondition.Fractures  = data['Fractures']
                preexistingcondition.Infection_Dissease  = data['Infection_Dissease']
                preexistingcondition.Fever = data['Fever']
                preexistingcondition.Lower_Extremety = data['Lower_Extremety']
                preexistingcondition.Nausea = data['Nausea']

        else:
            preexistingcondition = PreConditionModel(user_id, **data)
        preexistingcondition.save_to_db()

        return preexistingcondition.json(),201
