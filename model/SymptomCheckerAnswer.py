from run import db

class SymptomCheckerAnswerModel(db.Model):
    __tablename__ = 'SymptomCheckerAnswer'

    SCA_Option_id = db.Column(db.Integer, primary_key=True)
    SCA_Option_1 = db.Column(db.String(120))
    SCA_Option_2 = db.Column(db.String(120))
    SCA_Option_3 = db.Column(db.String(120))
    SCA_Option_4 = db.Column(db.String(120))
    SCA_Option_5 = db.Column(db.String(120))
    SCA_Option_6 = db.Column(db.String(120))
    SCA_Option_7 = db.Column(db.String(120))
    SCA_Option_8 = db.Column(db.String(120))
    SCA_Option_9 = db.Column(db.String(120))
    SCA_Option_10 = db.Column(db.String(120))


    def json(self):
        return{
        'SCA_Option_1': self.SCA_Option_1,
        'SCA_Option_2': self.SCA_Option_2,
        'SCA_Option_3': self.SCA_Option_3,
        'SCA_Option_4': self.SCA_Option_4,
        'SCA_Option_5': self.SCA_Option_5,
        'SCA_Option_6': self.SCA_Option_6,
        'SCA_Option_7': self.SCA_Option_7,
        'SCA_Option_8': self.SCA_Option_8,
        'SCA_Option_9': self.SCA_Option_9,
        'SCA_Option_10': self.SCA_Option_10,
        }



    @classmethod
    def find_by_answer_id(cls, SCA_Option_id):
        return cls.query.filter_by(SCA_Option_id=SCA_Option_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
