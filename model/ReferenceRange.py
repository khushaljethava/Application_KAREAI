from run import db

class ReferenceRangeModel(db.Model):
    __tablename__ = 'ReferenceRange'

    id = db.Column(db.Integer, primary_key=True)
    ProcessedBy = db.Column(db.String(120) )
    Category = db.Column(db.String(120))
    Lab_Test = db.Column(db.String(120))
    Technology = db.Column(db.String(120))
    Units = db.Column(db.String(120))
    Age = db.Column(db.String(120))
    Gender = db.Column(db.String(120))
    Range_Low = db.Column(db.Float)
    Range_High = db.Column(db.Float)
    Race = db.Column(db.String(120))
    Location = db.Column(db.String(120))



    def __init__(self, ProcessedBy,Category,Lab_Test,Technology,Units,Age,Gender,Range_Low,Range_High,Race,Location):

        self.ProcessedBy = ProcessedBy
        self.Category = Category
        self.Lab_Test = Lab_Test
        self.Technology = Technology
        self.Age = Age
        self.Gender = Gender
        self.Range_Low = Range_Low
        self.Range_High = Range_High
        self.Race = Race
        self.Location = Location




    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def Compare_IRON(cls):
#        Low_Range = db.select([ReferenceRangeModel.Range_Low]).where(ReferenceRangeModel.Lab_Test == 'Iron')
#        Low_Range = cls.query.filter([ReferenceRangeModel.Range_Low]).where(ReferenceRangeModel.Lab_Test =='ALKALINE PHOSPHATASE')
#        Low_Range = cls.query([ReferenceRangeModel.Range_Low]).filter(ReferenceRangeModel.Lab_Test == 'Iron')
#        Low_Range = cls.query(ReferenceRangeModel.Range_Low).filter_by(ReferenceRangeModel.Lab_Test == 'Iron').first()
#        Low_Range = ReferenceRangeModel.select().where(ReferenceRangeModel.Lab_Test == 'ALKALINE PHOSPHATASE')
#        Low_Range = "SELECT Range_Low FROM `ReferenceRange` WHERE Lab_Test = 'ALKALINE PHOSPHATASE'"
#        result = db.session.execute(Low_Range)
        result = db.session.query(ReferenceRangeModel.Range_Low).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.Gender=='F').first()

        return result
