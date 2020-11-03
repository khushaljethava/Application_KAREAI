from run import db
from model.user import UserModel

class FamilyHistoryModel(db.Model):
    __tablename__ = 'FamilyHistory'


    id = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    Member = db.Column(db.String(120), nullable = False)
    Alcoholism = db.Column(db.String(120), nullable = False)
    Allergies= db.Column(db.String(120), nullable = False)
    Anesthesia= db.Column(db.String(120), nullable = False)
    Anxiety= db.Column(db.String(120), nullable = False)
    Arthritis = db.Column(db.String(120), nullable = False)
    Asthma = db.Column(db.String(120), nullable = False)
    ADHD = db.Column(db.String(120), nullable = False)
    Birth_Defects = db.Column(db.String(120), nullable = False)
    Blood_Problem = db.Column(db.String(120), nullable = False)
    Bone_Joint_Problems = db.Column(db.String(120), nullable = False)
    Breast_Disease = db.Column(db.String(120), nullable = False)
    Cancer = db.Column(db.String(120), nullable = False)
    Chicken_Pox = db.Column(db.String(120), nullable = False)
    Colitis = db.Column(db.String(120), nullable = False)
    Depression = db.Column(db.String(120), nullable = False)
    Diabetes = db.Column(db.String(120), nullable = False)
    ENT_Problems = db.Column(db.String(120), nullable = False)
    Eating_Disorders = db.Column(db.String(120), nullable = False)
    Eczema = db.Column(db.String(120), nullable = False)
    Epilepsy = db.Column(db.String(120), nullable = False)
    Fertility = db.Column(db.String(120), nullable = False)
    Gallbladder = db.Column(db.String(120), nullable = False)
    Gynecology = db.Column(db.String(120), nullable = False)
    Fever = db.Column(db.String(120), nullable = False)
    Headaches = db.Column(db.String(120), nullable = False)
    Heart_Problems = db.Column(db.String(120), nullable = False)
    Heart_Attack_Over_60 = db.Column(db.String(120), nullable = False)
    Heart_Attack_Under_60 = db.Column(db.String(120), nullable = False)
    Heart_Murmur = db.Column(db.String(120), nullable = False)
    Hepatitis = db.Column(db.String(120), nullable = False)
    High_Blood_Pressure = db.Column(db.String(120), nullable = False)
    High_Cholestorol  = db.Column(db.String(120), nullable = False)

    users = db.relationship('UserModel')

    def __init__(self,user_id,Member, Alcoholism, Allergies, Anesthesia, Anxiety, Arthritis, Asthma, ADHD, Birth_Defects, Blood_Problem,
                 Bone_Joint_Problems, Breast_Disease, Cancer, Chicken_Pox, Colitis, Depression, Diabetes, ENT_Problems, Eating_Disorders, Eczema, Epilepsy,
                 Fertility, Gallbladder, Gynecology, Fever, Headaches, Heart_Problems, Heart_Attack_Over_60, Heart_Attack_Under_60, Heart_Murmur, Hepatitis,
                 High_Blood_Pressure, High_Cholestorol):

                 self.user_id = user_id
                 self.Member = Member
                 self.Alcoholism = Alcoholism
                 self.Allergies = Allergies
                 self.Anesthesia = Anesthesia
                 self.Anxiety = Anxiety
                 self.Arthritis = Arthritis
                 self.Asthma = Asthma
                 self.ADHD = ADHD
                 self.Birth_Defects = Birth_Defects
                 self.Blood_Problem = Blood_Problem
                 self.Bone_Joint_Problems = Bone_Joint_Problems
                 self.Breast_Disease = Breast_Disease
                 self.Cancer = Cancer
                 self.Chicken_Pox = Chicken_Pox
                 self.Colitis = Colitis
                 self.Depression = Depression
                 self.Diabetes = Diabetes
                 self.ENT_Problems = ENT_Problems
                 self.Eating_Disorders = Eating_Disorders
                 self.Eczema = Eczema
                 self.Epilepsy = Epilepsy
                 self.Fertility = Fertility
                 self.Gallbladder = Gallbladder
                 self.Gynecology = Gynecology
                 self.Fever = Fever
                 self.Headaches = Headaches
                 self.Heart_Problems = Heart_Problems
                 self.Heart_Attack_Over_60 = Heart_Attack_Over_60
                 self.Heart_Attack_Under_60 = Heart_Attack_Under_60
                 self.Heart_Murmur = Heart_Murmur
                 self.Hepatitis = Hepatitis
                 self.High_Blood_Pressure = High_Blood_Pressure
                 self.High_Cholestorol = High_Cholestorol



    def json(self):
         return{
         'Member' : self.Member,
         'Alcoholism' : self.Alcoholism,
         'Allergies': self.Allergies,
         'Anesthesia': self.Anesthesia,
         'Anxiety': self.Anxiety,
         'Arthritis': self.Arthritis,
         'Asthma': self.Asthma,
         'ADHD': self.ADHD,
         'Birth_Defects': self.Birth_Defects,
         'Blood_Problem': self.Blood_Problem,
         'Bone_Joint_Problems': self.Bone_Joint_Problems,
         'Breast_Disease': self.Breast_Disease,
         'Cancer' : self.Cancer,
         'Chicken_Pox': self.Chicken_Pox,
         'Colitis': self.Colitis,
         'Depression': self.Depression,
         'Diabetes': self.Diabetes,
         'ENT_Problems': self.ENT_Problems,
         'Eating_Disorders': self.Eating_Disorders,
         'Eczema' : self.Eczema,
         'Epilepsy': self.Epilepsy,
         'Fertility': self.Fertility,
         'Gallbladder': self.Gallbladder,
         'Gynecology': self.Gynecology,
         'Fever' : self.Fever,
         'Headaches': self.Headaches,
         'Heart_Problems': self.Heart_Problems,
         'Heart_Attack_Over_60': self.Heart_Attack_Over_60,
         'Heart_Attack_Under_60': self.Heart_Attack_Under_60,
         'Heart_Murmur': self.Heart_Murmur,
         'Hepatitis': self.Hepatitis,
         'High_Blood_Pressure': self.High_Blood_Pressure,
         'High_Cholestorol': self.High_Cholestorol
}



    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).first()


    @classmethod
    def find_by_member(cls, Member):
        return cls.query.filter_by(Member = Member).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
