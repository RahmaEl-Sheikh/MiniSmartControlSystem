import os
os.environ["DISPLAY"] = ":0"
import RPi.GPIO as GPIO
import tkinter as tk
#from mfrc522 import SimpleMFRC522
#reader = SimpleMFRC522()
root = tk.Tk()
def read_rfid():
    try:
        id, tag = reader.read()
        return id
    finally:
        GPIO.cleanup()
def open_door_with_rfid():
    rfid_id = read_rfid()
    if rfid_id == "YOUR_RFID_TAG_ID":
        open_door()
    else:
        messagebox.showinfo("Access Denied", "Invalid RFID tag.")
rfid_button = tk.Button(root, text="Scan RFID Tag", command=open_door_with_rfid)
rfid_button.pack()

root.mainloop()
