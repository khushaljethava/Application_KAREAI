from run import db
from model.user import UserModel

class LabReportUploadModel(db.Model):
    __tablename__ = 'LabReportFiles'

    LU_id = db.Column(db.Integer,primary_key=True)
    LU_user_id  = db.Column(db.Integer,db.ForeignKey('users.u_id'))
    LU_name = db.Column(db.String(300))
    LU_report = db.Column(db.LargeBinary(length=(2**32)-1))

    users = db.relationship('UserModel')

    def __init__(self,LU_user_id,LU_name,LU_report):

                 self.LU_user_id = LU_user_id
                 self.LU_name = LU_name
                 self.LU_report = LU_report




    @classmethod
    def find_by_id(cls, LU_user_id):
        return cls.query.filter_by(LU_user_id = LU_user_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
