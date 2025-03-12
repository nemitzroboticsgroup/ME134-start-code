from XRPLib.differential_drive import DifferentialDrive
from machine import Timer
import time, math, gc, os
drivetrain = DifferentialDrive.get_default_differential_drive()

gc.collect() # empty RAM

# Data collection
data = [] # temp. storage
data_interval = 20 #ms
filename = "data.csv"

if filename in os.listdir():
    os.remove(filename)
    print(f"{filename} deleted.")
else:
    print(f"{filename} does not exist.")

# Hardware timer for pose_udpate
hardware_timer_period = 0.1 #s

class PositionEstimation:
    def __init__(self):
        self.track_width = 15.5 #cm
        self.wheel_diam = 6 #cm
        self.RPMtoCMPS = (math.pi * self.wheel_diam) / 60     # Covert from RPM to cm/s
        self.CMPStoRPM = 60 / (math.pi * self.wheel_diam)     # Covert from cm/s to RPM
        self.x = 0
        self.y = 0
        self.theta = 0
        self.last_data_time = time.ticks_ms()
    def pose_update(self):
        right_motor_speed = drivetrain.right_motor.get_speed()*self.RPMtoCMPS
        left_motor_speed = drivetrain.left_motor.get_speed()*self.RPMtoCMPS
        
        # calculcate forward kinematics model and update x,y, and theta
        # ...


        # Store every data_interval, robot pose in data[]
        current_time = time.ticks_ms() 
        if time.ticks_diff(current_time, self.last_data_time) >= data_interval:
            data.append([
                self.x,
                self.y,
                self.theta
            ])
            self.last_data_time = current_time

kinematics = PositionEstimation()

# Implement hardware timer from lecture and call pose_update function
# ...

# Program robot behavior
# ...

# After experiment, write into file
with open(filename, "w") as f:
    f.write('x,y,theta\n')
    for row in data:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")
print("experiment completed")