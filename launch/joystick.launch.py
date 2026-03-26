import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    joy_params = os.path.join(get_package_share_directory('auto_bot'),'config','joystick.yaml')
    
    # Create a joy_node node for real controller input
    # joy_node = Node(
    #     package='joy',
    #     executable='joy_node',
    #     parameters=[joy_params, {'use_sim_time': use_sim_time}],
    # )
    
    # Create a teleop_node node
    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_node',
        parameters=[joy_params, {'use_sim_time': use_sim_time}],
        remappings=[('/cmd_vel', '/cmd_vel_joy')]
    )

    # twist_stamper = Node(
    #     package='twist_stamper',
    #     executable='twist_stamper',
    #     parameters=[{'use_sim_time': use_sim_time}],
    #     remappings=[('/cmd_vel_in', '/diff_cont/cmd_vel_unstamped'), 
    #     ('/cmd_vel_out', '/diff_cont/cmd_vel')]
    # )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        teleop_node,
        # joy_node,
        # twist_stamper
    ])
