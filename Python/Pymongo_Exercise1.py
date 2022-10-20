from pymongo import MongoClient
import json
import pandas as pd
import numpy as np

def mongoimport(csv_path):

    hr_df=pd.read_csv(csv_path)
    payload=json.loads(hr_df.to_json(orient='records'))
    collection.delete_many({})
    
    collection.insert_many(payload)
    
if __name__ == "__main__":
    client=MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['HRdatabase1']
    collection=db['EmpCollection']
    mongoimport('D:/Pymongo/HR-Employee-Attrition.csv')
    
    #1
    allDocuments=collection.aggregate([{'$group':{'_id':'$Department','Employeecount':{'$count':{}}}},{ '$sort' : { 'Employeecount' : -1 }},{'$limit':1}])
    for item in allDocuments:
        print(item)

    #2
    allDocuments3=collection.aggregate([{'$group':{'_id':'$EducationField','Totalcount':{'$count':{}}}},{ '$sort' : { 'Totalcount' : -1 }},{'$limit':1}])
    for item in allDocuments3:
        print(item)
    #3
    allDocuments2=collection.aggregate([{'$group':{'_id':'null','minincome':{'$min':'$Income'},'maxincome':{'$max':'$Income'}}},{ '$project' : { '_id' : 0 ,}}])
    for i in allDocuments2:
        print(i)
        
    #4
    average_sal=collection.aggregate([{'$group':{'_id':'null','averageamount':{'$avg':'$MonthlyIncome'}}},{ '$project' : { '_id' : 0 }}])
    for i in average_sal:
        print(i)
    #5
    allDocuments5=collection.aggregate([{'$group':{'_id':'null','average':{'$avg':'$PercentSalaryHike'}}},{ '$project' : { '_id' : 0 }}])
    for i in allDocuments5:
        i['average'] = np.round(i['average'], 2)
        print(i)

    
    #6
    allDocuments7=collection.aggregate([{'$match':{ 'Attrition' : { '$eq' :'Yes'}}},{'$group':{'_id':'null','average_of_resigned':{'$avg':'$PercentSalaryHike'}}},{ '$project' : { '_id' : 0 }}])
    for i in allDocuments7:
        i['average_of_resigned'] = np.round(i['average_of_resigned'], 2)
        print(i)
    
    #7
    allDocuments8=collection.aggregate([{'$match':{ 'Attrition':'Yes'}},{'$group':{'_id':'$Department','count':{'$count':{}}}},{ '$sort' : { 'count' : -1 }},{'$limit':1}])
    for i in allDocuments8:
        print(i)
    #8
    emp_qualification = collection.aggregate([
       {'$match':{'EducationField':{'$lte' : 'avg_sal'}}},
       {'$group' : {'_id' : '$EducationField', 'avg_sal':{ '$avg' : '$MonthlyIncome'}}},
       ])
   
    for item in emp_qualification:
        print(item)
        
    