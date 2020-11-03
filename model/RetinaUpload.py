from run import db
from model.user import UserModel

class RetinaUploadModel(db.Model):
    __tablename__ = 'RetinaReport'

    id = db.Column(db.Integer,primary_key=True)
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    name = db.Column(db.String(300))
    prediction = db.Column(db.String(300))
    accuracy = db.Column(db.Float)
    report = db.Column(db.LargeBinary(length=(2**32)-1))
    #report = db.Column(db.String(300))

    users = db.relationship('UserModel')

    def __init__(self,user_id,name,prediction,accuracy,report):

                 self.user_id = user_id
                 self.name = name
                 self.prediction = prediction
                 self.accuracy = accuracy
                 self.report = report



    def json(self):
        return{
                 'name' : self.name,
                 'prediction' : self.prediction,
                 'accuracy' : self.accuracy,
                 

        }
    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
