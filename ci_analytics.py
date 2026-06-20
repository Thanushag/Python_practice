import pandas as pd
import csv
def identifyFailedTests(test_log_file,Component_mapping):
    with open(test_log_file) as file:# Read the header line
       with open(Component_mapping, 'r') as mapping_file:
            mapping_reader = csv.DictReader(mapping_file)
            component_map = {row['ID']: row['TeamOwner'] for row in mapping_reader} 
            data = []
        
            for line in file:
                if(line.__contains__('METRIC')):
                    status = line.split('|')[3].split(':')[1].strip()
                    id=line.split('|')[0].split(':')[1]
                    data.append({'TeamOwner':component_map.get(id),'Total_Tests':1,'Avg_Execution_Time':float(line.split('|')[2].split(':')[1].strip('s')),'Failure_Count':0 if status == 'PASS' else 1})

    df = pd.DataFrame(data)
    return df
#df.groupby('TeamOwner').agg({'Total_Tests':'sum','Avg_Execution_Time':'mean','Failure_Count':'sum'}).reset_index()

df = identifyFailedTests('./resources/week1.TestLog.txt','./resources/week1_compontent_mapping.csv')
print(df)
#print(df.groupby('TeamOwner').agg({'Total_Tests':'sum','Avg_Execution_Time':'mean','Failure_Count':'sum'}).reset_index())

""" 
[METRIC] ID:1001|Name:test_cart_add|Time:0.45s|Status:PASS
1001,Frontend,Low
Summary Metrics by Team:
   TeamOwner  Total_Tests  Avg_Execution_Time  Failure_Count
0   Frontend            1                0.45              0
1  Marketing            1                0.12              1
2   Payments            1                4.82              1
3 SearchCore            1                3.10              0
4   Security            1                1.25              0 """