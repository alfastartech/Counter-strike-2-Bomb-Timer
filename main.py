import time
import threading
from PIL import ImageGrab
import tkinter as tk
from tkinter import Label

def get_red_pixel_ratio(image):
    pixels = image.getdata()
    red_pixels = [pixel for pixel in pixels if pixel[0] > 160 and pixel[1] < 100 and pixel[2] < 100]
    return len(red_pixels) / len(pixels)

def contains_white_pixel(image):
    pixels = image.getdata()
    return any(pixel == (255, 255, 255) for pixel in pixels)

def start_timer(seconds, stop_event):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.wm_attributes("-alpha", 0.5)
    label = Label(root, text="", font=("Helvetica", 48))
    label.pack()

    start_time = time.perf_counter()
    while seconds > 0:
        if stop_event.is_set():
            break
        elapsed = time.perf_counter() - start_time
        remaining = max(0, seconds - int(elapsed))
        label.config(text=str(remaining))
        root.update()
        time.sleep(1)
    
    root.destroy()

def scan_screen_and_start_timer(red_threshold=0.1):
    while True:
        screenshot = ImageGrab.grab(bbox=(945, 10, 975, 30))
        red_ratio = get_red_pixel_ratio(screenshot)
        
        if red_ratio > red_threshold:
            stop_event = threading.Event()
            timer_thread = threading.Thread(target=start_timer, args=(40, stop_event))
            timer_thread.start()
            
            while timer_thread.is_alive():
                screenshot = ImageGrab.grab(bbox=(945, 10, 975, 30))
                if contains_white_pixel(screenshot):
                    stop_event.set()
                    break
                time.sleep(1)
        
        time.sleep(0.1)

if __name__ == "__main__":
    scan_screen_and_start_timer()
