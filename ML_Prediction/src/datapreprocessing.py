class DataPreProcessing():
  def process(self, data):
    print('Data Pre Processing ...')
    if data.isnull().sum().sum() == 0:
      print('No Null values found')
    else:
      data = data.dropna()  
    # checking the distribution of Target Variable
    data['Readmission_30or60Days'].value_counts().sort_index()
    data = data.drop(columns=['Gender', 'Ethnicity', 'Discharge_Disposition', 'Patient_ID', 'Readmission_30Days', 'Readmission_60Days'], axis=1)
    return data