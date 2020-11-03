from run import db
class SymptomCheckerModel(db.Model):
    __tablename__ = 'SymptomChecker'

    question_id = db.Column(db.Integer, primary_key=True)
    questions = db.Column(db.String(120))



    def __init__(self, question_id, questions):
        self.question_id = question_id
        self.questions = questions

    def json(self):
        return{
        'Questions': self.questions
        }


    @classmethod
    def find_by_Question_id(cls, question_id):
        return cls.query.filter_by(question_id=question_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
