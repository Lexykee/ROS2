from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():
    speed_value = LaunchConfiguration('speed')
    omega_value = LaunchConfiguration('omega')
    background_g_value = LaunchConfiguration('background_g')

    speed_arg = DeclareLaunchArgument(
        'speed_value',
        default_value='1.8'
    )
    omega_arg = DeclareLaunchArgument(
        'omega',
        default_value='20.0'
    )
    background_g_launch_arg = DeclareLaunchArgument(
        'background_g',
        default_value='100'
    )
    turtle_node1 = Node(
        package='turtlesim',
        namespace='turtlesim1',
        executable='turtlesim_node',
        name='sim'
    )
    turtle_node2 = Node(
        package='turtlesim',
        namespace='turtlesim2',
        executable='turtlesim_node',
        name='sim'
    )
    turtle_node3 = Node(
        package='turtlesim',
        executable='mimic',
        name='mimic',
        remappings=[
            ('/input/pose', '/turtlesim1/turtle1/pose'),
            ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        ]
    )
    turtle_node4 = Node(
        package='ros2_course',
        executable='turtlesim_controller',
        name='controller',
        remappings=[
            ('/turtle1/pose', '/turtlesim1/turtle1/pose'),
            ('/turtle1/cmd_vel', '/turtlesim1/turtle1/cmd_vel'),
        ]
    )
    return LaunchDescription([
        speed_arg,
        omega_arg,
        background_g_launch_arg,
        turtle_node1,
        turtle_node2,
        turtle_node3,
        turtle_node4
    ])

