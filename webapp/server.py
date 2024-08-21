from fastapi import FastAPI, Body
import joblib
import numpy as np

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

model = joblib.load('webapp/solubility_model_0.joblib')

app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"provide a SMILES and predict the solubility"}

@app.post('/predict')
async def predict(data:str=Body()):
    mol=Chem.MolFromSmiles(data)
    if not mol:
        return None
    properties=rdMolDescriptors.Properties()
    input_features=properties.ComputeProperties(mol)
    prediction=model.predict([input_features])
    return {'solubility':prediction[0]}
