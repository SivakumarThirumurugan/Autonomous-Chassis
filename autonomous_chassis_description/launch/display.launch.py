import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Locate the package and URDF file
    pkg_name = 'autonomous_chassis_description'
    pkg_share = get_package_share_directory(pkg_name)
    urdf_file = os.path.join(pkg_share, 'urdf', 'chassis.urdf')

    # 2. Read the XML file into Python
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # 3. Node: Robot State Publisher (Calculates exactly where your STLs are in 3D space)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    # 4. Node: Joint State Publisher GUI (Gives you a pop-up window with sliders to test your wheels!)
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # 5. Node: RViz2 (The 3D visualization window)
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    # 6. Launch everything together
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
