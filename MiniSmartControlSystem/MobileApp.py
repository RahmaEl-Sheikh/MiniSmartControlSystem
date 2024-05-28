import RPi.GPIO as GPIO
from flask import Flask, request

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
    app.run(host='169.254.223.222', port=5000)