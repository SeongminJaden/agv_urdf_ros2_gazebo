cmake_minimum_required(VERSION 3.5)

# 프로젝트 이름을 설정합니다.
project(amr_sim)

# 필요한 패키지를 찾습니다.
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)  # 필요에 따라 추가
find_package(gazebo_ros REQUIRED)

# 실행 파일이나 라이브러리 추가 (필요시)
# add_executable(my_node src/my_node.cpp)
# ament_target_dependencies(my_node rclcpp)

# 설치 디렉토리 설정
install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME}/meshes)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/launch)

ament_package()

