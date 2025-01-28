from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample route to show the status of light intensity
@app.route('/')
def index():
    # Simulate reading light intensity (this could be real-time sensor data)
    ambient_light = random.randint(0, 1023)  # Simulated ambient light level
    optimal_light = random.randint(0, 1023)  # Simulated optimal light level
    return render_template('index.html', ambient_light=ambient_light, optimal_light=optimal_light)

if __name__ == '__main__':
    app.run(debug=True)
