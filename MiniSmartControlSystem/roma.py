import os
os.environ["DISPLAY"] = ":0"
import RPi.GPIO as GPIO
import tkinter as tk


# Set up GPIO pins for controlling the devices
DOOR_PIN = 17  # Replace with the actual GPIO pin number for doors
WINDOW_PIN = 18  # Replace with the actual GPIO pin number for windows
LIGHTS_PIN = 19  # Replace with the actual GPIO pin number for lights
AC_PIN = 20  # Replace with the actual GPIO pin number for the air conditioner

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

def create_main_window():
    # Create the main window
    window = tk.Tk()
    window.title("Smart Home Control Center")

    # Doors control
    doors_label = tk.Label(window, text="Doors")
    doors_label.pack()
    doors_button = tk.Button(window, text="Open Doors", command=open_doors)
    doors_button.pack()

    # Windows control
    windows_label = tk.Label(window, text="Windows")
    windows_label.pack()
    windows_button = tk.Button(window, text="Open Windows", command=open_windows)
    windows_button.pack()

    # Lights control
    lights_label = tk.Label(window, text="Lights")
    lights_label.pack()
    lights_button = tk.Button(window, text="Turn On Lights", command=turn_on_lights)
    lights_button.pack()

    # Air conditioner control
    ac_label = tk.Label(window, text="Air Conditioner")
    ac_label.pack()
    ac_button = tk.Button(window, text="Turn On AC", command=turn_on_ac)
    ac_button.pack()

    window.mainloop()

# Call the create_main_window function to start the application
create_main_window()
