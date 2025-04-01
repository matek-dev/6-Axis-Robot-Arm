import tkinter as tk
from PIL import Image, ImageTk
import serial

# Configure Serial Communication with Arduino
SERIAL_PORT = "/dev/serial0"  # Points to "/dev/ttyS0"
BAUD_RATE = 115200  

try:
    uart_serial = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to Arduino on {SERIAL_PORT} at {BAUD_RATE} baud.")
except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")
    uart_serial = None

# Function to send slider value over UART
def send_slider_data(slider_id, value):
    if uart_serial and uart_serial.is_open:
        data_string = f"S{slider_id}{value}\n"
        uart_serial.write(data_string.encode())
        print(f"Sent: {data_string.strip()}")
    else:
        print("UART serial not connected", f"SliderID: {slider_id}", f"Val: {value}")

# Function to update slider value and send data
def update_slider(index, value):
    # slider_value = sliders[index].get()
    send_slider_data(index + 1, value)

# Function to exit the application
def exit_app():
    if uart_serial:
        uart_serial.close()
    root.destroy()

# Function to resize the image dynamically
# def resize_image(event):
#     new_width = event.width // 2  # Half the window width
#     new_height = event.height    # Full window height
#     if new_width > 0 and new_height > 0:
#         resized_img = img_original.resize((new_width, new_height), Image.Resampling.LANCZOS)
#         img_tk_resized = ImageTk.PhotoImage(resized_img)
#         img_label.config(image=img_tk_resized)
#         img_label.image = img_tk_resized

# Function to adjust slider value and update UART
def adjust_slider(slider, step, index):
    current_value = slider.get()
    new_value = max(0, min(100, current_value + step))  # Ensure value stays between 0 and 100
    slider.set(new_value)
    # update_slider(index)

run_state = {'running': False}

def send_command(cmd):
    if uart_serial and uart_serial.is_open:
        uart_serial.write((cmd + "\n").encode())
        print(f"Sent: {cmd}")
    else:
        print("UART not connected", f" cmd: {cmd}")

def toggle_run_pause():
    if run_state['running']:
        send_command("PAUSE")
        run_button.config(text="RUN")
    else:
        send_command("RUN")
        run_button.config(text="PAUSE")
    run_state['running'] = not run_state['running']

# Initialize the main window
root = tk.Tk()
root.title("UART Robot Control")
root.minsize(350, 300)  # Minimum size: 3.5 in width x 6 in height

# Configure the main grid
root.rowconfigure(0, weight=1)  # Image and sliders share row 0
root.columnconfigure(0, weight=1)  # Image column
root.columnconfigure(1, weight=1)  # Sliders column

# Add an image frame
image_frame = tk.Frame(root)
image_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Load and display the image
image_path = "Robot-Arm.png"  # Replace with your image path
try:
    img_original = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img_original)
    img_label = tk.Label(image_frame, image=img_tk)
    img_label.pack(fill=tk.BOTH, expand=True)
except FileNotFoundError:
    img_label = tk.Label(image_frame, text="Image not found")
    img_label.pack(fill=tk.BOTH, expand=True)

# Add a frame for sliders
slider_frame = tk.Frame(root)
slider_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
slider_frame.rowconfigure(list(range(7)), weight=1)
slider_frame.columnconfigure(1, weight=1)

# Create sliders and add plus/minus buttons
sliders = []
labels = ['Grip', 'Wrist Bend', 'Wrist Rotate', 'Elbow', 'Shoulder Bend', 'Shoulder Rotate', 'Speed']
for i in range(7):
    slider = tk.Scale(slider_frame, from_=0, to=100, orient=tk.HORIZONTAL, label=labels[i], command=lambda val, idx=i: update_slider(idx, val))
    slider.set(50)
    sliders.append(slider)

    # Minus button
    minus_button = tk.Button(slider_frame, text="-", command=lambda s=slider, idx=i: adjust_slider(s, -1, idx))
    minus_button.grid(row=i, column=0, padx=5, pady=5, sticky="nsew")

    # Slider
    slider.grid(row=i, column=1, padx=5, pady=5, sticky="ew")

    # Plus button
    plus_button = tk.Button(slider_frame, text="+", command=lambda s=slider, idx=i: adjust_slider(s, 1, idx))
    plus_button.grid(row=i, column=2, padx=5, pady=5, sticky="nsew")

# Add a frame for buttons and create buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# SAVE button
btn_save = tk.Button(button_frame, text="SAVE", command=lambda: send_command("SAVE"))
btn_save.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# RUN/PAUSE button
run_button = tk.Button(button_frame, text="RUN", command=toggle_run_pause)
run_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# RESET button
btn_reset = tk.Button(button_frame, text="RESET", command=lambda: send_command("RESET"))
btn_reset.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# EXIT button
btn_exit = tk.Button(button_frame, text="EXIT", command=exit_app)
btn_exit.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# Bind the resize event to dynamically resize the image
# root.bind("<Configure>", resize_image)

# Run the Tkinter main loop
root.mainloop()
