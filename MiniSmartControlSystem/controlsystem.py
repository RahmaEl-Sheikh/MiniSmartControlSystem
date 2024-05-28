import os
os.environ["DISPLAY"] = ":0"

        # Import necessary libraries
import RPi.GPIO as GPIO
from flask import Flask, request    
#from flask_assistant import Assistant, ask, tell


# Set up GPIO pins for controlling the devices
DOOR_PIN = 17  # Replace with the actual GPIO pin number for doors
WINDOW_PIN = 18  # Replace with the actual GPIO pin number for windows
LIGHTS_PIN = 19  # Replace with the actual GPIO pin number for lights
AC_PIN = 20  # Replace with the actual GPIO pin number for the air conditioner

app = Flask(__name__)

def open_doors():
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DOOR_PIN, GPIO.OUT)

    # Open the doors
    GPIO.output(DOOR_PIN, GPIO.HIGH)
    # Add any additional code or delays needed for your specific hardware

    # Clean up GPIO
    GPIO.cleanup()

    print("Opening doors...")

@app.route('/open-doors', methods=['POST'])
def handle_open_doors():
    open_doors()
    return 'Doors opened!'

def open_windows():
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WINDOW_PIN, GPIO.OUT)

    # Open the windows
    GPIO.output(WINDOW_PIN, GPIO.HIGH)
    # Add any additional code or delays needed for your specific hardware

    # Clean up GPIO
    GPIO.cleanup()

    print("Opening windows...")

@app.route('/open-windows', methods=['POST'])
def handle_open_windows():
    open_windows()
    return 'Windows opened!'

def turn_on_lights():
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHTS_PIN, GPIO.OUT)

    # Turn on the lights
    GPIO.output(LIGHTS_PIN, GPIO.HIGH)
    # Add any additional code or delays needed for your specific hardware

    # Clean up GPIO
    GPIO.cleanup()

    print("Turning on lights...")

@app.route('/turn-on-lights', methods=['POST'])
def handle_turn_on_lights():
    turn_on_lights()
    return 'Lights turned on!'

def turn_on_ac():
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AC_PIN, GPIO.OUT)

    # Turn on the air conditioner
    GPIO.output(AC_PIN, GPIO.HIGH)
    # Add any additional code or delays needed for your specific hardware

    # Clean up GPIO
    GPIO.cleanup()

    print("Turning on AC...")

@app.route('/turn-on-ac', methods=['POST'])
def handle_turn_on_ac():
    turn_on_ac()
    return 'AC turned on!'

if __name__ == '__main__':
    # Initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([DOOR_PIN, WINDOW_PIN, LIGHTS_PIN, AC_PIN], GPIO.OUT)

    # Run the Flask web server
    #app.run(host='http://rahmaelsheikh.pythonanywhere.com/', port=5000)
    app.run(host='169.254.223.222', port=5000)
    


# Configure GPIO pins for servo control
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)

# Define the appropriate angles for different temperature settings
temperature_angles = {
    "low": 0,
    "medium": 90,
    "high": 180
}

# Function to set the servo motor position based on desired temperature
def set_servo_position(temperature):
    angle = temperature_angles.get(temperature.lower(), 90)  # Use 90 degrees if temperature is not recognized
    duty_cycle = angle / 18 + 2  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)

# Create Flask app and Assistant
app = Flask(__name__)
assist = Assistant(app, route='/')

# Define intent handler for controlling the air conditioner temperature
@assist.action('ControlAirConditioner')
def control_air_conditioner(temperature):
    set_servo_position(temperature)
    return tell('The air conditioner has been set to {} temperature.'.format(temperature))

# Define endpoint for IFTTT webhook
@app.route('/air-conditioner', methods=['POST'])
def air_conditioner():
    temperature = request.get_json().get('temperature')
    set_servo_position(temperature)
    return 'OK'

if __name__ == '__main__':
    pwm.start(2)  # Start the PWM
    app.run()
    
# Configure GPIO pins for gas sensor
gas_sensor_pin = 14
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gas_sensor_pin, GPIO.IN)

# Create Flask app and Assistant
app = Flask(__name__)
assist = Assistant(app, route='/')

# Define function to check for gas leak
def check_gas_leak():
    if GPIO.input(gas_sensor_pin) == GPIO.HIGH:
        return True
    else:
        return False

# Define intent handler for gas leak detection
@assist.action('CheckGasLeak')
def check_gas_leak_intent():
    if check_gas_leak():
        return tell('A gas leak has been detected. Please evacuate immediately.')
    else:
        return tell('No gas leak detected.')

# Define endpoint for IFTTT webhook
@app.route('/gas-leak', methods=['POST'])
def gas_leak():
    if check_gas_leak():
        # Code to trigger warning mechanism (e.g., send notification to Control Center and mobile app)
        return 'OK'
    else:
        return 'No gas leak detected.'

if __name__ == '__main__':
    app.run()

# Configure GPIO pins for flame sensor
flame_sensor_pin = 14
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(flame_sensor_pin, GPIO.IN)

# Create Flask app and Assistant
app = Flask(__name__)
assist = Assistant(app, route='/')

# Define function to check for fire
def check_fire():
    if GPIO.input(flame_sensor_pin) == GPIO.HIGH:
        return True
    else:
        return False

# Define intent handler for fire detection
@assist.action('CheckFire')
def check_fire_intent():
    if check_fire():
        return tell('Fire has been detected. Please evacuate immediately and call emergency services.')
    else:
        return tell('No fire detected.')

# Define endpoint for IFTTT webhook
@app.route('/fire-detection', methods=['POST'])
def fire_detection():
    if check_fire():
        # Code to trigger alarm or notification mechanism (e.g., send notification to Control Center and mobile app)
        return 'OK'
    else:
        return 'No fire detected.'

if __name__ == '__main__':
    app.run()
    

# Create Flask app and Assistant
app = Flask(__name__)
assist = Assistant(app, route='/')

# Define intent handlers for voice commands
@assist.action('OpenDoorsIntent')
def open_doors():
    # Code to open doors
    return tell('Opening the doors.')

@assist.action('TurnOnLightsIntent')
def turn_on_lights():
    # Code to turn on lights
    return tell('Turning on the lights.')

# Define other voice commands for various aspects of the Smart Home

if __name__ == '__main__':
    app.run()
    
    
    