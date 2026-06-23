import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.descriptions

def generate_launch_description():
    # Dynamically find where the system compiled the package
    pkg_dir = get_package_share_directory('autonomous_chassis_description')
    
    # Locate files smoothly within the share index
    xacro_file = os.path.join(pkg_dir, 'urdf', 'chassis.urdf.xacro')
    rviz_config = os.path.join(pkg_dir, 'rviz', 'chassis_view.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': launch_ros.descriptions.ParameterValue(
                os.popen(f'xacro {xacro_file}').read(), value_type=str
            )}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])
