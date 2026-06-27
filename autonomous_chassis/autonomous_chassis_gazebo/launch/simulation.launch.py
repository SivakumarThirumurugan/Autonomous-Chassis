import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_description = get_package_share_directory('autonomous_chassis_description')

    gz_sim_launch = os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')

    return LaunchDescription([
        # 1. Launch Gazebo Harmonic with an empty local grid world
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_sim_launch),
            launch_arguments={'gz_args': '-r empty.sdf'}.items()
        ),

        # 2. Run the Robot State Publisher (Broadcasts your chassis structure)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(pkg_description, 'launch', 'display.launch.py'))
        ),

        # 3. NEW: The ROS-to-Gazebo Parameter Bridge (Crucial for Jazzy/Harmonic)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/robot_description@std_msgs/String[gz.msgs.StringMsg'],
            output='screen'
        ),

        # 4. Inject the vehicle frame directly into the running Gazebo simulation
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', 'robot_description', '-name', 'autonomous_chassis', '-z', '0.1'],
            output='screen'
        )
    ])
