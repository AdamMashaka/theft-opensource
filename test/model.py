import joblib
import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Load the model from the file
model = joblib.load('models3/fraud.pkl')

# Inspect the model
print(model)