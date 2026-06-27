import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_dir = get_package_share_directory('autonomous_chassis_description')
    xacro_file = os.path.join(pkg_dir, 'urdf', 'chassis.urdf.xacro')

    # Process Xacro to raw XML format string
    robot_description_raw = os.popen(f'xacro {xacro_file}').read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_raw, 'use_sim_time': True}]
        )
    ])
