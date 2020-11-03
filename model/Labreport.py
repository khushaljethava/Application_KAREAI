from run import db
from model.user import UserModel


class LabReportModel(db.Model):
    __tablename__ = 'LabReport'


    id = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    HPLC = db.Column(db.Float, nullable = True)
    AVERAGE_BLOOD_GLUCOSE = db.Column(db.Float, nullable = True)
    TOTAL_LEUCOCYTES_COUNT  = db.Column(db.Float, nullable = True)
    NEUTROPHILS = db.Column(db.Float, nullable = True)
    LYMPHOCYTE_PERCENTAGE = db.Column(db.Float, nullable = True)
    MONOCYTES = db.Column(db.Float, nullable = True)
    EOSINOPHILS = db.Column(db.Float, nullable = True)
    BASOPHILS = db.Column(db.Float, nullable = True)
    IMMATURE_GRANULOCYTE_PERCENTAGE = db.Column(db.Float, nullable = True)
    NEUTROPHILS_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    LYMPHOCYTES_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    MONOCYTES_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    BASOPHILS_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    EOSINOPHILS_ABSOLUTE_COUNT = db.Column(db.Float, nullable = True)
    IMMATURE_GRANULOCYTES = db.Column(db.Float, nullable = True)
    TOTAL_RBC = db.Column(db.Float, nullable = True)
    NUCLEATED_RED_BLOOD_CELLS = db.Column(db.Float, nullable = True)
    HEMOGLOBIN = db.Column(db.Float, nullable = True)
    HEMATOCRIT = db.Column(db.Float, nullable = True)
    MEAN_CORPUSCULAR_VOLUME = db.Column(db.Float, nullable = True)
    MEAN_CORPUSCULAR_HEMOGLOBIN = db.Column(db.Float, nullable = True)
    MEAN_CORP_HEMO_CONC = db.Column(db.Float, nullable = True)
    RED_CELL_DISTRIBUTION_WIDTH_SD = db.Column(db.Float, nullable = True)
    RED_CELL_DISTRIBUTION_WIDTH_CV = db.Column(db.Float, nullable = True)
    PLATELET_DISTRIBUTION_WIDTH = db.Column(db.Float, nullable = True)
    MEAN_PLATELET_VOLUME = db.Column(db.Float, nullable = True)
    PLATELET_COUNT = db.Column(db.Float, nullable = True)
    PLATELET_TO_LARGE_CELL_RATIO = db.Column(db.Float, nullable = True)
    PLATELETCRIT = db.Column(db.Float, nullable = True)
    ARSENIC =  db.Column(db.Float, nullable = True)
    CADMIUM = db.Column(db.Float, nullable = True)
    MERCURY = db.Column(db.Float, nullable = True)
    LEAD = db.Column(db.Float, nullable = True)
    CHROMIUM = db.Column(db.Float, nullable = True)
    BARIUM = db.Column(db.Float, nullable = True)
    COBALT = db.Column(db.Float, nullable = True)
    CAESIUM = db.Column(db.Float, nullable = True)
    THALLIUM = db.Column(db.Float, nullable = True)
    URANIUM = db.Column(db.Float, nullable = True)
    STRONTIUM = db.Column(db.Float, nullable = True)
    ANTIMONY = db.Column(db.Float, nullable = True)
    TIN = db.Column(db.Float, nullable = True)
    MOLYBDENUM = db.Column(db.Float, nullable = True)
    SILVER = db.Column(db.Float, nullable = True)
    VANADIUM = db.Column(db.Float, nullable = True)
    BERYLLIUM = db.Column(db.Float, nullable = True)
    BISMUTH = db.Column(db.Float, nullable = True)
    SELENIUM = db.Column(db.Float, nullable = True)
    ALUMINIUM = db.Column(db.Float, nullable = True)
    NICKEL = db.Column(db.Float, nullable = True)
    MANGANESE = db.Column(db.Float, nullable = True)
    HOMOCYSTEINE = db.Column(db.Float, nullable = True)
    CYSTATIN_C = db.Column(db.Float, nullable = True)
    LIPOPROTEIN = db.Column(db.Float, nullable = True)
    VITAMIN_B = db.Column(db.Float, nullable = True)
    APOLIPOPROTEIN_A_APOA = db.Column(db.Float, nullable = True)
    APOLIPOPROTEIN_B_APOB = db.Column(db.Float, nullable = True)
    APOB_APOA_RATIO = db.Column(db.Float, nullable = True)
    HSCRP = db.Column(db.Float, nullable = True)
    SERUM_COPPER = db.Column(db.Float, nullable = True)
    SERUM_ZINC = db.Column(db.Float, nullable = True)
    TESTOSTERONE = db.Column(db.Float, nullable = True)
    IRON = db.Column(db.Float, nullable = True)
    TOTAL_IRON_BINDING_CAPACITY = db.Column(db.Float, nullable = True)
    TRANSFERRIN_SATURATION = db.Column(db.Float, nullable = True)
    ALKALINE_PHOSPHATASE = db.Column(db.Float, nullable = True)
    BILIRUBIN_TOTAL = db.Column(db.Float, nullable = True)
    BILIRUBIN_DIRECT = db.Column(db.Float, nullable = True)
    BILIRUBIN_INDIRECT = db.Column(db.Float, nullable = True)
    GAMMA_GLUTAMYL_TRANSFERASE = db.Column(db.Float, nullable = True)
    ASPARTATE_AMINOTRANSFERASE = db.Column(db.Float, nullable = True)
    ALANINE_TRANSAMINASE = db.Column(db.Float, nullable = True)
    PROTEIN_TOTAL = db.Column(db.Float, nullable = True)
    ALBUMIN_SERUM = db.Column(db.Float, nullable = True)
    SERUM_ALB = db.Column(db.Float, nullable = True)
    SERUM_GLOBULIN = db.Column(db.Float, nullable = True)
    TOTAL_CHOLESTEROL = db.Column(db.Float, nullable = True)
    HDL_CHOLESTEROL_DIRECT = db.Column(db.Float, nullable = True)
    LDL_CHOLESTEROL_DIRECT = db.Column(db.Float, nullable = True)
    TRIGLYCERIDES = db.Column(db.Float, nullable = True)
    TC_HDL_CHOLESTEROL_RATIO = db.Column(db.Float, nullable = True)
    LDL_HDL_RATIO = db.Column(db.Float, nullable = True)
    VLDL_CHOLESTEROL = db.Column(db.Float, nullable = True)
    NON_HDL_CHOLESTEROL = db.Column(db.Float, nullable = True)
    TOTAL_TRIIODOTHYRONINE = db.Column(db.Float, nullable = True)
    TOTAL_THYROXINE = db.Column(db.Float, nullable = True)
    THYROID_STIMULATING_HORMONE = db.Column(db.Float, nullable = True)
    BLOOD_UREA_NITROGEN = db.Column(db.Float, nullable = True)
    CREATININE_SERUM = db.Column(db.Float, nullable = True)
    BUN_SR_CREATININE_RATIO = db.Column(db.Float, nullable = True)
    CALCIUM = db.Column(db.Float, nullable = True)
    URIC_ACID = db.Column(db.Float, nullable = True)
    EST_GLOMERULAR_FILTRATION_RATE = db.Column(db.Float, nullable = True)

    users = db.relationship('UserModel')


    def __init__(self,user_id,HPLC,AVERAGE_BLOOD_GLUCOSE,TOTAL_LEUCOCYTES_COUNT,NEUTROPHILS,
                LYMPHOCYTE_PERCENTAGE, MONOCYTES,EOSINOPHILS,BASOPHILS,IMMATURE_GRANULOCYTE_PERCENTAGE,
                NEUTROPHILS_ABSOLUTE_COUNT,LYMPHOCYTES_ABSOLUTE_COUNT,MONOCYTES_ABSOLUTE_COUNT,
                BASOPHILS_ABSOLUTE_COUNT,EOSINOPHILS_ABSOLUTE_COUNT,IMMATURE_GRANULOCYTES,TOTAL_RBC,
                NUCLEATED_RED_BLOOD_CELLS,HEMOGLOBIN,HEMATOCRIT,MEAN_CORPUSCULAR_VOLUME,MEAN_CORPUSCULAR_HEMOGLOBIN,
                MEAN_CORP_HEMO_CONC,RED_CELL_DISTRIBUTION_WIDTH_SD,RED_CELL_DISTRIBUTION_WIDTH_CV,
                PLATELET_DISTRIBUTION_WIDTH,MEAN_PLATELET_VOLUME,PLATELET_COUNT,PLATELET_TO_LARGE_CELL_RATIO,PLATELETCRIT,
                ARSENIC,CADMIUM,MERCURY,LEAD,CHROMIUM,BARIUM,COBALT,CAESIUM,THALLIUM,URANIUM,STRONTIUM,ANTIMONY,TIN,MOLYBDENUM,
                SILVER,VANADIUM,BERYLLIUM,BISMUTH,SELENIUM,ALUMINIUM,NICKEL,MANGANESE,HOMOCYSTEINE,CYSTATIN_C,LIPOPROTEIN,
                VITAMIN_B,APOLIPOPROTEIN_A_APOA,APOLIPOPROTEIN_B_APOB,APOB_APOA_RATIO,HSCRP,SERUM_COPPER,SERUM_ZINC,TESTOSTERONE,
                IRON,TOTAL_IRON_BINDING_CAPACITY,TRANSFERRIN_SATURATION,ALKALINE_PHOSPHATASE,BILIRUBIN_TOTAL,BILIRUBIN_DIRECT,
                BILIRUBIN_INDIRECT,GAMMA_GLUTAMYL_TRANSFERASE,ASPARTATE_AMINOTRANSFERASE,ALANINE_TRANSAMINASE,PROTEIN_TOTAL,
                ALBUMIN_SERUM,SERUM_ALB,SERUM_GLOBULIN,TOTAL_CHOLESTEROL,HDL_CHOLESTEROL_DIRECT,LDL_CHOLESTEROL_DIRECT,
                TRIGLYCERIDES,TC_HDL_CHOLESTEROL_RATIO,LDL_HDL_RATIO,VLDL_CHOLESTEROL,NON_HDL_CHOLESTEROL,
                TOTAL_TRIIODOTHYRONINE,TOTAL_THYROXINE,THYROID_STIMULATING_HORMONE,BLOOD_UREA_NITROGEN,CREATININE_SERUM,
                BUN_SR_CREATININE_RATIO,CALCIUM,URIC_ACID,EST_GLOMERULAR_FILTRATION_RATE):


                self.user_id = user_id
                self.HPLC = HPLC
                self.AVERAGE_BLOOD_GLUCOSE = AVERAGE_BLOOD_GLUCOSE
                self.TOTAL_LEUCOCYTES_COUNT  = TOTAL_LEUCOCYTES_COUNT
                self.NEUTROPHILS = NEUTROPHILS
                self.LYMPHOCYTE_PERCENTAGE = LYMPHOCYTE_PERCENTAGE
                self.MONOCYTES = MONOCYTES
                self.EOSINOPHILS = EOSINOPHILS
                self.BASOPHILS = BASOPHILS
                self.IMMATURE_GRANULOCYTE_PERCENTAGE = IMMATURE_GRANULOCYTE_PERCENTAGE
                self.NEUTROPHILS_ABSOLUTE_COUNT = NEUTROPHILS_ABSOLUTE_COUNT
                self.LYMPHOCYTES_ABSOLUTE_COUNT = LYMPHOCYTES_ABSOLUTE_COUNT
                self.MONOCYTES_ABSOLUTE_COUNT = MONOCYTES_ABSOLUTE_COUNT
                self.BASOPHILS_ABSOLUTE_COUNT = BASOPHILS_ABSOLUTE_COUNT
                self.EOSINOPHILS_ABSOLUTE_COUNT = EOSINOPHILS_ABSOLUTE_COUNT
                self.IMMATURE_GRANULOCYTES = IMMATURE_GRANULOCYTES
                self.TOTAL_RBC = TOTAL_RBC
                self.NUCLEATED_RED_BLOOD_CELLS = NUCLEATED_RED_BLOOD_CELLS
                self.HEMOGLOBIN = HEMOGLOBIN
                self.HEMATOCRIT = HEMATOCRIT
                self.MEAN_CORPUSCULAR_VOLUME = MEAN_CORPUSCULAR_VOLUME
                self.MEAN_CORPUSCULAR_HEMOGLOBIN = MEAN_CORPUSCULAR_HEMOGLOBIN
                self.MEAN_CORP_HEMO_CONC = MEAN_CORP_HEMO_CONC
                self.RED_CELL_DISTRIBUTION_WIDTH_SD = RED_CELL_DISTRIBUTION_WIDTH_SD
                self.RED_CELL_DISTRIBUTION_WIDTH_CV = RED_CELL_DISTRIBUTION_WIDTH_CV
                self.PLATELET_DISTRIBUTION_WIDTH = PLATELET_DISTRIBUTION_WIDTH
                self.MEAN_PLATELET_VOLUME = MEAN_PLATELET_VOLUME
                self.PLATELET_COUNT = PLATELET_COUNT
                self.PLATELET_TO_LARGE_CELL_RATIO = PLATELET_TO_LARGE_CELL_RATIO
                self.PLATELETCRIT = PLATELETCRIT
                self.ARSENIC = ARSENIC
                self.CADMIUM = CADMIUM
                self.MERCURY = MERCURY
                self.LEAD = LEAD
                self.CHROMIUM = CHROMIUM
                self.BARIUM = BARIUM
                self.COBALT = COBALT
                self.CAESIUM = CAESIUM
                self.THALLIUM = THALLIUM
                self.URANIUM = URANIUM
                self.STRONTIUM = STRONTIUM
                self.ANTIMONY = ANTIMONY
                self.TIN = TIN
                self.MOLYBDENUM = MOLYBDENUM
                self.SILVER = SILVER
                self.VANADIUM = VANADIUM
                self.BERYLLIUM = BERYLLIUM
                self.BISMUTH = BISMUTH
                self.SELENIUM = SELENIUM
                self.ALUMINIUM = ALUMINIUM
                self.NICKEL = NICKEL
                self.MANGANESE = MANGANESE
                self.HOMOCYSTEINE  = HOMOCYSTEINE
                self.CYSTATIN_C = CYSTATIN_C
                self.LIPOPROTEIN = LIPOPROTEIN
                self.VITAMIN_B = VITAMIN_B
                self.APOLIPOPROTEIN_A_APOA = APOLIPOPROTEIN_A_APOA
                self.APOLIPOPROTEIN_B_APOB = APOLIPOPROTEIN_B_APOB
                self.APOB_APOA_RATIO = APOB_APOA_RATIO
                self.HSCRP = HSCRP
                self.SERUM_COPPER = SERUM_COPPER
                self.SERUM_ZINC = SERUM_ZINC
                self.TESTOSTERONE = TESTOSTERONE
                self.IRON = IRON
                self.TOTAL_IRON_BINDING_CAPACITY = TOTAL_IRON_BINDING_CAPACITY
                self.TRANSFERRIN_SATURATION = TRANSFERRIN_SATURATION
                self.ALKALINE_PHOSPHATASE = ALKALINE_PHOSPHATASE
                self.BILIRUBIN_TOTAL = BILIRUBIN_TOTAL
                self.BILIRUBIN_DIRECT = BILIRUBIN_DIRECT
                self.BILIRUBIN_INDIRECT = BILIRUBIN_INDIRECT
                self.GAMMA_GLUTAMYL_TRANSFERASE = GAMMA_GLUTAMYL_TRANSFERASE
                self.ASPARTATE_AMINOTRANSFERASE = ASPARTATE_AMINOTRANSFERASE
                self.ALANINE_TRANSAMINASE = ALANINE_TRANSAMINASE
                self.PROTEIN_TOTAL = PROTEIN_TOTAL
                self.ALBUMIN_SERUM = ALBUMIN_SERUM
                self.SERUM_ALB = SERUM_ALB
                self.SERUM_GLOBULIN = SERUM_GLOBULIN
                self.TOTAL_CHOLESTEROL = TOTAL_CHOLESTEROL
                self.HDL_CHOLESTEROL_DIRECT = HDL_CHOLESTEROL_DIRECT
                self.LDL_CHOLESTEROL_DIRECT = LDL_CHOLESTEROL_DIRECT
                self.TRIGLYCERIDES = TRIGLYCERIDES
                self.TC_HDL_CHOLESTEROL_RATIO = TC_HDL_CHOLESTEROL_RATIO
                self.LDL_HDL_RATIO = LDL_HDL_RATIO
                self.VLDL_CHOLESTEROL = VLDL_CHOLESTEROL
                self.NON_HDL_CHOLESTEROL = NON_HDL_CHOLESTEROL
                self.TOTAL_TRIIODOTHYRONINE = TOTAL_TRIIODOTHYRONINE
                self.TOTAL_THYROXINE = TOTAL_THYROXINE
                self.THYROID_STIMULATING_HORMONE = THYROID_STIMULATING_HORMONE
                self.BLOOD_UREA_NITROGEN = BLOOD_UREA_NITROGEN
                self.CREATININE_SERUM = CREATININE_SERUM
                self.BUN_SR_CREATININE_RATIO = BUN_SR_CREATININE_RATIO
                self.CALCIUM = CALCIUM
                self.URIC_ACID = URIC_ACID
                self.EST_GLOMERULAR_FILTRATION_RATE = EST_GLOMERULAR_FILTRATION_RATE


    def json(self):
        return {
        'HPLC': self.HPLC,
        'AVERAGE_BLOOD_GLUCOSE': self.AVERAGE_BLOOD_GLUCOSE,
        'TOTAL_LEUCOCYTES_COUNT': self.TOTAL_LEUCOCYTES_COUNT ,
        'NEUTROPHILS': self.NEUTROPHILS,
        'LYMPHOCYTE_PERCENTAGE': self.LYMPHOCYTE_PERCENTAGE,
        'MONOCYTES': self.MONOCYTES,
        'EOSINOPHILS': self.EOSINOPHILS,
        'BASOPHILS': self.BASOPHILS,
        'IMMATURE_GRANULOCYTE_PERCENTAGE': self.IMMATURE_GRANULOCYTE_PERCENTAGE,
        'NEUTROPHILS_ABSOLUTE_COUNT': self.NEUTROPHILS_ABSOLUTE_COUNT,
        'LYMPHOCYTES_ABSOLUTE_COUNT': self.LYMPHOCYTES_ABSOLUTE_COUNT,
        'MONOCYTES_ABSOLUTE_COUNT': self.MONOCYTES_ABSOLUTE_COUNT,
        'BASOPHILS_ABSOLUTE_COUNT': self.BASOPHILS_ABSOLUTE_COUNT,
        'EOSINOPHILS_ABSOLUTE_COUNT': self.EOSINOPHILS_ABSOLUTE_COUNT,
        'IMMATURE_GRANULOCYTES': self.IMMATURE_GRANULOCYTES,
        'TOTAL_RBC': self.TOTAL_RBC,
        'NUCLEATED_RED_BLOOD_CELLS': self.NUCLEATED_RED_BLOOD_CELLS,
        'HEMOGLOBIN': self.HEMOGLOBIN,
        'HEMATOCRIT': self.HEMATOCRIT,
        'MEAN_CORPUSCULAR_VOLUME': self.MEAN_CORPUSCULAR_VOLUME,
        'MEAN_CORPUSCULAR_HEMOGLOBIN': self.MEAN_CORPUSCULAR_HEMOGLOBIN,
        'MEAN_CORP_HEMO_CONC': self.MEAN_CORP_HEMO_CONC,
        'RED_CELL_DISTRIBUTION_WIDTH_SD': self.RED_CELL_DISTRIBUTION_WIDTH_SD,
        'RED_CELL_DISTRIBUTION_WIDTH_CV': self.RED_CELL_DISTRIBUTION_WIDTH_CV,
        'PLATELET_DISTRIBUTION_WIDTH': self.PLATELET_DISTRIBUTION_WIDTH,
        'MEAN_PLATELET_VOLUME': self.MEAN_PLATELET_VOLUME,
        'PLATELET_COUNT': self.PLATELET_COUNT,
        'PLATELET_TO_LARGE_CELL_RATIO': self.PLATELET_TO_LARGE_CELL_RATIO,
        'PLATELETCRIT': self.PLATELETCRIT,
        'ARSENIC' : self.ARSENIC,
        'CADMIUM' :self.CADMIUM,
        'MERCURY': self.MERCURY,
        'LEAD': self.LEAD,
        'CHROMIUM': self.CHROMIUM,
        'BARIUM' : self.BARIUM,
        'COBALT': self.COBALT,
        'CAESIUM': self.CAESIUM,
        'THALLIUM': self.THALLIUM,
        'URANIUM': self.URANIUM,
        'STRONTIUM': self.STRONTIUM,
        'ANTIMONY': self.ANTIMONY,
        'TIN': self.TIN,
        'MOLYBDENUM': self.MOLYBDENUM,
        'SILVER': self.SILVER,
        'VANADIUM': self.VANADIUM,
        'BERYLLIUM': self.BERYLLIUM,
        'BISMUTH': self.BISMUTH,
        'SELENIUM': self.SELENIUM,
        'ALUMINIUM': self.ALUMINIUM,
        'NICKEL': self.NICKEL,
        'MANGANESE': self.MANGANESE,
        'HOMOCYSTEINE': self.HOMOCYSTEINE,
        'CYSTATIN_C': self.CYSTATIN_C,
        'LIPOPROTEIN': self.LIPOPROTEIN,
        'VITAMIN_B': self.VITAMIN_B,
        'APOLIPOPROTEIN_A_APOA' : self.APOLIPOPROTEIN_A_APOA,
        'APOLIPOPROTEIN_B_APOB': self.APOLIPOPROTEIN_B_APOB,
        'APOB_APOA_RATIO': self.APOB_APOA_RATIO,
        'HSCRP': self.HSCRP,
        'SERUM_COPPER': self.SERUM_COPPER,
        'SERUM_ZINC': self.SERUM_ZINC,
        'TESTOSTERONE': self.TESTOSTERONE,
        'IRON' :self.IRON,
        'TOTAL_IRON_BINDING_CAPACITY': self.TOTAL_IRON_BINDING_CAPACITY,
        'TRANSFERRIN_SATURATION': self.TRANSFERRIN_SATURATION,
        'ALKALINE_PHOSPHATASE': self.ALKALINE_PHOSPHATASE,
        'BILIRUBIN_TOTAL': self.BILIRUBIN_TOTAL,
        'BILIRUBIN_DIRECT': self.BILIRUBIN_DIRECT,
        'BILIRUBIN_INDIRECT': self.BILIRUBIN_INDIRECT,
        'GAMMA_GLUTAMYL_TRANSFERASE': self.GAMMA_GLUTAMYL_TRANSFERASE,
        'ASPARTATE_AMINOTRANSFERASE': self.ASPARTATE_AMINOTRANSFERASE,
        'ALANINE_TRANSAMINASE': self.ALANINE_TRANSAMINASE,
        'PROTEIN_TOTAL': self.PROTEIN_TOTAL,
        'ALBUMIN_SERUM': self.ALBUMIN_SERUM,
        'SERUM_ALB': self.SERUM_ALB,
        'SERUM_GLOBULIN': self.SERUM_GLOBULIN,
        'TOTAL_CHOLESTEROL': self.TOTAL_CHOLESTEROL,
        'HDL_CHOLESTEROL_DIRECT': self.HDL_CHOLESTEROL_DIRECT,
        'LDL_CHOLESTEROL_DIRECT': self.LDL_CHOLESTEROL_DIRECT,
        'TRIGLYCERIDES': self.TRIGLYCERIDES,
        'TC_HDL_CHOLESTEROL_RATIO': self.TC_HDL_CHOLESTEROL_RATIO,
        'LDL_HDL_RATIO': self.LDL_HDL_RATIO,
        'VLDL_CHOLESTEROL': self.VLDL_CHOLESTEROL,
        'NON_HDL_CHOLESTEROL': self.NON_HDL_CHOLESTEROL,
        'TOTAL_TRIIODOTHYRONINE': self.TOTAL_TRIIODOTHYRONINE,
        'TOTAL_THYROXINE': self.TOTAL_THYROXINE,
        'THYROID_STIMULATING_HORMONE': self.THYROID_STIMULATING_HORMONE,
        'BLOOD_UREA_NITROGEN': self.BLOOD_UREA_NITROGEN,
        'CREATININE_SERUM': self.CREATININE_SERUM,
        'BUN_SR_CREATININE_RATIO': self.BUN_SR_CREATININE_RATIO,
        'CALCIUM': self.CALCIUM,
        'URIC_ACID': self.URIC_ACID,
        'EST_GLOMERULAR_FILTRATION_RATE': self.EST_GLOMERULAR_FILTRATION_RATE
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
