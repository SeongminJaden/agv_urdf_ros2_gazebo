cmake_minimum_required(VERSION 3.8)
project(sendbooster_amr)

# ROS 2 패키지 설정
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rviz2 REQUIRED)

# 설치할 launch 파일 경로 설정
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# 설치할 URDF, RViz 설정 파일 경로 설정
install(DIRECTORY urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

# ament 패키지 설정
ament_package()
