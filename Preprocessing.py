#!/usr/bin/env python



import pandas as pd
import numpy as np


def main():
	#Read in the datasets
	student_info = pd.read_csv('./data/raw/distance_learning/studentInfo.csv')
	assessments = pd.read_csv('./data/raw/distance_learning/assessments.csv')
	student_assessment = pd.read_csv('./data/raw/distance_learning/studentAssessment.csv')
	student_registration = pd.read_csv('./data/raw/distance_learning/studentRegistration.csv')
	student_assessment = pd.read_csv('./data/raw/distance_learning/studentAssessment.csv')
	vle = pd.read_csv('./data/raw/distance_learning/vle.csv')
	studentVle = pd.read_csv('./data/raw/distance_learning/studentVle.csv')



	#Merge Student and assessment lookups into 2 datasets
	#Student_combine has demographic and class details
	#Assessment_combined has student details merged with asessments
	student_key = ['code_module','code_presentation','id_student']
	student_combined = student_info.merge(student_registration,on=student_key)

	assessment_combined  = student_assessment.merge(assessments, on = 'id_assessment')
	assessment_combined = assessment_combined.merge(student_combined, on = student_key)


	#Writing Files to Processed Directory
	student_combined.to_csv('./data/processed/student_combined.csv',index=None)
	assessment_combined.to_csv('./data/processed/assessment_combined.csv',index=None)


	#Get only Assessments for DDD Module
	ddd_assessments = assessments[(assessments.code_module =='DDD')&(assessments.code_presentation!='2013B')]

	#There are 6 TMA's and an exam.  They are all assigned in sequential order
	ddd_assessments.loc[:,'tma_number']=ddd_assessments.id_assessment%7



	#Create a master dataset for all DDD exam and TMA Scores w demographic info
	ddd_assessment_combined  = student_assessment.merge(ddd_assessments, on = 'id_assessment',how='inner')
	ddd_assessment_combined = ddd_assessment_combined.merge(student_combined, on = student_key)


	#There is 1 final per module, only get that row per student
	ddd_exams = ddd_assessment_combined[ddd_assessment_combined.assessment_type=='Exam']



	#Pivot Out TMA Scores for TMA score Feature
	tma1=ddd_assessment_combined[ddd_assessment_combined.tma_number==1][student_key+['score']]
	tma1.columns=student_key+['tma1']
	tma2=ddd_assessment_combined[ddd_assessment_combined.tma_number==2][student_key+['score']]
	tma2.columns=student_key+['tma2']
	tma3=ddd_assessment_combined[ddd_assessment_combined.tma_number==3][student_key+['score']]
	tma3.columns=student_key+['tma3']
	tma4=ddd_assessment_combined[ddd_assessment_combined.tma_number==4][student_key+['score']]
	tma4.columns=student_key+['tma4']
	tma5=ddd_assessment_combined[ddd_assessment_combined.tma_number==5][student_key+['score']]
	tma5.columns=student_key+['tma5']
	tma6=ddd_assessment_combined[ddd_assessment_combined.tma_number==6][student_key+['score']]
	tma6.columns=student_key+['tma6']

	ddd_exams=ddd_exams.merge(tma1,on=student_key)
	ddd_exams=ddd_exams.merge(tma2,on=student_key)
	ddd_exams=ddd_exams.merge(tma3,on=student_key)
	ddd_exams=ddd_exams.merge(tma4,on=student_key)
	ddd_exams=ddd_exams.merge(tma5,on=student_key)
	ddd_exams=ddd_exams.merge(tma6,on=student_key)
	ddd_exams['tma_average']=ddd_exams[['tma1','tma2','tma3','tma4','tma5','tma6']].sum(axis=1)/6



	#Create a summarized version of the VLE Data for the DDD Module
	vle_join = ['code_module','code_presentation','id_site']
	ddd_vle = vle[(vle.code_module=='DDD')&(vle.code_presentation!='2013B')]
	ddd_student_vle = studentVle.merge(ddd_vle,on=vle_join)
	ddd_student_vle_agg = ddd_student_vle.groupby(student_key+['activity_type']).sum_click.sum().reset_index()
	ddd_vle_summary = pd.pivot_table(ddd_student_vle_agg, values = 'sum_click', index=student_key, columns = 'activity_type').reset_index()


	#Merge with the ddd_exams df
	ddd_exams=ddd_exams.merge(ddd_vle_summary,on=student_key)



	#Write out to file
	ddd_exams.to_csv('./data/processed/ddd_exams.csv',index=None)

if __name__ == "__main__":
	main()




