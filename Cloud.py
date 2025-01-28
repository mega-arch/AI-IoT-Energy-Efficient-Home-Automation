import requests
import json

# Firebase project URL
firebase_url = "https://your-firebase-project.firebaseio.com/data.json"

# Data to upload (ambient light and optimal light intensity)
data = {
    'ambient_light': 350,
    'optimal_light_intensity': 150,
}

# Sending the data to Firebase
response = requests.post(firebase_url, data=json.dumps(data))

# Check if data was successfully uploaded
if response.status_code == 200:
    print("Data uploaded successfully!")
else:
    print("Failed to upload data.")
