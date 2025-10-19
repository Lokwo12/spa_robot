# SENSE-PLAN-ACT Robot Simulation

## Overview
This project implements a basic **SENSE-PLAN-ACT (SPA) hierarchical robot** model in Python.  
It demonstrates how a robot can sense its environment, plan actions, and execute them using object-oriented programming.

## Project Structure
- `spa_robot.py` – Main robot implementation
  - `Sensor` – Simulates environment sensing
  - `Planner` – Makes decisions based on sensor data
  - `Actuator` – Executes the chosen actions
  - `Robot` – Integrates all modules and simulates SPA cycles
- `test_robot.py` – Script for testing:
  - Full SPA cycles
  - Individual module tests
  - Robot reactions to specific sensor inputs

## How to Run
1. Create and activate a virtual environment (optional but recommended):
`python3 -m venv .venv`
`source .venv/bin/activate`

## 2. Install any dependencies (standard Python library is sufficient for this project):
`pip install --upgrade pip`

## 3. Run the main robot simulation:
`python spa_robot.py`

## 4. Run the tests:
`python test_robot.py`

## 5. Dependencies.
- Python 3.x
- Standard Python libraries (`random`, `time`)


## Features
- Randomized environmental sensing
- Simple decision-making (move forward or turn right)
- Battery level management
- Modular design for easy extension
