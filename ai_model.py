import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "bp":[120,140,160,180],
    "sugar":[90,160,110,180],
    "cholesterol":[180,220,250,300],
    "disease":[0,1,0,1]
}

df = pd.DataFrame(data)

X = df[["bp","sugar","cholesterol"]]
y = df["disease"]

model = DecisionTreeClassifier()

model.fit(X,y)


def predict_disease(bp,sugar,cholesterol):

    result = model.predict([[bp,sugar,cholesterol]])

    if result[0] == 1:
        return 80
    else:
        return 20


def explain_prediction(bp,sugar,cholesterol):

    reasons = []

    if bp > 140:
        reasons.append("High Blood Pressure detected")

    if sugar > 140:
        reasons.append("High Sugar Level detected")

    if cholesterol > 220:
        reasons.append("High Cholesterol detected")

    if not reasons:
        reasons.append("All health parameters are normal")

    return reasons