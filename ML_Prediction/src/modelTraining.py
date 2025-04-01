from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

class ModelTraining():
  def process(self,data):
    print('Training Model....')
    X = data.drop(columns='Readmission_30or60Days', axis=1)
    Y = data['Readmission_30or60Days']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
    print(X.shape, X_train.shape, X_test.shape)

    # Create a scaler object
    scaler = StandardScaler()

    # Fit the scaler on the training data and transform it
    X_train_scaled = scaler.fit_transform(X_train)

    # Use the same scaler to transform the test data
    X_test_scaled = scaler.transform(X_test)

    # Create the logistic regression model with increased max_iter
    model = LogisticRegression(max_iter=1000, solver='lbfgs')
    # Train the model using the scaled training data / 
   
    model.fit(X_train_scaled, Y_train)
    X_train_prediction = model.predict(X_train_scaled)
    training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
    print('Accuracy on Training data : ', training_data_accuracy)

    # Accuracy on test data
    X_test_prediction = model.predict(X_test_scaled)
    test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
    print('Accuracy on Test data : ', test_data_accuracy)
    #data = model, test_data_accuracy, scaler, X_test_prediction
    #return data
    return model, scaler, X_train.columns