from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package='class4_tf',
            executable='broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'base_link'}
            ]
        ),
        DeclareLaunchArgument(
            name = 'target_frame', 
            default_value='world',
            description='Target frame name.'
        ),

        Node(
            package='class4_tf',
            executable='broadcast_fix',
            name='broadcaster2',
            output='screen',
            
        ),
        Node(
            package='class4_tf',
            executable='assignment3_listen',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
    ])