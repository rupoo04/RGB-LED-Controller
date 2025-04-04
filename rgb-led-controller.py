import RPi.GPIO as GPIO
import time
import threading
import tkinter as tk
from tkinter import ttk

# Default GPIO pins for R, G, B
DEFAULT_RED_PIN = 17
DEFAULT_GREEN_PIN = 22
DEFAULT_BLUE_PIN = 24

# Function to set up GPIO
def setup_gpio(red, green, blue):
    global RED_PIN, GREEN_PIN, BLUE_PIN, red_pwm, green_pwm, blue_pwm
    RED_PIN, GREEN_PIN, BLUE_PIN = red, green, blue
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN, GPIO.OUT)
    red_pwm = GPIO.PWM(RED_PIN, 1000)
    green_pwm = GPIO.PWM(GREEN_PIN, 1000)
    blue_pwm = GPIO.PWM(BLUE_PIN, 1000)
    red_pwm.start(0)
    green_pwm.start(0)
    blue_pwm.start(0)

fade_running = False

def set_color(r, g, b):
    """Set color using values from 0 to 255."""
    red_pwm.ChangeDutyCycle(100 - (r / 255.0) * 100)
    green_pwm.ChangeDutyCycle(100 - (g / 255.0) * 100)
    blue_pwm.ChangeDutyCycle(100 - (b / 255.0) * 100)
    color_label.config(text=f"Current Color: R={r} G={g} B={b}")

def fade_loop():
    global fade_running
    fade_running = True
    hue = 0  # Start at red
    while fade_running:
        fade_speed = fade_slider.get()
        if fade_speed == 0:
            time.sleep(0.1)
            continue
        hue = (hue + fade_speed / 100) % 1.0  # Cycle through colors
        r, g, b = hsv_to_rgb(hue, 1, 1)
        set_color(int(r * 255), int(g * 255), int(b * 255))
        time.sleep(0.05)

def hsv_to_rgb(h, s, v):
    """Convert HSV to RGB (values from 0-1)."""
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i %= 6
    if i == 0:
        return v, t, p
    elif i == 1:
        return q, v, p
    elif i == 2:
        return p, v, t
    elif i == 3:
        return p, q, v
    elif i == 4:
        return t, p, v
    elif i == 5:
        return v, p, q

def toggle_fade():
    global fade_running
    if fade_running:
        fade_running = False
    else:
        threading.Thread(target=fade_loop, daemon=True).start()

def cleanup():
    global fade_running
    fade_running = False
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()

def update_color():
    global fade_running
    fade_running = False  # Stop fade effect when setting manual color
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
    set_color(r, g, b)

def update_label(var, label):
    label.config(text=str(int(var.get())))

def apply_gpio_settings():
    red = int(red_pin_entry.get())
    green = int(green_pin_entry.get())
    blue = int(blue_pin_entry.get())
    setup_gpio(red, green, blue)

# Create GUI
root = tk.Tk()
root.title("RGB LED Controller")

tk.Label(root, text="Red GPIO Pin").pack()
red_pin_entry = tk.Entry(root)
red_pin_entry.insert(0, str(DEFAULT_RED_PIN))
red_pin_entry.pack()

tk.Label(root, text="Green GPIO Pin").pack()
green_pin_entry = tk.Entry(root)
green_pin_entry.insert(0, str(DEFAULT_GREEN_PIN))
green_pin_entry.pack()

tk.Label(root, text="Blue GPIO Pin").pack()
blue_pin_entry = tk.Entry(root)
blue_pin_entry.insert(0, str(DEFAULT_BLUE_PIN))
blue_pin_entry.pack()

tk.Button(root, text="Apply GPIO Pins", command=apply_gpio_settings).pack()

red_frame = tk.Frame(root)
red_frame.pack()
tk.Label(red_frame, text="Red").pack(side=tk.LEFT)
red_slider = ttk.Scale(red_frame, from_=0, to=255, orient="horizontal")
red_slider.pack(side=tk.LEFT)
red_value = tk.Label(red_frame, text="0")
red_value.pack(side=tk.LEFT)
red_slider.config(command=lambda v: update_label(red_slider, red_value))

green_frame = tk.Frame(root)
green_frame.pack()
tk.Label(green_frame, text="Green").pack(side=tk.LEFT)
green_slider = ttk.Scale(green_frame, from_=0, to=255, orient="horizontal")
green_slider.pack(side=tk.LEFT)
green_value = tk.Label(green_frame, text="0")
green_value.pack(side=tk.LEFT)
green_slider.config(command=lambda v: update_label(green_slider, green_value))

blue_frame = tk.Frame(root)
blue_frame.pack()
tk.Label(blue_frame, text="Blue").pack(side=tk.LEFT)
blue_slider = ttk.Scale(blue_frame, from_=0, to=255, orient="horizontal")
blue_slider.pack(side=tk.LEFT)
blue_value = tk.Label(blue_frame, text="0")
blue_value.pack(side=tk.LEFT)
blue_slider.config(command=lambda v: update_label(blue_slider, blue_value))

fade_frame = tk.Frame(root)
fade_frame.pack()
tk.Label(fade_frame, text="Fade Speed").pack(side=tk.LEFT)
fade_slider = ttk.Scale(fade_frame, from_=0, to=100, orient="horizontal")
fade_slider.pack(side=tk.LEFT)
fade_value = tk.Label(fade_frame, text="0")
fade_value.pack(side=tk.LEFT)
fade_slider.config(command=lambda v: update_label(fade_slider, fade_value))

apply_button = tk.Button(root, text="Set Color", command=update_color)
apply_button.pack()

fade_button = tk.Button(root, text="Toggle Fade", command=toggle_fade)
fade_button.pack()

color_label = tk.Label(root, text="Current Color: R=0 G=0 B=0")
color_label.pack()

setup_gpio(DEFAULT_RED_PIN, DEFAULT_GREEN_PIN, DEFAULT_BLUE_PIN)

try:
    root.mainloop()
except KeyboardInterrupt:
    cleanup()
