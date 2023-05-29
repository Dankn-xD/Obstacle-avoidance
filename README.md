# ROS2 Obstacle Avoidance for TurtleBot3

## Description
This is a ROS2 based project that implements obstacle avoidance for the TurtleBot3 robot using the Burger model. The robot uses laser sensor readings to detect obstacles and adjusts its path to avoid them.

## Installation
1. Make sure you have ROS2 Foxy installed
2. Clone this repository into your workspace src folder
3. Compile the project: Run `colcon build` from the workspace root directory.
4. Source the setup script: `. install/setup.bash`
   
## Usage
1. Start the TurtleBot3 simulation: `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py`
2. Run the obstacle avoidance node: `ros2 run obstacle_avoidance obstacle_avoidance`
