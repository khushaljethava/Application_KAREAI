from run import db
from flask_restful import Resource, reqparse
from model.Labreport import LabReportModel
from flask_jwt_extended import jwt_required
import pandas as pd
import json

class LabReport(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('HPLC', help=' HPLC cannot be blank')
    parser.add_argument('AVERAGE_BLOOD_GLUCOSE', help=' AVERAGE_BLOOD_GLUCOSE cannot be blank')
    parser.add_argument('TOTAL_LEUCOCYTES_COUNT', help=' TOTAL_LEUCOCYTES_COUNT cannot be blank')
    parser.add_argument('NEUTROPHILS', help=' NEUTROPHILS cannot be blank')
    parser.add_argument('LYMPHOCYTE_PERCENTAGE', help=' LYMPHOCYTE_PERCENTAGE cannot be blank')
    parser.add_argument('MONOCYTES', help=' MONOCYTES cannot be blank')
    parser.add_argument('EOSINOPHILS', help=' EOSINOPHILS cannot be blank')
    parser.add_argument('BASOPHILS', help=' BASOPHILS cannot be blank')
    parser.add_argument('IMMATURE_GRANULOCYTE_PERCENTAGE', help=' IMMATURE_GRANULOCYTE_PERCENTAGE cannot be blank')
    parser.add_argument('NEUTROPHILS_ABSOLUTE_COUNT', help=' NEUTROPHILS_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('LYMPHOCYTES_ABSOLUTE_COUNT', help=' LYMPHOCYTES_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('MONOCYTES_ABSOLUTE_COUNT', help=' MONOCYTES_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('BASOPHILS_ABSOLUTE_COUNT', help=' BASOPHILS_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('EOSINOPHILS_ABSOLUTE_COUNT', help=' EOSINOPHILS_ABSOLUTE_COUNT cannot be blank')
    parser.add_argument('IMMATURE_GRANULOCYTES', help=' IMMATURE_GRANULOCYTES cannot be blank')
    parser.add_argument('TOTAL_RBC', help=' TOTAL_RBC cannot be blank')
    parser.add_argument('NUCLEATED_RED_BLOOD_CELLS', help=' NUCLEATED_RED_BLOOD_CELLS cannot be blank')
    parser.add_argument('HEMOGLOBIN', help=' HEMOGLOBIN cannot be blank')
    parser.add_argument('HEMATOCRIT', help=' HEMATOCRIT cannot be blank')
    parser.add_argument('MEAN_CORPUSCULAR_VOLUME', help=' MEAN_CORPUSCULAR_VOLUME cannot be blank')
    parser.add_argument('MEAN_CORPUSCULAR_HEMOGLOBIN', help=' MEAN_CORPUSCULAR_HEMOGLOBIN cannot be blank')
    parser.add_argument('MEAN_CORP_HEMO_CONC', help=' MEAN_CORP_HEMO_CONC cannot be blank')
    parser.add_argument('RED_CELL_DISTRIBUTION_WIDTH_SD', help=' RED_CELL_DISTRIBUTION_WIDTH_SD cannot be blank')
    parser.add_argument('RED_CELL_DISTRIBUTION_WIDTH_CV', help=' RED_CELL_DISTRIBUTION_WIDTH_CV cannot be blank')
    parser.add_argument('PLATELET_DISTRIBUTION_WIDTH', help=' PLATELET_DISTRIBUTION_WIDTH cannot be blank')
    parser.add_argument('MEAN_PLATELET_VOLUME', help=' MEAN_PLATELET_VOLUME cannot be blank')
    parser.add_argument('PLATELET_COUNT', help=' PLATELET_COUNT cannot be blank')
    parser.add_argument('PLATELET_TO_LARGE_CELL_RATIO', help=' PLATELET_TO_LARGE_CELL_RATIO cannot be blank')
    parser.add_argument('PLATELETCRIT', help=' PLATELETCRIT cannot be blank')
    parser.add_argument('ARSENIC', help=' ARSENIC cannot be blank')
    parser.add_argument('CADMIUM', help=' CADMIUM cannot be blank')
    parser.add_argument('MERCURY', help='MERCURY cannot be blank')
    parser.add_argument('LEAD', help='LEAD cannot be blank')
    parser.add_argument('CHROMIUM', help='CHROMIUM cannot be blank')
    parser.add_argument('BARIUM', help=' BARIUM cannot be blank')
    parser.add_argument('COBALT', help=' COBALT cannot be blank')
    parser.add_argument('CAESIUM', help=' CAESIUM cannot be blank')
    parser.add_argument('THALLIUM', help=' THALLIUM cannot be blank')
    parser.add_argument('URANIUM', help=' URANIUM cannot be blank')
    parser.add_argument('STRONTIUM', help=' STRONTIUM cannot be blank')
    parser.add_argument('ANTIMONY', help=' ANTIMONY cannot be blank')
    parser.add_argument('TIN', help=' TIN cannot be blank')
    parser.add_argument('MOLYBDENUM', help=' MOLYBDENUM cannot be blank')
    parser.add_argument('SILVER', help=' SILVER cannot be blank')
    parser.add_argument('VANADIUM', help=' VANADIUM cannot be blank')
    parser.add_argument('BERYLLIUM', help=' BERYLLIUM cannot be blank')
    parser.add_argument('BISMUTH', help=' BISMUTH cannot be blank')
    parser.add_argument('SELENIUM', help=' SELENIUM cannot be blank')
    parser.add_argument('ALUMINIUM', help=' ALUMINIUM cannot be blank')
    parser.add_argument('NICKEL', help=' NICKEL cannot be blank')
    parser.add_argument('MANGANESE', help=' MANGANESE cannot be blank')
    parser.add_argument('HOMOCYSTEINE', help=' HOMOCYSTEINE cannot be blank')
    parser.add_argument('CYSTATIN_C', help=' CYSTATIN_C cannot be blank')
    parser.add_argument('LIPOPROTEIN', help=' LIPOPROTEIN cannot be blank')
    parser.add_argument('VITAMIN_B', help=' VITAMIN B cannot be blank')
    parser.add_argument('APOLIPOPROTEIN_A_APOA', help=' APOLIPOPROTEIN_A_APOA cannot be blank')
    parser.add_argument('APOLIPOPROTEIN_B_APOB', help=' APOLIPOPROTEIN_B_APOB cannot be blank')
    parser.add_argument('APOB_APOA_RATIO', help=' APOB_APOA_RATIO cannot be blank')
    parser.add_argument('HSCRP', help=' HSCRP cannot be blank')
    parser.add_argument('SERUM_COPPER', help=' SERUM_COPPER cannot be blank')
    parser.add_argument('SERUM_ZINC', help=' SERUM_ZINC cannot be blank')
    parser.add_argument('TESTOSTERONE', help=' TESTOSTERONE cannot be blank')
    parser.add_argument('IRON', help=' IRON cannot be blank')
    parser.add_argument('TOTAL_IRON_BINDING_CAPACITY', help=' TOTAL_IRON_BINDING_CAPACITY cannot be blank')
    parser.add_argument('TRANSFERRIN_SATURATION', help=' TRANSFERRIN_SATURATION cannot be blank')
    parser.add_argument('ALKALINE_PHOSPHATASE', help=' ALKALINE_PHOSPHATASE cannot be blank')
    parser.add_argument('BILIRUBIN_TOTAL', help=' BILIRUBIN_TOTAL cannot be blank')
    parser.add_argument('BILIRUBIN_DIRECT', help=' BILIRUBIN_DIRECT cannot be blank')
    parser.add_argument('BILIRUBIN_INDIRECT', help=' BILIRUBIN_INDIRECT cannot be blank')
    parser.add_argument('GAMMA_GLUTAMYL_TRANSFERASE', help=' GAMMA_GLUTAMYL_TRANSFERASE cannot be blank')
    parser.add_argument('ASPARTATE_AMINOTRANSFERASE', help=' ASPARTATE_AMINOTRANSFERASE cannot be blank')
    parser.add_argument('ALANINE_TRANSAMINASE', help=' ALANINE_TRANSAMINASE cannot be blank')
    parser.add_argument('PROTEIN_TOTAL', help=' PlabreportEOSINOPHILSROTEIN_TOTAL cannot be blank')
    parser.add_argument('ALBUMIN_SERUM', help=' ALBUMIN_SERUM cannot be blank')
    parser.add_argument('SERUM_ALB', help=' SERUM_ALB cannot be blank')
    parser.add_argument('SERUM_GLOBULIN', help=' SERUM_GLOBULIN cannot be blank')
    parser.add_argument('TOTAL_CHOLESTEROL', help=' TOTAL_CHOLESTEROL cannot be blank')
    parser.add_argument('HDL_CHOLESTEROL_DIRECT', help=' Huser_idDL_CHOLESTEROL_DIRECT cannot be blank')
    parser.add_argument('LDL_CHOLESTEROL_DIRECT', help=' LDL_CHOLESTEROL_DIRECT cannot be blank')
    parser.add_argument('TRIGLYCERIDES', help=' TRIGLYCERIDES cannot be blank')
    parser.add_argument('TC_HDL_CHOLESTEROL_RATIO', help=' TC_HDL_CHOLESTEROL_RATIO cannot be blank')
    parser.add_argument('LDL_HDL_RATIO', help=' LDL_HDL_RATIO cannot be blank')
    parser.add_argument('VLDL_CHOLESTEROL', help=' VLDL_CHOLESTEROL cannot be blank')
    parser.add_argument('NON_HDL_CHOLESTEROL', help=' NON_HDL_CHOLESTEROL cannot be blank')
    parser.add_argument('TOTAL_TRIIODOTHYRONINE', help=' TOTAL_TRIIODOTHYRONINE cannot be blank')
    parser.add_argument('TOTAL_THYROXINE', help=' TOTAL_THYROXINE cannot be blank')
    parser.add_argument('THYROID_STIMULATING_HORMONE', help=' THYROID_STIMULATING_HORMONE cannot be blank')
    parser.add_argument('BLOOD_UREA_NITROGEN', help=' BLOOD_UREA_NITROGEN cannot be blank')
    parser.add_argument('CREATININE_SERUM', help=' CREATININE_SERUM cannot be blank')
    parser.add_argument('BUN_SR_CREATININE_RATIO', help=' BUN_SR_CREATININE_RATIO cannot be blank')
    parser.add_argument('CALCIUM', help=' CALCIUM cannot be blank')
    parser.add_argument('URIC_ACID', help=' URIC_ACID cannot be blank')
    parser.add_argument('EST_GLOMERULAR_FILTRATION_RATE', help=' EST_GLOMERULAR_FILTRATION_RATE cannot be blank')



    @jwt_required
    def get(self,user_id):
        #lowrange = LabReportModel.Compare_IRON()
        #print(lowrange)
        labreport = LabReportModel.find_by_id(user_id)
        if labreport:
            return labreport.json()
#        return {'message': 'Item not found' }, 404
        #return lowrange



    @jwt_required
    def put (self,user_id):
        data =  LabReport.parser.parse_args()
        labreport = LabReportModel.find_by_id(user_id)
        if labreport:
            labreport.HPLC = data['HPLC']
            labreport.AVERAGE_BLOOD_GLUCOSE = data['AVERAGE_BLOOD_GLUCOSE']
            labreport.TOTAL_LEUCOCYTES_COUNT  = data['TOTAL_LEUCOCYTES_COUNT']
            labreport.NEUTROPHILS = data['NEUTROPHILS']
            labreport.LYMPHOCYTE_PERCENTAGE = data['LYMPHOCYTE_PERCENTAGE']
            labreport.MONOCYTES = data['MONOCYTES']
            labreport.EOSINOPHILS = data['EOSINOPHILS']
            labreport.BASOPHILS = data['BASOPHILS']
            labreport.IMMATURE_GRANULOCYTE_PERCENTAGE = data['IMMATURE_GRANULOCYTE_PERCENTAGE']
            labreport.NEUTROPHILS_ABSOLUTE_COUNT = data['NEUTROPHILS_ABSOLUTE_COUNT']
            labreport.LYMPHOCYTES_ABSOLUTE_COUNT = data['LYMPHOCYTES_ABSOLUTE_COUNT']
            labreport.MONOCYTES_ABSOLUTE_COUNT = data['MONOCYTES_ABSOLUTE_COUNT']
            labreport.BASOPHILS_ABSOLUTE_COUNT = data['BASOPHILS_ABSOLUTE_COUNT']
            labreport.EOSINOPHILS_ABSOLUTE_COUNT = data['EOSINOPHILS_ABSOLUTE_COUNT']
            labreport.IMMATURE_GRANULOCYTES = data['IMMATURE_GRANULOCYTES']
            labreport.TOTAL_RBC = data['TOTAL_RBC']
            labreport.NUCLEATED_RED_BLOOD_CELLS = data['NUCLEATED_RED_BLOOD_CELLS']
            labreport.HEMOGLOBIN = data['HEMOGLOBIN']
            labreport.HEMATOCRIT = data['HEMATOCRIT']
            labreport.MEAN_CORPUSCULAR_VOLUME = data['MEAN_CORPUSCULAR_VOLUME']
            labreport.MEAN_CORPUSCULAR_HEMOGLOBIN = data['MEAN_CORPUSCULAR_HEMOGLOBIN']
            labreport.MEAN_CORP_HEMO_CONC = data['MEAN_CORP_HEMO_CONC']
            labreport.RED_CELL_DISTRIBUTION_WIDTH_SD = data['RED_CELL_DISTRIBUTION_WIDTH_SD']
            labreport.RED_CELL_DISTRIBUTION_WIDTH_CV = data['RED_CELL_DISTRIBUTION_WIDTH_CV']
            labreport.PLATELET_DISTRIBUTION_WIDTH = data['PLATELET_DISTRIBUTION_WIDTH']
            labreport.MEAN_PLATELET_VOLUME = data['MEAN_PLATELET_VOLUME']
            labreport.PLATELET_COUNT = data['PLATELET_COUNT']
            labreport.PLATELET_TO_LARGE_CELL_RATIO = data['PLATELET_TO_LARGE_CELL_RATIO']
            labreport.PLATELETCRIT = data['PLATELETCRIT']
            labreport.ARSENIC = data['ARSENIC']
            labreport.CADMIUM = data['CADMIUM']
            labreport.MERCURY = data['MERCURY']
            labreport.LEAD = data['LEAD']
            labreport.CHROMIUM = data['CHROMIUM']
            labreport.BARIUM = data['BARIUM']
            labreport.COBALT = data['COBALT']
            labreport.CAESIUM = data['CAESIUM']
            labreport.THALLIUM = data['THALLIUM']
            labreport.URANIUM = data['URANIUM']
            labreport.STRONTIUM = data['STRONTIUM']
            labreport.ANTIMONY = data['ANTIMONY']
            labreport.TIN = data['TIN']
            labreport.MOLYBDENUM = data['MOLYBDENUM']
            labreport.SILVER = data['SILVER']
            labreport.VANADIUM = data['VANADIUM']
            labreport.BERYLLIUM = data['BERYLLIUM']
            labreport.BISMUTH = data['BISMUTH']
            labreport.SELENIUM = data['SELENIUM']
            labreport.ALUMINIUM = data['ALUMINIUM']
            labreport.NICKEL = data['NICKEL']
            labreport.MANGANESE = data['MANGANESE']
            labreport.HOMOCYSTEINE = data['HOMOCYSTEINE']
            labreport.CYSTATIN_C = data['CYSTATIN_C']
            labreport.LIPOPROTEIN = data['LIPOPROTEIN']
            labreport.VITAMIN_B = data['VITAMIN_B']
            labreport.APOLIPOPROTEIN_A_APOA = data['APOLIPOPROTEIN_A_APOA']
            labreport.APOLIPOPROTEIN_B_APOB = data['APOLIPOPROTEIN_B_APOB']
            labreport.APOB_APOA_RATIO = data['APOB_APOA_RATIO']
            labreport.HSCRP = data['HSCRP']
            labreport.SERUM_COPPER = data['SERUM_COPPER']
            labreport.SERUM_ZINC = data['SERUM_ZINC']
            labreport.TESTOSTERONE = data['TESTOSTERONE']
            labreport.IRON = data['IRON']
            labreport.TOTAL_IRON_BINDING_CAPACITY = data['TOTAL_IRON_BINDING_CAPACITY']
            labreport.TRANSFERRIN_SATURATION = data['TRANSFERRIN_SATURATION']
            labreport.ALKALINE_PHOSPHATASE = data['ALKALINE_PHOSPHATASE']
            labreport.BILIRUBIN_TOTAL = data['BILIRUBIN_TOTAL']
            labreport.BILIRUBIN_DIRECT = data['BILIRUBIN_DIRECT']
            labreport.BILIRUBIN_INDIRECT = data['BILIRUBIN_INDIRECT']
            labreport.GAMMA_GLUTAMYL_TRANSFERASE = data['GAMMA_GLUTAMYL_TRANSFERASE']
            labreport.ASPARTATE_AMINOTRANSFERASE = data['ASPARTATE_AMINOTRANSFERASE']
            labreport.ALANINE_TRANSAMINASE = data['ALANINE_TRANSAMINASE']
            labreport.PROTEIN_TOTAL = data['PROTEIN_TOTAL']
            labreport.ALBUMIN_SERUM = data['ALBUMIN_SERUM']
            labreport.SERUM_ALB = data['SERUM_ALB']
            labreport.SERUM_GLOBULIN = data['SERUM_GLOBULIN']
            labreport.TOTAL_CHOLESTEROL = data['TOTAL_CHOLESTEROL']
            labreport.HDL_CHOLESTEROL_DIRECT = data['HDL_CHOLESTEROL_DIRECT']
            labreport.LDL_CHOLESTEROL_DIRECT = data['LDL_CHOLESTEROL_DIRECT']
            labreport.TRIGLYCERIDES = data['TRIGLYCERIDES']
            labreport.TC_HDL_CHOLESTEROL_RATIO = data['TC_HDL_CHOLESTEROL_RATIO']
            labreport.LDL_HDL_RATIO = data['LDL_HDL_RATIO']
            labreport.VLDL_CHOLESTEROL = data['VLDL_CHOLESTEROL']
            labreport.NON_HDL_CHOLESTEROL = data['NON_HDL_CHOLESTEROL']
            labreport.TOTAL_TRIIODOTHYRONINE = data['TOTAL_TRIIODOTHYRONINE']
            labreport.TOTAL_THYROXINE = data['TOTAL_THYROXINE']
            labreport.THYROID_STIMULATING_HORMONE = data['THYROID_STIMULATING_HORMONE']
            labreport.BLOOD_UREA_NITROGEN = data['BLOOD_UREA_NITROGEN']
            labreport.CREATININE_SERUM = data['CREATININE_SERUM']
            labreport.BUN_SR_CREATININE_RATIO = data['BUN_SR_CREATININE_RATIO']
            labreport.CALCIUM = data['CALCIUM']
            labreport.URIC_ACID = data['URIC_ACID']
            labreport.EST_GLOMERULAR_FILTRATION_RATE = data['EST_GLOMERULAR_FILTRATION_RATE']


        else:

            labreport = LabReportModel(user_id, **data)

        labreport.save_to_db()

        return labreport.json(),201
    @jwt_required
    def delete(self, user_id):
        labreport = LabReportModel.find_by_id(user_id)
        if labreport:
            labreport.delete_from_db()
            return {'message': 'Item deleted successfully.'}

        return {'message': ' Item Not Found'}
