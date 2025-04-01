from datapreprocessing import DataPreProcessing
from data_ingestion import DataIngestion
from modelTraining import ModelTraining
from modelPrediction import ModelPrediction
from ML_pipeline import Pipeline 

if __name__ == '__main__':
    steps = [
        DataIngestion(),
        DataPreProcessing(),
        ModelTraining(),
        ModelPrediction()
    ]

    pipeline = Pipeline(steps)
    pipeline.run()