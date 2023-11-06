import requests
from datetime import datetime
API_ID = "c7ec5544"
API_KEY = "6c4c0ed84151dc005cf4fabf47ee817c"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise = input("what did you do ? ")

parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 75.5,
    "height_cm": 181.64,
    "age": 21
}

response = requests.post(url=exercise_endpoint, json=headers, params=parameters)

data = response.json()
# print(data)

sheet_endpoint = "https://api.sheety.co/ca12b68c5b3e2641f918e1b56755ec29/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
