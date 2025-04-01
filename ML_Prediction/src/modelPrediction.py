import numpy as np
import pandas as pd

class ModelPrediction():
  def process(self,model_data): 
    print('Prediction ....')
    model, scaler, columns = model_data

    #input data that predict no heart failuer
    input_data = (83,7,4,119,37.1,147,160,99,27,11,0.61,127,13.1,2973,39)
    
    #input data that predict heart failuer
    #input_data = (31,86,11,0,94,37.6,58,151,105,29,1.38,139,10.5,3746,52)

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    #reshaping the numpy array as we are prediciting for only one instance
    input_data_reshaped= input_data_as_numpy_array.reshape(1, -1)

    # Convert to DataFrame with the same column names as your training data
    # Assuming X_train was originally a DataFrame
    input_data_df = pd.DataFrame(input_data_reshaped, columns=columns)

    # Scale the input data using the previously defined scaler
    input_data_scaled = scaler.transform(input_data_df)

    # Make the prediction using the scaled input data
    prediction = model.predict(input_data_scaled)
    #print("Prediction:", prediction)
    if prediction[0] == 0:
        print('No Predication of readmission')
    else:
        print('The Person can be readmitted')
    #return prediction