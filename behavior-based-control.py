class BehaviorBasedRobot:
    def __init__(self):
        pass  # No explicit state; behavior is determined by sensor input

    def get_sensor_input(self):
        return input("Enter sensor input: ")  # Simulating sensor data

    def random_walk(self):
        print("Robot is wandering.") 

    def line_following(self):
        print("Robot is line following.") 

    def wall_following(self):
        print("Robot is wall following.")

    def execute_behavior(self, sensor_input):
        if sensor_input == "line":
            self.line_following()
        elif sensor_input == "wall":
            self.wall_following()
        else:
            self.random_walk()

    def run(self):
        while True:
            sensor_input = self.get_sensor_input()
            if sensor_input == "halt":
                print("Robot has stopped.")
                break
            self.execute_behavior(sensor_input)

# Example usage
robot = BehaviorBasedRobot()
robot.run()
