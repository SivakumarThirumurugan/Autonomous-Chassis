cmake_minimum_required(VERSION 3.8)
project(autonomous_chassis_description)

find_package(ament_cmake REQUIRED)

# Install directories to share folder so ROS 2 runtimes can locate assets
install(DIRECTORY launch meshes rviz urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
