from run import db
from model.user import UserModel

class LabReportUploadModel(db.Model):
    __tablename__ = 'LabReportFiles'

    id = db.Column(db.Integer,primary_key=True)
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    name = db.Column(db.String(300))
    report = db.Column(db.LargeBinary(length=(2**32)-1))

    users = db.relationship('UserModel')

    def __init__(self,user_id,name,report):

                 self.user_id = user_id
                 self.name = name
                 self.report = report




    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
