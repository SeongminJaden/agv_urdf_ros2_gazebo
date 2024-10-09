from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_robot',
            output='screen',
            arguments=[
                '-entity', 'my_robot',
                '-file', '/home/ubuntu/ros2_ws/src/amr_sim/urdf/UDRF_AMR_Model.urdf',
                '-x', '0', '-y', '0', '-z', '0'  # 위치 조정
            ]
        )
    ])

