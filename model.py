# model.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dummy data
data = [
    {"instituteName": "Institute A", "teachingLearningResources": 85, "researchProfessionalPractice": 78, "placementRecord": 90, "outreachInclusivity": 76, "perception": 80},
    {"instituteName": "Institute B", "teachingLearningResources": 75, "researchProfessionalPractice": 68, "placementRecord": 85, "outreachInclusivity": 70, "perception": 75},
    {"instituteName": "Institute C", "teachingLearningResources": 88, "researchProfessionalPractice": 80, "placementRecord": 92, "outreachInclusivity": 78, "perception": 83},
    {"instituteName": "Institute D", "teachingLearningResources": 70, "researchProfessionalPractice": 65, "placementRecord": 80, "outreachInclusivity": 72, "perception": 68},
    {"instituteName": "Institute E", "teachingLearningResources": 82, "researchProfessionalPractice": 75, "placementRecord": 88, "outreachInclusivity": 74, "perception": 79},
    {"instituteName": "Institute F", "teachingLearningResources": 78, "researchProfessionalPractice": 72, "placementRecord": 85, "outreachInclusivity": 73, "perception": 76},
    {"instituteName": "Institute G", "teachingLearningResources": 83, "researchProfessionalPractice": 78, "placementRecord": 90, "outreachInclusivity": 77, "perception": 82},
    {"instituteName": "Institute H", "teachingLearningResources": 74, "researchProfessionalPractice": 70, "placementRecord": 83, "outreachInclusivity": 71, "perception": 74},
    {"instituteName": "Institute I", "teachingLearningResources": 86, "researchProfessionalPractice": 79, "placementRecord": 91, "outreachInclusivity": 76, "perception": 81},
    {"instituteName": "Institute J", "teachingLearningResources": 72, "researchProfessionalPractice": 67, "placementRecord": 81, "outreachInclusivity": 70, "perception": 69},
    {"instituteName": "Institute K", "teachingLearningResources": 80, "researchProfessionalPractice": 74, "placementRecord": 86, "outreachInclusivity": 75, "perception": 77},
    {"instituteName": "Institute L", "teachingLearningResources": 79, "researchProfessionalPractice": 73, "placementRecord": 84, "outreachInclusivity": 72, "perception": 75},
    {"instituteName": "Institute M", "teachingLearningResources": 84, "researchProfessionalPractice": 77, "placementRecord": 89, "outreachInclusivity": 78, "perception": 80},
    {"instituteName": "Institute N", "teachingLearningResources": 73, "researchProfessionalPractice": 69, "placementRecord": 82, "outreachInclusivity": 71, "perception": 70},
    {"instituteName": "Institute O", "teachingLearningResources": 81, "researchProfessionalPractice": 76, "placementRecord": 87, "outreachInclusivity": 74, "perception": 78},
    {"instituteName": "Institute P", "teachingLearningResources": 76, "researchProfessionalPractice": 70, "placementRecord": 83, "outreachInclusivity": 72, "perception": 73},
    {"instituteName": "Institute Q", "teachingLearningResources": 85, "researchProfessionalPractice": 79, "placementRecord": 90, "outreachInclusivity": 77, "perception": 81},
    {"instituteName": "Institute R", "teachingLearningResources": 74, "researchProfessionalPractice": 68, "placementRecord": 82, "outreachInclusivity": 70, "perception": 72},
    {"instituteName": "Institute S", "teachingLearningResources": 82, "researchProfessionalPractice": 75, "placementRecord": 88, "outreachInclusivity": 75, "perception": 79},
    {"instituteName": "Institute T", "teachingLearningResources": 77, "researchProfessionalPractice": 71, "placementRecord": 84, "outreachInclusivity": 72, "perception": 74},
    {"instituteName": "Institute U", "teachingLearningResources": 89, "researchProfessionalPractice": 81, "placementRecord": 93, "outreachInclusivity": 79, "perception": 84}
]

df = pd.DataFrame(data)

# Encode InstituteName if needed
df['instituteName'] = df['instituteName'].astype('category').cat.codes

# Define the features and target variable
X = df[['teachingLearningResources', 'researchProfessionalPractice', 'placementRecord', 'outreachInclusivity', 'perception']]
y = np.arange(len(df))  # This is a placeholder for ranks. Replace with actual ranks if available.

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

def predict_rank(data):
    df = pd.DataFrame(data, index=[0])
    df['instituteName'] = df['instituteName'].astype('category').cat.codes
    X_new = df[['teachingLearningResources', 'researchProfessionalPractice', 'placementRecord', 'outreachInclusivity', 'perception']]
    rank = model.predict(X_new)
    return rank[0]
