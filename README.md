# AI & IoT: Energy Efficient Home Automation

## Overview

This project demonstrates the integration of **Artificial Intelligence (AI)** and **Internet of Things (IoT)** to create a smart, energy-efficient home lighting system. The system automates light intensities in residential areas using machine learning algorithms, Light Dependent Resistor (LDR) sensors, and Raspberry Pi Pico. The goal is to optimize energy consumption while maintaining comfort by adjusting lighting based on ambient light conditions and user preferences.

## Key Features

- **Energy-Efficient Lighting**: Automatically adjusts light intensity based on ambient light conditions.
- **Real-Time Monitoring**: Monitors and adjusts lighting in real-time using an LDR sensor.
- **Machine Learning Model**: Uses machine learning algorithms to predict the optimal lighting conditions.
- **User Control**: Option to manually override the automatic control through a web or mobile interface.
- **Cloud Integration**: Stores sensor data and system status on the cloud for future analysis and monitoring.
- **Scalability**: Can be extended to include other IoT devices like thermostats, fans, etc.

## Technologies Used

- **Raspberry Pi Pico**: Microcontroller for interfacing with sensors and controlling actuators.
- **Light Dependent Resistor (LDR)**: Sensor to measure ambient light intensity.
- **PWM (Pulse Width Modulation)**: Controls light intensity based on LDR readings.
- **Machine Learning**: Used to predict optimal light intensity based on data patterns.
- **Flask**: Python web framework to create a simple user interface for monitoring and control.
- **Firebase**: Cloud storage for storing sensor data and system logs.
- **MQTT**: Messaging protocol for communication between IoT devices.

## System Architecture

The system architecture involves the following key components:
1. **LDR Sensor**: Measures the ambient light intensity in the room.
2. **Raspberry Pi Pico**: The microcontroller processes sensor data and controls the PWM pins to adjust light brightness.
3. **Machine Learning Model**: Analyzes past data to predict the optimal light intensity needed.
4. **Web Interface**: Provides users with an interface to monitor and control the system.

## Getting Started

Follow these steps to set up and run the project:

### Prerequisites
- **Raspberry Pi Pico** (or any compatible microcontroller)
- **LDR Sensor**
- **Relay Module** (to control lights)
- **OLED Display** (optional for real-time feedback)
- **Python 3.x** (for running the machine learning model and Flask web app)
- **MQTT Broker** (e.g., MQTT Eclipse or your own setup)

### Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/ai-iot-energy-efficient-home-automation.git
   cd ai-iot-energy-efficient-home-automation
   ```

2. **Install Required Libraries:**
   Install necessary Python libraries using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Upload Code to Raspberry Pi Pico:**
   Follow the instructions to upload the code for reading the LDR sensor, adjusting PWM, and connecting to MQTT.

4. **Set Up the Cloud Integration (Firebase):**
   - Create a Firebase project and configure the database URL.
   - Replace the Firebase URL in the code with your project's URL.

5. **Run the Web Interface (Optional):**
   If you'd like to view and control the system via a web interface, run the Flask app:
   ```
   python app.py
   ```
   Navigate to `http://127.0.0.1:5000` in your browser.

### Example Usage

1. **Real-time Light Adjustment**: The system continuously monitors ambient light intensity and adjusts the light levels accordingly.
2. **Manual Override**: Using the web interface, users can manually adjust the light intensity or turn the light on/off.
3. **Data Storage**: Sensor data is sent to the cloud and can be analyzed for future improvements.

## Future Improvements

- **Integration with other IoT Devices**: Extend the system to include other smart home devices such as thermostats and fans.
- **Enhanced Machine Learning Models**: Improve the model's prediction accuracy by training with more diverse datasets.
- **Mobile Application**: Develop a mobile app to allow users to control the system on the go.
- **Energy Consumption Analytics**: Add analytics to track energy savings and provide insights for improving efficiency.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Raspberry Pi Pico**: For enabling easy IoT integration.
- **Firebase**: For cloud storage and real-time data sync.
- **MQTT Protocol**: For efficient messaging and communication between devices.
- **Open-source Community**: For various resources and libraries that helped in the development of this project.

