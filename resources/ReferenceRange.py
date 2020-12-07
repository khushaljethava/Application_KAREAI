from run import db
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from model.ReferenceRange import ReferenceRangeModel
import pandas as pd

class ReferenceRange(Resource):

    def get(self):



        #if IRON >= db.session.query(ReferenceRangeModel.Range_Low).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.gender=='F').first() and IRON <= db.session.query(ReferenceRangeModel.Range_High).filter(ReferenceRangeModel.Lab_Test == 'Iron', ReferenceRangeModel.gender=='F').first():
        #    print('Working')



#        lowrange = ReferenceRangeModel.Compare_IRON()
        lowrange = db.session.query(ReferenceRangeModel.RR_Range_Low).filter(ReferenceRangeModel.RR_Lab_Test == 'IRON' , ReferenceRangeModel.RR_gender=='F').first()
        highrange = db.session.query(ReferenceRangeModel.RR_Range_High).filter(ReferenceRangeModel.RR_Lab_Test == 'IRON', ReferenceRangeModel.RR_gender=='F').first()
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
