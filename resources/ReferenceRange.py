from run import db
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from model.ReferenceRange import ReferenceRangeModel
import pandas as pd

class ReferenceRange(Resource):

    def get(self):
        IRON =  40
        #if IRON >= db.session.query(ReferenceRangeModel.Range_Low).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.Gender=='F').first() and IRON <= db.session.query(ReferenceRangeModel.Range_High).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.Gender=='F').first():
        #    print('Working')



#        lowrange = ReferenceRangeModel.Compare_IRON()
        lowrange = db.session.query(ReferenceRangeModel.Range_Low).filter(ReferenceRangeModel.Lab_Test == 'test' , ReferenceRangeModel.Gender=='F').first()
        highrange = db.session.query(ReferenceRangeModel.Range_High).filter(ReferenceRangeModel.Lab_Test == 'test', ReferenceRangeModel.Gender=='F').first()
        print(lowrange)
        highrange = float(pd.to_numeric(highrange))
        lowrange = float(pd.to_numeric(lowrange))

        print(highrange)
        #highrange1 = float(str(highrange))
        #result = [str(path) for path in lowrange]
        #print(type(result))
        print(lowrange,highrange)
        #print(highrange1)
        #result1 = [str(path) for path in highrange]
        #print(type(result1))
        print(highrange)
        print(type(IRON))
        print(type(lowrange))
        print(type(highrange))
        if IRON <= (lowrange):
            print("YO")
        elif IRON >= (highrange):
            print("LOdu")


        if IRON <= lowrange:
            print("Low")
        elif IRON >= highrange:
            print("High")
        elif lowrange <= IRON <= highrange:
            print("Between")
