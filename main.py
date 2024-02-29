import machine, neopixel, utime

# Pin where the NeoPixel is connected
pin = machine.Pin(0)
mode_button_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
power_button_pin = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)  # New power button

# Number of LEDs
n = 300

# Create a NeoPixel object
np = neopixel.NeoPixel(pin, n)

current_mode = 0  # Current mode starts at 0
power_on = True   # Power state starts as on

# Function to set all pixels to a color
def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()

# Function to change modes
def change_mode():
    global current_mode
    current_mode += 1
    if current_mode > 3:
        current_mode = 1  # Reset to mode 1 if over mode 3

# Function to handle button press and debounce
def handle_button(pin):
    button_state = pin.value()
    utime.sleep_ms(20)  # Debounce delay
    return button_state == 0  # Active low

# Function to toggle power state
def toggle_power():
    global power_on
    power_on = not power_on
    if power_on:
        np.write()  # Turn LEDs back on
    else:
        np.fill((0, 0, 0))  # Turn off all LEDs
        np.write()
        machine.lightsleep()  # Enter light sleep mode

# Function for mode 1
def mode1():
    set_color(255, 0, 0)  # Red
    utime.sleep(1)

# Function for mode 2
def mode2():
    set_color(0, 255, 0)  # Green
    utime.sleep(1)

# Function for mode 3
def mode3():
    set_color(0, 0, 255)  # Blue
    utime.sleep(1)

# Main loop
while True:
    if handle_button(power_button_pin):
        toggle_power()  # Toggle power on/off

    if power_on:
        if handle_button(mode_button_pin):
            change_mode()  # Change mode only if power is on

        # Check for button press and run modes if power is on
        if current_mode == 1:
            mode1()
        elif current_mode == 2:
            mode2()
        elif current_mode == 3:
            mode3()

