from run import db
from flask_restful import Resource
from model.SymptomChecker import SymptomCheckerModel
from model.SymptomCheckerAnswer import SymptomCheckerAnswerModel
from flask import jsonify

class SymptomChecker(Resource):

    @jwt_required
    def get(self, question_id):
        if SymptomCheckerModel.find_by_Question_id(question_id):
            options = SymptomCheckerAnswerModel.find_by_answer_id(question_id)
            symptom_checker = SymptomCheckerModel.find_by_Question_id(question_id)

            payload = {
            "Question": symptom_checker.json(),
            "Answer": options.json()

            }

            return jsonify(payload)
        else:
            return {
            "message":"Error"
            }
