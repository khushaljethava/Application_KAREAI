# Login_Reg

# registration

	POST /registration

	{
	   "username": "Khushal54",
	   "fullname": "Khushal Jethwa",
	   "mobile" : 9662737937,
	   "email" : "Khushaljethwa14@gmail.com",
	   "Gerder" : "Male",
	   "Age" : 22   
	}

	{

# Login


	{
	   "mobile" : 9662737937
	}



# Logout

	POST  /logout/access




# pre_existing_condition

	POST : /preexisting/<int:user_id>
	GET : /preexisting/<int:user_id>
	PUT : /preexisting/<int:user_id>
	DELETE : /preexisting/<int:user_id>

Example :  localhost/preexisting/5,
          localhost/preexisting/453,



	{

	"PC_Race" : 1,
	"PC_Smoking": 1,
	"PC_Alcohol": 1,
	"PC_Diabetes": 1,
	"PC_Hear": 1,
	"PC_Blood_Pressure": 1,
	"PC_Chest_Pain": 1,
	"PC_Stroke": 1,
	"PC_Kidney": 1,
	"PC_Blood_Clot": 1,
	"PC_Metal_implants": 1,
	"PC_Asthma": 1,
	"PC_Cancer": 1,
	"PC_Difficulty_Swallowing": 1,
	"PC_Vascular_Problems": 1,
	"PC_Peripheral_Neuropathy": 1,
	"PC_Weightloss": 1,
	"PC_Double_Vision": 1,
	"PC_Night_Sweats": 1,
	"PC_Night_Pain": 1,
	"PC_Neurologic_Condition": 1,
	"PC_Skin_Disease": 1,
	"PC_Spinal_Cord_Injury": 1,
	"PC_Degenerative_Joint_Disease": 1,
	"PC_Sexual_Dysfunction": 1,
	"PC_Bladder": 1,
	"PC_Groin_Numbness": 1,
	"PC_Ringing_in_Ears": 1,
	"PC_Allergy_to_Latex": 1,
	"PC_Head_Injury": 1,
	"PC_Obesity": 1,
	"PC_Chronic_Pain": 1,
	"PC_Fractures": 1,
	"PC_Infection_Dissease": 1,
	"PC_Fever": 1,
	"PC_Lower_Extremety": 1,
	"PC_Nausea": 1,
	"PC_Arthritis": 1,
	"PC_Osteoporosis": 1,
	"PC_Phsychological_Problems": 1,
	"PC_Seizures": 1,
	"PC_Dizziness": 1,
	"PC_Ringing_in_Ears": 1,
	"PC_Allergy_to_Latex": 1,
	"PC_Head_Injury": 1,
	"PC_Obesity": 1,
	"PC_Chronic_Pain": 1,
	"PC_Fractures": 1,
	"PC_Infection_Dissease": 1,
	"PC_Fever": 1,
	"PC_Lower_Extremety": 1,
	"PC_Nausea": 1
	}


# Family History  
	POST : /familyhistory/<int:user_id>/<string:Member>
	  GET : /familyhistory/<int:user_id>/<string:Member>
	  PUT : /familyhistory/<int:user_id>/<string:Member>
	  DELETE : /familyhistory/<int:user_id>/<string:Member>

	  {
	  "FH_Member": "Mother",
	  "FH_Alcoholism": 1,
	  "FH_Allergies": "1" ,
	  "FH_Anesthesia": 1 ,
	  "FH_Anxiety": 1 ,
	  "FH_Arthritis": 1 ,
	  "FH_Asthma": 1 ,
	  "FH_ADHD": 1 ,
	  "FH_Birth_Defects": 1 ,
	  "FH_Blood_Problem": 1 ,
	  "FH_Bone_Joint_Problems": 1 ,
	  "FH_Breast_Disease": 1 ,
	  "FH_Cancer": "1" ,
	  "FH_Chicken_Pox": 1 ,
	  "FH_Colitis": 1 ,
	  "FH_Depression": 1 ,
	  "FH_Diabetes": 1 ,
	  "FH_ENT_Problems": 1 ,
	  "FH_Eating_Disorders": 1 ,
	  "FH_Eczema": 1 ,
	  "FH_Epilepsy": 1 ,
	  "FH_Fertility": 1 ,
	  "FH_Gallbladder": 1 ,
	  "FH_Gynecology": 1 ,
	  "FH_Fever": 1 ,
	  "FH_Headaches": 1 ,
	  "FH_Heart_Problems": 1 ,
	  "FH_Heart_Attack_Over_60": 1 ,
	  "FH_Heart_Attack_Under_60": 1 ,
	  "FH_Heart_Murmur": 1 ,
	  "FH_Hepatitis": 1 ,
	  "FH_High_Blood_Pressure": 1 ,
	  "FH_High_Cholestorol": 1
	  }

# Lab Reports

POST method is not Available.

	  GET : /labreport/<int:user_id>
	  PUT : /labreport/<int:user_id>
	  DELETE : /labreport/<int:user_id>


Parameters for Put Method


	{
	    "HPLC": 5.9,
	    "AVERAGE_BLOOD_GLUCOSE": 123.0,
	    "TOTAL_LEUCOCYTES_COUNT": 8.3,
	    "NEUTROPHILS": 52.2,
	    "LYMPHOCYTE_PERCENTAGE": 42.8,
	    "MONOCYTES": 3.3,
	    "EOSINOPHILS": 1.3,
	    "BASOPHILS": 0.2,
	    "IMMATURE_GRANULOCYTE_PERCENTAGE": 0.2,
	    "NEUTROPHILS_ABSOLUTE_COUNT": null,
	    "LYMPHOCYTES_ABSOLUTE_COUNT": 3.55,
	    "MONOCYTES_ABSOLUTE_COUNT": 0.27,
	    "BASOPHILS_ABSOLUTE_COUNT": 0.02,
	    "EOSINOPHILS_ABSOLUTE_COUNT": null,
	    "IMMATURE_GRANULOCYTES": null,
	    "TOTAL_RBC": 4.83,
	    "NUCLEATED_RED_BLOOD_CELLS": null,
	    "HEMOGLOBIN": 9.4,
	    "HEMATOCRIT": 37.2,
	    "MEAN_CORPUSCULAR_VOLUME": 77.0,
	    "MEAN_CORPUSCULAR_HEMOGLOBIN": 19.5,
	    "MEAN_CORP_HEMO_CONC": 25.3,
	    "RED_CELL_DISTRIBUTION_WIDTH_SD": 54.5,
	    "RED_CELL_DISTRIBUTION_WIDTH_CV": 19.7,
	    "PLATELET_DISTRIBUTION_WIDTH": 10.8,
	    "MEAN_PLATELET_VOLUME": 10.2,
	    "PLATELET_COUNT": 518.0,
	    "PLATELET_TO_LARGE_CELL_RATIO": 25.6,
	    "PLATELETCRIT": 0.53,
	    "ARSENIC": 0.53,
	    "CADMIUM": 0.53,
	    "MERCURY": 0.53,
	    "LEAD": 0.53,
	    "CHROMIUM": 0.53,
	    "BARIUM": 0.53,
	    "COBALT": 0.53,
	    "CAESIUM": 0.53,
	    "THALLIUM": 0.53,
	    "URANIUM": 0.53,
	    "STRONTIUM": 0.53,
	    "ANTIMONY": 0.53,
	    "TIN": 0.53,
	    "MOLYBDENUM": 0.53,
	    "SILVER": 0.53,
	    "VANADIUM": 0.53,
	    "BERYLLIUM": 0.53,
	    "BISMUTH": 0.53,
	    "SELENIUM": 0.53,
	    "ALUMINIUM": 0.53,
	    "NICKEL": 0.53,
	    "MANGANESE": 0.53,
	    "HOMOCYSTEINE": 0.53,
	    "CYSTATIN C": 0.53,
	    "LIPOPROTEIN": 0.53,
	    "VITAMIN D (TOTAL)": 0.53,
	    "VITAMIN B-12": 0.53,
	    "APOLIPOPROTEIN - A1 (APO-A1)": 0.53,
	    "APOLIPOPROTEIN - B (APO-B)": 0.53,
	    "APO B / APO A1 RATIO (APO B/A1)": 0.53,
	    "HIGH SENSITIVITY C-REACTIVE PROTEIN (HS-CRP)": 0.53,
	    "SERUM COPPER": 0.53,
	    "SERUM ZINC": 0.53,
	    "TESTOSTERONE": 0.53,
	    "IRON": null,
	    "TOTAL_IRON_BINDING_CAPACITY": null,
	    "TRANSFERRIN_SATURATION": null,
	    "ALKALINE_PHOSPHATASE": 129.0,
	    "BILIRUBIN_TOTAL": 0.32,
	    "BILIRUBIN_DIRECT": 0.11,
	    "BILIRUBIN_INDIRECT": 0.21,
	    "GAMMA_GLUTAMYL_TRANSFERASE": null,
	    "ASPARTATE_AMINOTRANSFERASE": null,
	    "ALANINE_TRANSAMINASE": null,
	    "PROTEIN_TOTAL": null,
	    "ALBUMIN_SERUM": 4.1,
	    "SERUM_ALB": -2.0,
	    "SERUM_GLOBULIN": 3.3,
	    "TOTAL_CHOLESTEROL": 153.0,
	    "HDL_CHOLESTEROL_DIRECT": 44.0,
	    "LDL_CHOLESTEROL_DIRECT": 90.0,
	    "TRIGLYCERIDES": 179.0,
	    "TC_HDL_CHOLESTEROL_RATIO": 3.5,
	    "LDL_HDL_RATIO": 2.1,
	    "VLDL_CHOLESTEROL": 35.8,
			LR_HSCRP
	    "NON_HDL_CHOLESTEROL": 109.2,
	    "TOTAL_TRIIODOTHYRONINE": 115.0,
	    "TOTAL_THYROXINE": 11.9,
	    "THYROID_STIMULATING_HORMONE": 1.57,
	    "BLOOD_UREA_NITROGEN": 8.86,
	    "CREATININE_SERUM": 0.72,
	    "BUN_SR_CREATININE_RATIO": 12.31,
	    "CALCIUM": 8.59,
	    "URIC_ACID": 4.8,
	    "EST_GLOMERULAR_FILTRATION_RATE": null
	}





# Lab Reports Upload (pdf upload)

	  POST : /labreportupload/<int:user_id>
	  DELETE : /labreportupload/<int:user_id>


Key: "inputFile"
Value: "File"




# Retina Upload (image upload)
	  GET : /retinaupload/<int:user_id>
	  POST : /retinaupload/<int:user_id>
	  DELETE : /retinaupload/<int:user_id>

Key: "inputFile"
Value: "File"

# Symptoms Checker
 	 GET : /symptomcheck/<int:question_id>
