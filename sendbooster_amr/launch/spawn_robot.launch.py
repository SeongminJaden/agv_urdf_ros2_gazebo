from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # 로봇 설명 파일 경로
    robot_description_path = '/home/ubuntu/ros2_ws/src/sendbooster_amr/urdf/sendbooster_amr.urdf'
    
    # 기본 비어있는 Gazebo 월드 파일 경로
    empty_world_path = os.path.join(
        FindPackageShare('gazebo_ros').find('gazebo_ros'),
        'worlds', 'empty.world'
    )
    
    return LaunchDescription([
        # Robot State Publisher 노드
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': open(robot_description_path).read(),
            }],
        ),
        
        # RViz 노드
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/ubuntu/ros2_ws/src/sendbooster_amr/rviz/sendbooster_amr.rviz'],
            parameters=[{
                'use_sim_time': True,
            }],
            remappings=[
                ('/tf', '/tf'),
                ('/tf_static', '/tf_static'),
                ('/robot_description', 'robot_description'),
            ],
        ),
        
        # Gazebo 시뮬레이터 노드
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([PathJoinSubstitution([
                FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'
            ])]),
            launch_arguments={'world': empty_world_path}.items(),
        ),
    ])
