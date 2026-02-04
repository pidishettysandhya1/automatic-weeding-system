import time
import random

# --- Simulation of sensor data ---
def read_sensor():
    """Simulates reading sensor data (e.g., distance to weed)."""
    return random.randint(10, 50)  # Simulate distance in cm

# --- Navigation functions ---
def move_forward(speed=1.0):
    print(f"Moving forward at speed: {speed}")
    time.sleep(1)

def turn_right(angle=90):
    print(f"Turning right by {angle} degrees")
    time.sleep(0.5)

def turn_left(angle=90):
    print(f"Turning left by {angle} degrees")
    time.sleep(0.5)

def stop_robot():
    print("Stopping the robot")
    time.sleep(0.2)

# --- Weeding functions ---
def is_weed_detected():
    distance = read_sensor()
    if distance < 20:  # Weed detected if distance < 20 cm
        return True
    return False

def remove_weed():
    print("Weed detected! Removing it...")
    time.sleep(2)
    print("Weed removed.")

# --- Main weeding logic ---
def paddy_weeding_system():
    field_width = 100
    field_length = 150
    current_x = 0
    current_y = 0
    direction = "north"

    while current_y < field_length:
        move_forward()
        current_y += 1

        if is_weed_detected():
            remove_weed()

        if current_x >= field_width:
            turn_right(90)
            direction = "south"
            current_x = field_width
        elif current_x <= 0 and direction == "south":
            turn_right(90)
            direction = "north"
            current_x = 0
        elif direction == "north" and current_x < field_width:
            move_forward()
            current_x += 1

    print("Weeding complete.")

# ✅ Correct line
if __name__ == "__main__":
    paddy_weeding_system()
