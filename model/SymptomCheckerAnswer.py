from run import db

class SymptomCheckerAnswerModel(db.Model):
    __tablename__ = 'SymptomCheckerAnswer'

    Option_id = db.Column(db.Integer, primary_key=True)
    Option_1 = db.Column(db.String(120))
    Option_2 = db.Column(db.String(120))
    Option_3 = db.Column(db.String(120))
    Option_4 = db.Column(db.String(120))
    Option_5 = db.Column(db.String(120))
    Option_6 = db.Column(db.String(120))
    Option_7 = db.Column(db.String(120))
    Option_8 = db.Column(db.String(120))
    Option_9 = db.Column(db.String(120))
    Option_10 = db.Column(db.String(120))


    def json(self):
        return{
        'Option_1': self.Option_1,
        'Option_2': self.Option_2,
        'Option_3': self.Option_3,
        'Option_4': self.Option_4,
        'Option_5': self.Option_5,
        'Option_6': self.Option_6,
        'Option_7': self.Option_7,
        'Option_8': self.Option_8,
        'Option_9': self.Option_9,
        'Option_10': self.Option_10,
        }



    @classmethod
    def find_by_answer_id(cls, Option_id):
        return cls.query.filter_by(Option_id=Option_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
