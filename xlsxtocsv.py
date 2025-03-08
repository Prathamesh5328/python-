import pandas as pd 
from openpyxl import load_workbook 
dataset = load_workbook(filename = 'Telco_customer_churn.xlsx') 
df = pd.DataFrame(dataset)
# df.to_csv('Telco_customer_churn.xlsx')
# pd.read_csv('Telco_customer_churn.xlsx') 
