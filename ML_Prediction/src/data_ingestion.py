import pandas as pd
import numpy as np

class DataIngestion():
  def process(self,data=None):
    print('Fetching the Health care data....')
    url = 'D:\\DE_Projects_github\\practice_projects\\ML_Prediction\\Data\\GHW_HeartFailure_Readmission_Combined.csv'
    data = pd.read_csv(url)
    print('Data fetched successfully')
    return data