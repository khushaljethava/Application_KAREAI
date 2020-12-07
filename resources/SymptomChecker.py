from run import db
from flask_restful import Resource
from model.SymptomChecker import SymptomCheckerModel
from model.SymptomCheckerAnswer import SymptomCheckerAnswerModel
from flask import jsonify
from flask_jwt_extended import jwt_required


class SymptomChecker(Resource):

    @jwt_required
    def get(self, SC_question_id):
        if SymptomCheckerModel.find_by_Question_id(SC_question_id):
            options = SymptomCheckerAnswerModel.find_by_answer_id(SC_question_id)
            symptom_checker = SymptomCheckerModel.find_by_Question_id(SC_question_id)

            payload = {
            "Question": symptom_checker.json(),
            "Answer": options.json()

            }

            return jsonify(payload)
        else:
            return {
            "message":"Error"
            }
