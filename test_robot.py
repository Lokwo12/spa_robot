from robot_spa import Robot

def test_full_cycles():
    print("\n=== TEST 1: Full SENSE-PLAN-ACT Cycles ===")
    robot = Robot(name="TestBot1", size=0.5, weight=10.0, battery_level=100.0)
    for i in range(5):
        print(f"\n-- Cycle {i+1} --")
        robot.sense_plan_act_cycle()


def test_modules_separately():
    print("\n=== TEST 2: Modules Tested Separately ===")
    robot = Robot(name="TestBot2", size=0.5, weight=10.0, battery_level=100.0)

    # Test Sensor
    sensor_data = robot.sensor.sense_environment()
    print("Sensor output:", sensor_data)

    # Test Planner
    decision = robot.planner.make_decision(sensor_data)
    print("Planner output:", decision)

    # Test Actuator
    robot.actuator.perform_action(decision)


def test_reaction_to_inputs():
    print("\n=== TEST 3: Robot Reaction to Specific Sensor Inputs ===")
    robot = Robot(name="TestBot3", size=0.5, weight=10.0, battery_level=100.0)

    # Define test cases
    test_inputs = ["clear", "obstacle", "clear", "obstacle"]

    for i, sensor_value in enumerate(test_inputs):
        print(f"\n-- Input {i+1}: {sensor_value} --")
        decision = robot.planner.make_decision(sensor_value)
        robot.actuator.perform_action(decision)


if __name__ == "__main__":
    test_full_cycles()
    test_modules_separately()
    test_reaction_to_inputs()

    print("\nAll tests completed successfully.")
