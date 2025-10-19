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
```bash
python3 -m venv .venv
source .venv/bin/activate
