from run import db
from model.user import UserModel



class PreConditionModel(db.Model):
    __tablename__ = 'PreexistingCondition'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    Race = db.Column(db.String(120), nullable = False)
    Smoking = db.Column(db.String(120), nullable = False)
    Alcohol = db.Column(db.String(120), nullable = False)
    Diabetes = db.Column(db.String(120), nullable = False)
    Hear = db.Column(db.String(120), nullable = False)
    Blood_Pressure = db.Column(db.String(120), nullable = False)
    Chest_Pain = db.Column(db.String(120), nullable = False)
    Stroke =  db.Column(db.String(120), nullable = False)
    Kidney  = db.Column(db.String(120), nullable = False)
    Blood_Clot = db.Column(db.String(120), nullable = False)
    Metal_implants = db.Column(db.String(120), nullable = False)
    Asthma = db.Column(db.String(120), nullable = False)
    Cancer = db.Column(db.String(120), nullable = False)
    Difficulty_Swallowing = db.Column(db.String(120), nullable = False)
    Vascular_Problems = db.Column(db.String(120), nullable = False)
    Peripheral_Neuropathy = db.Column(db.String(120), nullable = False)
    Weightloss = db.Column(db.String(120), nullable = False)
    Double_Vision = db.Column(db.String(120), nullable = False)
    Night_Sweats = db.Column(db.String(120), nullable = False)
    Night_Pain = db.Column(db.String(120), nullable = False)
    Neurologic_Condition = db.Column(db.String(120), nullable = False)
    Skin_Disease = db.Column(db.String(120), nullable = False)
    Spinal_Cord_Injury = db.Column(db.String(120), nullable = False)
    Degenerative_Joint_Disease = db.Column(db.String(120), nullable = False)
    Sexual_Dysfunction = db.Column(db.String(120), nullable = False)
    Bladder = db.Column(db.String(120), nullable = False)
    Groin_Numbness = db.Column(db.String(120), nullable = False)
    Arthritis = db.Column(db.String(120), nullable = False)
    Osteoporosis = db.Column(db.String(120), nullable = False)
    Phsychological_Problems = db.Column(db.String(120), nullable = False)
    Seizures = db.Column(db.String(120), nullable = False)
    Dizziness = db.Column(db.String(120), nullable = False)
    Ringing_in_Ears = db.Column(db.String(120), nullable = False)
    Allergy_to_Latex   = db.Column(db.String(120), nullable = False)
    Head_Injury = db.Column(db.String(120), nullable = False)
    Obesity = db.Column(db.String(120), nullable = False)
    Chronic_Pain = db.Column(db.String(120), nullable = False)
    Fractures  = db.Column(db.String(120), nullable = False)
    Infection_Dissease  = db.Column(db.String(120), nullable = False)
    Fever = db.Column(db.String(120), nullable = False)
    Lower_Extremety = db.Column(db.String(120), nullable = False)
    Nausea = db.Column(db.String(120), nullable = False)

    users = db.relationship('UserModel')


    def __init__(self,user_id,Race, Smoking, Alcohol, Diabetes, Hear, Blood_Pressure, Chest_Pain, Stroke,
         Kidney, Blood_Clot, Metal_implants, Asthma, Cancer, Difficulty_Swallowing, Vascular_Problems,
         Peripheral_Neuropathy, Weightloss, Double_Vision, Night_Sweats, Night_Pain, Neurologic_Condition,
          Skin_Disease, Spinal_Cord_Injury, Degenerative_Joint_Disease, Sexual_Dysfunction, Bladder,
          Groin_Numbness, Arthritis, Osteoporosis, Phsychological_Problems, Seizures, Dizziness,
          Ringing_in_Ears, Allergy_to_Latex, Head_Injury, Obesity, Chronic_Pain, Fractures,
          Infection_Dissease, Fever, Lower_Extremety, Nausea):


        self.user_id = user_id
        self.Race = Race
        self.Smoking = Smoking
        self.Alcohol = Alcohol
        self.Diabetes = Diabetes
        self.Hear = Hear
        self.Blood_Pressure = Blood_Pressure
        self.Chest_Pain = Chest_Pain
        self.Stroke =  Stroke
        self.Kidney  = Kidney
        self.Blood_Clot = Blood_Clot
        self.Metal_implants = Metal_implants
        self.Asthma = Asthma
        self.Cancer = Cancer
        self.Difficulty_Swallowing = Difficulty_Swallowing
        self.Vascular_Problems = Vascular_Problems
        self.Peripheral_Neuropathy = Peripheral_Neuropathy
        self.Weightloss = Weightloss
        self.Double_Vision = Double_Vision
        self.Night_Sweats = Night_Sweats
        self.Night_Pain = Night_Pain
        self.Neurologic_Condition = Neurologic_Condition
        self.Skin_Disease = Skin_Disease
        self.Spinal_Cord_Injury = Spinal_Cord_Injury
        self.Degenerative_Joint_Disease = Degenerative_Joint_Disease
        self.Sexual_Dysfunction = Sexual_Dysfunction
        self.Bladder = Bladder
        self.Groin_Numbness = Groin_Numbness
        self.Arthritis = Arthritis
        self.Osteoporosis = Osteoporosis
        self.Phsychological_Problems = Phsychological_Problems
        self.Seizures = Seizures
        self.Dizziness = Dizziness
        self.Ringing_in_Ears = Ringing_in_Ears
        self.Allergy_to_Latex   = Allergy_to_Latex
        self.Head_Injury = Head_Injury
        self.Obesity = Obesity
        self.Chronic_Pain = Chronic_Pain
        self.Fractures  = Fractures
        self.Infection_Dissease  = Infection_Dissease
        self.Fever = Fever
        self.Lower_Extremety = Lower_Extremety
        self.Nausea = Nausea

    def json(self):
        return {
        'Race' : self.Race,
        'Smoking' : self.Smoking,
        'Alcohol' :  self.Alcohol,
        'Diabetes' : self.Diabetes,
        'Hear' :  self.Hear,
        'Blood_Pressure' :  self.Blood_Pressure,
        'Chest_Pain' :  self.Chest_Pain,
        'Stroke' : self.Stroke,
         'Kidney': self.Kidney,
        'Blood_Clot' : self.Blood_Clot,
        'Metal_implants': self.Metal_implants,
        'Asthma': self.Asthma,
        'Cancer': self.Cancer,
        'Difficulty_Swallowing': self.Difficulty_Swallowing,
        'Vascular_Problems' : self.Vascular_Problems,
        'Peripheral_Neuropathy': self.Peripheral_Neuropathy,
        'Weightloss': self.Weightloss,
        'Double_Vision': self.Double_Vision,
        'Night_Sweats': self.Night_Sweats,
        'Night_Pain' : self.Night_Pain,
        'Neurologic_Condition': self.Neurologic_Condition,
        'Skin_Disease': self.Skin_Disease,
        'Spinal_Cord_Injury': self.Spinal_Cord_Injury,
        'Degenerative_Joint_Disease': self.Degenerative_Joint_Disease,
        'Sexual_Dysfunction': self.Sexual_Dysfunction,
        'Bladder': self.Bladder,
        'Groin_Numbness': self.Groin_Numbness,
        'Arthritis': self.Arthritis,
        'Osteoporosis': self.Osteoporosis,
        'Phsychological_Problems': self.Phsychological_Problems,
        'Seizures': self.Seizures,
        'Dizziness': self.Dizziness,
        'Ringing_in_Ears': self.Ringing_in_Ears,
        'Allergy_to_Latex': self.Allergy_to_Latex,
        'Head_Injury': self.Head_Injury,
        'Obesity': self.Obesity,
        'Chronic_Pain': self.Chronic_Pain,
        'Fractures': self.Fractures,
        'Infection_Dissease': self.Infection_Dissease,
        'Fever': self.Fever,
        'Lower_Extremety': self.Lower_Extremety,
        'Nausea': self.Nausea
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
