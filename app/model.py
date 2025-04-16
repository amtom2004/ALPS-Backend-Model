import joblib

model = joblib.load("model/landslide_model.pkl")

def predict(input_data):
    input_list = [
        input_data.displacement,
        input_data.kriging,
        input_data.idw,
        input_data.elevation,
        input_data.slope,
        input_data.lithology
    ]
    prediction = model.predict([input_list])[0]
    return int(prediction)