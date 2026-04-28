def detect_disease(bp, sugar, cholesterol):

    if sugar > 140:
        return "High Risk of Diabetes"

    elif bp > 140:
        return "High Risk of Hypertension"

    elif cholesterol > 240:
        return "High Risk of Heart Disease"

    else:
        return "No Major Silent Disease Risk"