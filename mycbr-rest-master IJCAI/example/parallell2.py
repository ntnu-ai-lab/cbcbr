from requests import get
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from IPython.display import HTML
import pyodbc


from pandas.io.json import json_normalize

from mycbr_py_api import MyCBRRestApi as mycbr

server = 'localhost'

port = '8080'
base_url = 'http://' + server + ':' + port + '/'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

obj = mycbr(base_url)
res=obj.getAllCases()
def retrieve_c_att(case,k):
    raw = pd.DataFrame(requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/amalgamationFunctions/default function/retrievalByMultipleAttributes?k='+str(k), json={'Municipality':case['Municipality'],'IndustrySubgroupCode':case['IndustrySubgroupCode'],'IndustryMainAreaCode':case['IndustryMainAreaCode'], 'ProbabilityForNonComplianceGivenControlPointandMunicipality':70,
    'ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup':70,'NumberofNonComplianceGivenControlPointandMunicipality':70,'NumberofNonComplianceGivenControlPointandIndustrySubgroup':70}).json()) 
    results = raw.apply(pd.to_numeric, errors='coerce').fillna(raw).sort_values(by='similarity', ascending=False)
    results['similarity'] = results['similarity'].astype(float)
    results['NonCompliance'] = results['NonCompliance'].astype(int)
    returned_df = results.apply(pd.to_numeric, errors='coerce').fillna(results)
    return results
def retrieve_c_att2(case,k):
    results = res.copy()
    results=results.loc[(results['Municipality']==case['Municipality']) & (results['IndustrySubgroupCode']==case['IndustrySubgroupCode'])]
    results['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup'] = results['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup'].astype(int)
    results['ProbabilityForNonComplianceGivenControlPointandMunicipality'] = results['ProbabilityForNonComplianceGivenControlPointandMunicipality'].astype(int)
    results['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup']=(results['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup']+results['ProbabilityForNonComplianceGivenControlPointandMunicipality'])/2
    results=results.sort_values(by='ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup', ascending=False)
    results=results.head(k)
    #results=results.loc[(results['ProbabilityForNonComplianceGivenControlPointandMunicipality']>=25) & (results['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup']>=25)]
    #predicted positive<=>in checklist
    results['NonCompliance'] = results['NonCompliance'].astype(int)
    return results
def retrieve_c_att22(case,k):
    raw = pd.DataFrame(requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/amalgamationFunctions/default function/retrievalByMultipleAttributes?k='+str(k), json={'IndustryAreaCode':case['IndustryAreaCode'],'IndustryGroupCode':case['IndustryGroupCode'],'IndustryCode':case['IndustryCode'],'MunicipalityNumber':case['MunicipalityNumber'],'IndustrySubgroupCode':case['IndustrySubgroupCode'],'IndustryMainAreaCode':case['IndustryMainAreaCode'],
   'Fylke':case['Fylke']},headers=headers).json())
    #print(case)
    results = raw.apply(pd.to_numeric, errors='coerce').fillna(raw).sort_values(by='similarity', ascending=False)
    results['similarity'] = results['similarity'].astype(float)
    results['NonCompliance'] = results['NonCompliance'].astype(int)
    returned_df = results.apply(pd.to_numeric, errors='coerce').fillna(results)
    #results=results.head(k)
    return results
#Retrieve all control points
def retrieve_c_att3(case,k):
    raw = pd.DataFrame(requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/amalgamationFunctions/default function/retrievalByMultipleAttributes?k='+str(k), json={'Kommune':case['Kommune'],'NaringsUndergruppeKode':case['NaringsUndergruppeKode'],'NaringshovedomradeKode':case['NaringshovedomradeKode'],'SannsynlighetForBruddGittKPogNaringKommune':70,'AntBruddGittKPogNaringKommune':70}).json()) 
    raw['similarity'] = raw['similarity'].astype(float)
    results = raw.apply(pd.to_numeric, errors='coerce').fillna(raw).sort_values(by='similarity', ascending=False)
    results['AntallBrudd'] = results['AntallBrudd'].astype(int)
    returned_df = results.apply(pd.to_numeric, errors='coerce').fillna(results)
    return results

def retrieve_c_att4(case,k):
    raw = pd.DataFrame(requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/amalgamationFunctions/default function/retrievalByMultipleAttributes?k='+str(k), json={'Municipality':case['Municipality'],'IndustrySubgroupCode':case['IndustrySubgroupCode'],'IndustryMainAreaCode':case['IndustryMainAreaCode'], 'ProbabilityForNonComplianceGivenControlPointandMunicipality':90,
    'ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup':90,'NumberOfNonComplianceGivenControlPointandMunicipality':70,'NumberOfNonComplianceGivenControlPointandIndustrySubgroup':70}).json()) 
    results = raw.apply(pd.to_numeric, errors='coerce').fillna(raw).sort_values(by='similarity', ascending=False)
    results['similarity'] = results['similarity'].astype(float)
    results['NonCompliance'] = results['NonCompliance'].astype(int)
    returned_df = results.apply(pd.to_numeric, errors='coerce').fillna(results)
    return results
def retrieve_c_att5(case,k):
    raw = pd.DataFrame(requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/amalgamationFunctions/default function/retrievalByMultipleAttributes?k='+str(k), json={'Municipality':case['Municipality'],'IndustrySubgroupCode':case['IndustrySubgroupCode'],'IndustryMainAreaCode':case['IndustryMainAreaCode']}).json()) 
    results = raw.apply(pd.to_numeric, errors='coerce').fillna(raw).sort_values(by='similarity', ascending=False)
    results['similarity'] = results['similarity'].astype(float)
    results['NonCompliance'] = results['NonCompliance'].astype(int)
    returned_df = results.apply(pd.to_numeric, errors='coerce').fillna(results)
    return results

def retrieve_c_att6(case,k):
    raw = pd.DataFrame(requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/amalgamationFunctions/default function/retrievalByMultipleAttributes?k='+str(k), json={'Municipality':case['Municipality'],'IndustrySubgroupCode':case['IndustrySubgroupCode'],'IndustryMainAreaCode':case['IndustryMainAreaCode'], 
    'ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup':70,'NumberOfNonComplianceGivenControlPointandIndustrySubgroup':70}).json()) 
    results = raw.apply(pd.to_numeric, errors='coerce').fillna(raw).sort_values(by='similarity', ascending=False)
    results['similarity'] = results['similarity'].astype(float)
    results['NonCompliance'] = results['NonCompliance'].astype(int)
    returned_df = results.apply(pd.to_numeric, errors='coerce').fillna(results)
    return results
    
initCBCopy=obj.getAllCases();
currentCBCopy=obj.getAllCases();
#Add multiple contorl points to the case base
def addManyCases(cases):
    cases=cases.to_dict('records')
    rec={'cases':cases}
    #print(rec)
    #structure of case dictionary must be {'cases':[{'IndustrySubgroupCode':45.2},{"Municipality":"Amik"}]}
    #NB! int values must be formatted as strings
    results=requests.post(url=base_url + 'concepts/KP/casebases/CB_csvImport/cases', json=rec,headers={'Accept': 'application/json'})
    return results
#Fill casebase in case its empty
def fillCaseBase(year):
    # Specifying the ODBC driver, server name, database, etc. directly
    cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=RisikoIndeksTjenesten;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    traindateid=" where (InspectionDateId<"+str(year)+"0101 or InspectionDateId>="+str(year+1)+"0101) and InspectionDateId<20190601"
    testdateid=" where InspectionDateId>="+str(year)+"0101 and InspectionDateId<"+str(year+1)+"0101 and InspectionDateId<20190601"
    cases=pd.read_sql("SELECT  [MuncipalityIndex] as MunicipalityIndex ,[IndustrySubgroupCodeIndex],[IndustryGroupCode],[IndustryAreaCode],[IndustryCode],[Fylke],[MunicipalityNumber],  [InspectionId] as 'InspectionId' ,[IndustryMainAreaCode],ControlPointText,[IndustrySubgroupCode],[Municipality],[NonCompliance]"
+",round(isNull(SannsynlighetForBruddGittKPogKommune,(1.0/(6.0+isNull(tttg2,0))))*100,0) as ProbabilityForNonComplianceGivenControlPointandMunicipality"
+",round(isNull(SannsynlighetForBruddGittKPogNaring,(1.0/(6.0+isNull(tttg,0))))*100,0) as ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup"
+",round(isNull(AntBruddGittKPogNaring,0),0) as NumberOfNonComplianceGivenControlPointandIndustrySubgroup"
+",round(isNull(AntBruddGittKPogKommune,0),0) as NumberOfNonComplianceGivenControlPointandMunicipality"
                      +" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]"
+" Left join(Select ( (Convert(real,isNull(Count(IndustrySubgroupCode),0))+1.0)/(AVG(Convert(real, Kommune3))+6.0))  as SannsynlighetForBruddGittKPogNaring,Count(IndustrySubgroupCode) as AntBruddGittKPogNaring,ControlPointText as KPT2, IndustrySubgroupCode as Nugk"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]"  
+" join (Select Count(IndustrySubgroupCode) as Kommune3 , ControlPointText as KT2, IndustrySubgroupCode as Kom"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]"+traindateid+"  group by ControlPointText, IndustrySubgroupCode) as a on a.Kom=IndustrySubgroupCode and ControlPointText=KT2" 
+" join (Select Count(Municipality) as Kommune5 ,  max(NonCompliance) as AntB2"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]" +traindateid+") as c on c.AntB2=NonCompliance"
                    +traindateid
+" group by ControlPointText, NonCompliance, IndustrySubgroupCode) as b on b.KPT2=ControlPointText and b.Nugk=IndustrySubgroupCode"
+" Left join(Select ( (Convert(real,isNull(Count(Municipality),0))+1.0)/(AVG(Convert(real, Kommune3))+6.0))  as SannsynlighetForBruddGittKPogKommune,Count(Municipality) as AntBruddGittKPogKommune, ControlPointText as KPT, Municipality as KOMM"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb] join (Select Count(Municipality) as Kommune3 , ControlPointText as KT2, Municipality as Kom"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]"+traindateid+" group by ControlPointText, Municipality) as a on a.Kom=Municipality and ControlPointText=KT2" 
+" join (Select Count(Municipality) as Kommune5 ,  max(NonCompliance) as AntB2"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]" +traindateid+") as c on c.AntB2=NonCompliance"
                    +traindateid+"  group by ControlPointText, NonCompliance, Municipality) as a on a.KOMM=Municipality and a.KPT=ControlPointText"
+" left join(Select Count(IndustrySubgroupCode) as tttg , ControlPointText as KT10, IndustrySubgroupCode as Kom10"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]"+traindateid+" group by ControlPointText, IndustrySubgroupCode) as z on z.Kom10=IndustrySubgroupCode and ControlPointText=z.KT10" 
+" left join(Select Count(Municipality) as tttg2 , ControlPointText as KT10, Municipality as NUG10"
+" FROM [RisikoIndeksTjenesten].[dbo].[BayesianDynamicChecklistLocalDb]"+traindateid+" group by ControlPointText, Municipality) as zz on ControlPointText=zz.KT10 and zz.NUG10=Municipality" 
+testdateid
                      +" Order by InspectionDateId",cnxn)
    #print(cases)
    cases['NonCompliance']= cases['NonCompliance'].map(str)
    cases['NumberOfNonComplianceGivenControlPointandIndustrySubgroup']= cases['NumberOfNonComplianceGivenControlPointandIndustrySubgroup'].map(str)
    cases['NumberOfNonComplianceGivenControlPointandMunicipality']= cases['NumberOfNonComplianceGivenControlPointandMunicipality'].map(str)
    cases['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup']= cases['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup'].astype(int)
    cases['ProbabilityForNonComplianceGivenControlPointandMunicipality']= cases['ProbabilityForNonComplianceGivenControlPointandMunicipality'].astype(int)
    cases['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup']= cases['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup'].map(str)
    cases['ProbabilityForNonComplianceGivenControlPointandMunicipality']= cases['ProbabilityForNonComplianceGivenControlPointandMunicipality'].map(str)
    cases['IndustrySubgroupCodeIndex']= cases['IndustrySubgroupCodeIndex'].map(str)
    cases['MunicipalityIndex']= cases['MunicipalityIndex'].map(str)
    cases['InspectionId']=cases['InspectionId'].apply(int)+0
    cases['InspectionId']= cases['InspectionId'].map(str)
    cases['MunicipalityNumber']= cases['MunicipalityNumber'].map(str)
    cases['IndustryAreaCode']= cases['IndustryAreaCode'].map(str)
    cases['IndustryCode']= cases['IndustryCode'].map(str)
    cases['IndustryCode']=cases['IndustryCode'].replace(to_replace=r',', value='.', regex=True)
    #print(cases['InspectionId'])
    return addManyCases(cases)
#Delete all control points from the case base
def deleteAllCases():
    final_urli = base_url + '/concepts/KP/casebases/CB_csvImport/cases/'
    response = requests.delete( url= final_urli)
    return response

#Updates casebase with the current set of cases (currentCBCopy)
def updateCaseBaseProb(cases):
    deleteAllCases()
    cases['NonCompliance']= cases['NonCompliance'].map(str)
    cases['NumberOfNonComplianceGivenControlPointandIndustrySubgroup']= cases['NumberOfNonComplianceGivenControlPointandIndustrySubgroup'].map(str)
    cases['NumberOfNonComplianceGivenControlPointandMunicipality']= cases['NumberOfNonComplianceGivenControlPointandMunicipality'].map(str)
    cases['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup']= cases['ProbabilityForNonComplianceGivenControlPointandIndustrySubgroup'].map(str)
    cases['ProbabilityForNonComplianceGivenControlPointandMunicipality']= cases['ProbabilityForNonComplianceGivenControlPointandMunicipality'].map(str)
    cases['IndustrySubgroupCodeIndex']= cases['IndustrySubgroupCodeIndex'].map(str)
    cases['MunicipalityIndex']= cases['MunicipalityIndex'].map(str)
    cases['InspectionId']=cases['InspectionId'].apply(int)+0
    cases['InspectionId']= cases['InspectionId'].map(str)
    cases['MunicipalityNumber']= cases['MunicipalityNumber'].map(str)
    cases['IndustryAreaCode']= cases['IndustryAreaCode'].map(str)
    cases['IndustryCode']= cases['IndustryCode'].map(str)
    cases['IndustryCode']=cases['IndustryCode'].replace(to_replace=r',', value='.', regex=True)

    cases=cases.drop(columns=[ 'caseID'])
    res=addManyCases(cases)
    return res;



#Restores the casebase back to it's original form
def restoreOriginalCaseBase(year):
    deleteAllCases()
    fillCaseBase(year)
    #return res;

#if len(res)==0:
 #   fillCaseBase(2019)
 
#TODO: Use the actual ground truth labels also, not only calculate matches with the validation base.
#TODO: Need to make precision (gt), recall (gt)... precision, recall by average pr control point instead of counting. Number of observations in validation base varies and we get bias.
#Prec(gt)=average precision (precision calculated by counting number of retrieved control points that both exists and are positive in the original checklist)
#Divide by number of retrieved control points that also exists in the original checklist
#Prec(val)=average precision pr control point (precision calculated from validation set by matching munc/ind from inspection)
#Prec(cp)=average precision pr control point (precision calculated from validation set by matching munc/ind from retrieved control point)
initCBCopy=obj.getAllCases();
currentCBCopy=initCBCopy
for ik in range(2013,2020):
    fh2=open("Log_" + "CBRChecklists"+str(ik) + '.txt', 'w+')
    if len(initCBCopy)==0:
        fillCaseBase(ik)
        initCBCopy=obj.getAllCases()
        currentCBCopy=initCBCopy
    else:
        restoreOriginalCaseBase(ik)
        initCBCopy=obj.getAllCases()
        currentCBCopy=initCBCopy
    noncompliance=0 #true positive(gt)
    controlpoints=0 #predicted positive(gt)
    noncompliancengt=0 #true positive (ngt)
    controlpointsngt=0#predicted positive (ngt)
    falsepositivegt=0
    falsepositivengt=0
    precisionval=0
    recallval=0
    accuracyval=0
    precision=0
    precisiongt=0
    lengthprecgt=0
    recall=0
    accuracy=0
    lengthprec=0.00001
    lengthvalprec=0
    lengthrec=0.00001
    lengthvalrec=0
    lengthacc=0.00001
    lengthvalacc=0
    truenegative=0
    falsenegative=0
    similarity=0
    counter=0
    Kcp=15
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    noncompliantInspection=0
    numberofOverlappingControlpoints=0
    inspections=obj.getAllCases().drop_duplicates(subset = ["InspectionId"])
    cases=obj.getAllCases()
    cases["NonCompliance"]=cases["NonCompliance"].astype(int)
    casestest=len(cases.drop_duplicates(subset = ["ControlPointText"]))
    cpCases=list()
    negatives=list()
    cltotallen=0
    inspectionstot=0
    precchecklists=0
    recchecklists=0
    accchecklists=0
    precchecklistsval=0
    recchecklistsval=0
    accchecklistsval=0
    print(casestest)
    for ind, case in inspections.iterrows():

        inspectionstot+=1
        uniquechecklistlengthval=0
        cpCases=list()
        counter+=1
        if counter>500:
            counter=0
            print(ind)
            
        r=0#Stop variable to ensure at least 10 cases are selected for each inspection (case)
        k=500#Finding the Top K cases
        existingChecklist=cases[cases['InspectionId']==case['InspectionId']]#Retrieve the existing checklist
        clck=cases[cases["IndustrySubgroupCode"].astype(float)==float(case["IndustrySubgroupCode"])]
        clck=clck[clck["MunicipalityNumber"].astype(int)==int(case["MunicipalityNumber"])]
        clck["NonCompliance"]=clck["NonCompliance"].astype(float)
        negatives=clck
        if len(clck)>0:
            caseAvgNoncompliancePrControlpoint=clck.groupby(["ControlPointText"],as_index=False).mean()

            #print(caseAvgNoncompliancePrControlpoint)
        while r==0:
            checklist=retrieve_c_att22(case,k)#Retrieve control points that matches each inspection (input case). checklist=CL from paper

            #caseAvgNoncompliancePrControlpoint=checklist.groupby(["ControlPointText"],as_index=False).mean()#FIX THIS
            #Find the mean value of each column in the returned data set of control points. 
            #The mean values are grouped by each unique control point, such that each solution s(non-compliance) is reassigned
            uniqueChecklist=checklist.drop_duplicates(subset = ["ControlPointText"])#Find all unique control points by removing duplicates
            uniqueChecklist=uniqueChecklist.head(Kcp)
            if len(uniqueChecklist)>(Kcp-1):#Check if there are at least 10 unique control points
                truepositive=0
                truepositiveval=0
                r=1#Stops the while loop since 10 unique control points are found
                #controlpoints+=len(uniqueChecklist) 
                #Record statistics. Add to the total, the number of unique control points that were found in current generated checklist. 
                #noncompliance+=caseAvgNoncompliancePrControlpoint["NonCompliance"].sum() 
                similarity+=uniqueChecklist["similarity"].sum() 
                #Record statistics. Add the ratio/fraction of non-compliance for each of the (unique) control point in the checklist.
                #noncompliancesum=caseAvgNoncompliancePrControlpoint["NonCompliance"].sum()
                #if noncompliancesum>=1:
                #    noncompliantInspection+=1#Record statistics. Count if the sum of non-compliance is >=1

                for ind2, generatedChecklistControlpoint in uniqueChecklist.iterrows():#Find overlap between the existing and new generated checklist
                    cltotallen+=1
                    negatives=negatives[negatives["ControlPointText"]!=generatedChecklistControlpoint["ControlPointText"]]#This is wrong. Negatives need to be outside the whole checklist
                    excp=existingChecklist[existingChecklist["ControlPointText"]==generatedChecklistControlpoint["ControlPointText"]]
                    if len(excp)>0:
                        numberofOverlappingControlpoints+=1 
                        precisiongt+=((excp["NonCompliance"].sum())/len(excp["NonCompliance"]))
                        lengthprecgt+=1
                        controlpoints+=1#matchlen
                        

                    caseAvgNoncompliancePrControlpoint2=caseAvgNoncompliancePrControlpoint[caseAvgNoncompliancePrControlpoint["ControlPointText"]==generatedChecklistControlpoint["ControlPointText"]]
                    #print("clck: "+str(len(clck[clck["ControlPointText"]==generatedChecklistControlpoint["ControlPointText"]])))
                    #print(caseAvgNoncompliancePrControlpoint)
                    #print("avg: "+ str(len(caseAvgNoncompliancePrControlpoint2)))
                    
                    summ2=caseAvgNoncompliancePrControlpoint2["NonCompliance"].sum() 
                    if len(caseAvgNoncompliancePrControlpoint2["NonCompliance"])>0:
                        noncompliance+=(summ2/len(caseAvgNoncompliancePrControlpoint2["NonCompliance"]))
                        truepositiveval+=(summ2/len(caseAvgNoncompliancePrControlpoint2["NonCompliance"]))
                    
                    matchlen=len(caseAvgNoncompliancePrControlpoint2["NonCompliance"])
                    if matchlen>1:
                        print(caseAvgNoncompliancePrControlpoint2["NonCompliance"])
                    controlpointsngt+=1
                    falsepositivegt+=(matchlen-summ2)
                    if matchlen>0:
                        #precisionval+=(summ2/matchlen)
                        lengthvalprec+=1
                        uniquechecklistlengthval+=1
                    summ3=0
                    if matchlen==0:#if validation record of checklist control point does not exist
                        cpCases=cases[cases["IndustrySubgroupCode"].astype(float)==float(generatedChecklistControlpoint["IndustrySubgroupCode"])]
                        cpCases=cpCases[cpCases["MunicipalityNumber"].astype(int)==int(generatedChecklistControlpoint["MunicipalityNumber"])]
                        cpCases=cpCases[cpCases["ControlPointText"]==generatedChecklistControlpoint["ControlPointText"]]
                        cpCases["NonCompliance"]=cpCases["NonCompliance"].astype(float)
                        summ3=cpCases["NonCompliance"].sum()
                        
                        
                        falsepositivengt+=(len(cpCases["NonCompliance"])-summ3)
                        if len(cpCases["NonCompliance"])>0:
                            noncompliancengt+=(summ3/len(cpCases["NonCompliance"]))
                            truepositive+=(summ3/len(cpCases["NonCompliance"]))
                            #precision+=(summ3/len(cpCases["NonCompliance"]))
                            #lengthprec+=1
                        
                        #cpCases["NonCompliance"]=cpCases["NonCompliance"].astype(float)
                 #   summ=0
                #    atruenegative=0
                  #  if len(negatives)>0:
                #        summ=negatives["NonCompliance"].sum()
                  #      falsenegative+=summ
                 #       truenegative+=(len(negatives["NonCompliance"])-summ)
                 #       atruenegative=(len(negatives["NonCompliance"])-summ)
                #    if (summ>0 or summ2>0) and matchlen>0:
                 #       recallval+=((summ2)/(summ2+summ))
                  #      lengthvalrec+=1
                 #   if matchlen>0:
                  #      accuracyval+=((summ2+atruenegative)/(atruenegative+summ+(matchlen))) #matchlen=positives
                #        lengthvalacc+=1

                #    if len(cpCases)>0 and matchlen==0:
               #         if summ3>0 or summ>0:
               #             recall+=(summ3/(summ3+summ))
               #             lengthrec+=1
               #         accuracy+=((summ3+atruenegative)/(atruenegative+len(cpCases["NonCompliance"])+summ))
               #         lengthacc+=1
                    #if noncompliancesum==0 and summ3>=1:
                        #numberofOverlappingControlpoints+=1
                #Calculate statistics on checklists level
                uniquenegatives=len(negatives.drop_duplicates(subset = ["ControlPointText"]))
                negativecpy=negatives.copy()
                negativecpy["NonCompliance"]=negativecpy["NonCompliance"].astype(float)
                groupedby=negativecpy.groupby(["ControlPointText"],as_index=False).count()
                groupedbys=negativecpy.groupby(["ControlPointText"],as_index=False).sum()
                groupedby["NonCompliance"]=groupedbys["NonCompliance"]/groupedby["NonCompliance"]
                uniquecalcnegatives=groupedby.drop_duplicates(subset = ["ControlPointText"])
                noncompliancenegatives=uniquecalcnegatives["NonCompliance"].sum()
                #fnegatives=noncompliancenegatives/uniquenegatives #To avoid selection bias effects
                #negativecpy["NonCompliance"]=negativectpy.groupby(["ControlPointText"],as_index=False)
                #fnegatives=negatives[negatives["NonCompliance"].astype(int)==1]
                #fnegatives=fnegatives["NonCompliance"]
                
                #falsenegativeelement=len(fnegatives)/len(negatives["NonCompliance"])
                falsenegativeelement=0
                if uniquenegatives>0:
                    falsenegativeelement=noncompliancenegatives/uniquenegatives #To avoid selection bias effects
                truenegativeelement=1-falsenegativeelement
                
                truepositivesprchecklistval=(truepositiveval)
                falsepositivesprchecklistval=(uniquechecklistlengthval-truepositivesprchecklistval)
                
                truepositivesprchecklist=(truepositive+truepositiveval)
                falsepositivesprchecklist=(len(uniqueChecklist)-(truepositive+truepositiveval))
                truenegativesprchecklist=truenegativeelement*uniquenegatives
                falsenegativesprchecklist=falsenegativeelement*uniquenegatives
                #len(uniqueChecklist)+uniquenegatives=len(unique control points)
                
                precprchecklist=truepositivesprchecklist/len(uniqueChecklist)
                precchecklists+=precprchecklist
                #print("prec: "+str(precprchecklist))
                precprchecklistval=0
                if uniquechecklistlengthval>0:
                    precprchecklistval=truepositivesprchecklistval/uniquechecklistlengthval
                precchecklistsval+=precprchecklistval
                #print("prec(val): "+str(precprchecklistval))
                #precprchecklistval=truepositive/len(uniqueChecklistval)
                recprchecklist=0
                if (truepositivesprchecklist+falsenegativesprchecklist)>0:
                    recprchecklist=truepositivesprchecklist/(truepositivesprchecklist+falsenegativesprchecklist)
                recchecklists+=recprchecklist
               # print("rec: "+str(recprchecklist))
                recprchecklistval=0
                if (truepositivesprchecklistval+falsenegativesprchecklist)>0:
                    recprchecklistval=truepositivesprchecklistval/(truepositivesprchecklistval+falsenegativesprchecklist)
                recchecklistsval+=recprchecklistval
                #print("rec(val): "+str(recprchecklistval))
                accprchecklist=0
                if (len(uniqueChecklist)+uniquenegatives)>0:
                    accprchecklist=(truepositivesprchecklist+truenegativesprchecklist)/(len(uniqueChecklist)+uniquenegatives)
                accchecklists+=accprchecklist
                #print("acc: "+str(accprchecklist))
                accprchecklistval=0
                if (uniquechecklistlengthval+uniquenegatives)>0:
                    accprchecklistval=(truepositivesprchecklistval+truenegativesprchecklist)/(uniquechecklistlengthval+uniquenegatives)
                accchecklistsval+=accprchecklistval
                #print("acc(val): "+str(accprchecklistval))
                
                
                #|true positives for each checklist|=sum(true positive elements in checklist)
                #|false positives for each checklist|=sum(false positive elements in checklist)
                #|true negatives for each checklist|=|true negative element|*|unique control points(2)|
                #|false negatives for each checklist|=|false negative element|*|unique control points(2)|
                #prec pr checklist
                #rec pr checklist
                #acc pr checklist
                        
            k+=500 #Increment k while there are less then 10 unique control points

        #print(ind)#Printing the case index for each unique inspection just to track progress of execution over time ("Progress bar")
    print("Precision (gt): "+str(precisiongt/lengthprecgt))
    fh2.write("\nPrecision (gt): "+str(precisiongt/lengthprecgt))
    #print("Precision (val): "+str(precisionval/lengthvalprec))
    #fh2.write("\nPrecision (val): "+str(precisionval/lengthvalprec))
    #print("Precision (ngt): "+str(precision/lengthprec))
    #fh2.write("\nPrecision (ngt): "+str(precision/lengthprec))
    #print("Precision: "+str((precision+precisionval)/(lengthprec+lengthvalprec)))
    #fh2.write("\nPrecision: "+str((precision+precisionval)/(lengthprec+lengthvalprec)))
    print("Precision(val): "+str((precchecklistsval)/(inspectionstot)))
    fh2.write("\nPrecision(val): "+str((precchecklistsval)/(inspectionstot)))
    print("Precision: "+str((precchecklists)/(inspectionstot)))
    fh2.write("\nPrecision: "+str((precchecklists)/(inspectionstot)))
    #print("Recall (val): "+str(recallval/(lengthvalrec)))
    #fh2.write("\nRecall (val): "+str(recallval/(lengthvalrec)))
    #print("Recall (ngt): "+str(recall/(lengthrec)))
    #fh2.write("\nRecall (ngt): "+str(recall/(lengthrec)))
    #print("Recall: "+str((recall+recallval)/(lengthrec+lengthvalrec)))
    #fh2.write("\nRecall: "+str((recall+recallval)/(lengthrec+lengthvalrec)))
    print("Recall(val): "+str((recchecklistsval)/(inspectionstot)))
    fh2.write("\nRecall(val): "+str((recchecklistsval)/(inspectionstot)))
    print("Recall: "+str((recchecklists)/(inspectionstot)))
    fh2.write("\nRecall: "+str((recchecklists)/(inspectionstot)))
    #print("Accuracy (val): "+str(accuracyval/(lengthvalacc)))
    #fh2.write("\nAccuracy (val): "+str(accuracyval/(lengthvalacc)))
    #print("Accuracy (ngt): "+str(accuracy/(lengthacc)))
    #fh2.write("\nAccuracy (ngt): "+str(accuracy/(lengthacc)))
    #print("Accuracy: "+str((accuracy+accuracyval)/(lengthacc+lengthvalacc)))
    #fh2.write("\nAccuracy: "+str((accuracy+accuracyval)/(lengthacc+lengthvalacc)))
    print("Accuracy(val): "+str((accchecklistsval)/(inspectionstot)))
    fh2.write("\nAccuracy(val): "+str((accchecklistsval)/(inspectionstot)))
    print("Accuracy: "+str((accchecklists)/(inspectionstot)))
    fh2.write("\nAccuracy: "+str((accchecklists)/(inspectionstot)))
    print("Average number of control points per checklist(gt): "+str(controlpoints/inspectionstot))
    fh2.write("\nAverage number of control points per checklist(gt): "+str(controlpoints/inspectionstot))
    print("Average number of control points per checklist: "+str((controlpointsngt)/inspectionstot))
    fh2.write("\nAverage number of control points per checklist: "+str((controlpointsngt)/inspectionstot))
    print("Average number of non-compliant control points per checklist(gt): "+str(precisiongt/inspectionstot))
    fh2.write("\nAverage number of non-compliant control points per checklist(gt): "+str(precisiongt/inspectionstot))
    print("Average number of non-compliant control points per checklist(val): "+str(noncompliance/inspectionstot))
    fh2.write("\nAverage number of non-compliant control points per checklist(val): "+str(noncompliance/inspectionstot))
    print("Average number of non-compliant control points per checklist: "+str((noncompliance+noncompliancengt)/inspectionstot))
    fh2.write("\nAverage number of non-compliant control points per checklist: "+str((noncompliance+noncompliancengt)/inspectionstot))
    print("Percentage of control points in the intersection between the CBR generated and the original checklists: "+str(numberofOverlappingControlpoints/(cltotallen)))
    fh2.write("\nPercentage of control points in the intersection between the CBR generated and the original checklists: "+str(numberofOverlappingControlpoints/(cltotallen)))
    #number of common control points between CBR generated and original lists divided by the number of control points in the CBR generated list
    #print("Probability for at least 1 control point being non-compliant: "+str(noncompliantInspection/len(inspections)))
    #fh2.write("\nProbability for at least 1 control point being non-compliant: "+str(noncompliantInspection/len(inspections)))
    print("Average similarity: "+str(similarity/(lengthprecgt+lengthvalprec)))
    fh2.write("\nAverage similarity: "+str(similarity/(lengthprecgt+lengthvalprec)))
    fh2.close()