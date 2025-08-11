 
from pydantic import BaseModel
import pickle
# Load the model
with open('app/model/rf_model.pkl', 'rb') as model_file:
    loaded_rf = pickle.load(model_file)

# Define the BankNoteAuthenticator class
class BankNoteAuthenticator(BaseModel):
    varsiance: float
    skewness: float   
    curtosis: float
    entropy: float

    def predict(self):
        features = [self.varsiance, self.skewness, self.curtosis, self.entropy]
        return loaded_rf.predict([features])[0]  # Return the prediction (0 or 1)




