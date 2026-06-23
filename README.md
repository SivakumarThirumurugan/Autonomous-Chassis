# Autonomous Chassis: Hardware-in-the-Loop Simulation

**Role:** R&D Mechatronics Engineer
**Tech Stack:** ROS 2 (Humble), Gazebo, C++, Python, Advanced CAD

---

<div align="center">
  <!-- TO DO: Upload a GIF of your robot moving in Gazebo here -->
  <img src="Chassis_gif.gif" alt="Robot Simulation GIF" width="800"/>
</div>

---

### 🚀 Project Architecture
This repository demonstrates a complete hardware-to-software pipeline for autonomous robotic systems. It details the transition of a custom-designed mechanical chassis from static 3D CAD models into a dynamic, physics-based simulation environment using ROS 2 and Gazebo.

### ⚙️ Engineering Workflow

1.  **Mechanical Design:** Custom chassis and drivetrain modeled emphasizing clearance management and realistic mass distribution.
2.  **Kinematic Translation:** Parts exported as lightweight `.STL` meshes and integrated into a custom URDF/Xacro framework to establish the rigid body tree, joint limits, and inertia tensors.
3.  **Simulation & Control:** Integration of the Gazebo Ackermann Steering Plugin (gazebo_ros_ackermann_drive), allowing direct velocity control via ROS 2 `cmd_vel` topics and real-time visualization in RViz.

### 🛠️ Build and Execution Instructions

**Prerequisites:**
*   Ubuntu 22.04 LTS
*   ROS 2 Humble
*   Gazebo / `gazebo_ros_pkgs`
---

<div align="center">
  <!-- TO DO: Upload a GIF of your robot moving in Gazebo here -->
  <img src="autonomous_chassis_rviz.png" alt="Robot Simulation GIF" width="800"/>
</div>

---

**Installation:**
```bash
# Create a clean ROS 2 workspace
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone https://github.com/SivakumarThirumurugan/Autonomous-Chassis.git

# Resolve dependencies and build
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install

# Environment activation & launch
source install/setup.bash
ros2 launch autonomous_chassis_description display.launch.py
