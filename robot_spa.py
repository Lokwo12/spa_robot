
import random
import random, time 
random.seed(time.time()) # Seed random number generator for reproducibility

# === SENSOR CLASS ===

class Sensor:
    """"Simulate a sensor that gathers data from the environment."""
    def __init__(self, sensor_type: str, range_m: float): 
        self.sensor_type = sensor_type 
        self.range = range_m

    def sense_environment(self): 
        """Simulate gathering data from the environment with weighted randomness. 
        For simplicity, returns 'obstacle' if an obstacle is detected or 'clear'  if the path is free.
        """
        sensed_data = random.choices(["obstacle", "clear"], weights=[0.3, 0.7], k=1)[0] # 30% chance of obstacle, 70% chance of clear path
        print(f"[SENSE] {self.sensor_type} detected: {sensed_data}")  #
        return sensed_data


# === PLANNER CLASS ===
class Planner:
    """handles decision-making based on sensor data."""
    def __init__(self):
        self.last_decision = None

    def make_decision(self, sensor_data):
        
        """Decide next action based on sensor data."""

        if sensor_data == "obstacle": # If an obstacle is detected
            decision = "turn_right" # Decide to turn right
        else:
            decision = "move_forward" # If path is clear, move forward
        self.last_decision = decision
        print(f"[PLAN] Decision made: {decision}")  # Log the decision
        return decision


# === ACTUATOR CLASS ===
class Actuator:
    """"represents the robot's actuators that execute actions."""
    def __init__(self, actuator_type: str): # e.g., wheels, arms
        self.actuator_type = actuator_type

    def perform_action(self, action): 
        """Execute the chosen action."""
        print(f"[ACT] {self.actuator_type} performing action: {action}")


# === ROBOT CLASS ===
class Robot:
    """Combines Sensor, Planner, and Actuator to form a robot."""
    def __init__(self, name: str, size: float, weight: float, battery_level: float):
        # Physical attributes
        self.name = name
        self.size = size
        self.weight = weight
        self.battery_level = battery_level

        # Functional components
        self.sensor = Sensor("Ultrasonic", range_m=5.0)
        self.planner = Planner()
        self.actuator = Actuator("Motor Wheels")

    def manage_battery(self, usage: float):
        """Simulate battery drain after each action."""
        self.battery_level -= usage
        self.battery_level = max(self.battery_level, 0)
        print(f"[STATE] Battery level: {self.battery_level:.1f}%")

    def sense_plan_act_cycle(self):
        """Perform one full SENSE → PLAN → ACT cycle."""
        print(f"\n=== {self.name} Starting Cycle ===")

        # sense data from environment
        data = self.sensor.sense_environment()

        # plan next action based on sensed data
        decision = self.planner.make_decision(data)

        # act on the decision
        self.actuator.perform_action(decision)

        # Manage battery
        self.manage_battery(usage=5.0)


# === MAIN TEST / DEMO ===
if __name__ == "__main__":
    robot = Robot(name="Robo1", size=0.5, weight=10.0, battery_level=100.0)

    # Run multiple SENSE-PLAN-ACT cycles
    for _ in range(5):
        robot.sense_plan_act_cycle()

    print("\nSimulation complete.")
