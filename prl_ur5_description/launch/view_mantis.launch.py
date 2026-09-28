############################################################################################################
# Description: This launch file starts the vizualization of the workbench with the UR5 robot in RViz.
#              The launch file starts the following nodes:
#               - joint_state_publisher_gui: GUI to move the robot joints
#               - robot_state_publisher: Publishes the robot state
#               - rviz2: RViz visualization
# Usage:
#   $ ros2 launch prl_ur5_description view_workbench.launch.py
############################################################################################################
import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    # Config file
    rviz_config_file = PathJoinSubstitution([FindPackageShare("prl_ur5_description"), "rviz", "config.rviz"])

    ###### Robot description ######
    # Command to generate robot description from xacro file
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),  # Find the xacro executable
            " ", 
            PathJoinSubstitution([FindPackageShare("prl_ur5_description"), "urdf", "mantis.urdf.xacro"]),
            " ",
            "gz_sim:=",
            "false",
            " ",
        ]
    )
    # Create dictionary to pass robot_description to the robot_state_publisher node parameters
    robot_description = {
        "robot_description": ParameterValue(value=robot_description_content, value_type=str)
    }
    # Start the joint sliders at the initial joint positions of the setup file (if any)
    setup_file = os.path.join(get_package_share_directory('prl_ur5_robot_configuration'), 'config', 'standard_setup.yaml')
    with open(setup_file, 'r') as f:
        setup = yaml.safe_load(f)
    zeros = {}
    for side in ('left', 'right'):
        for joint, value in ((setup.get(side) or {}).get('initial_joint_positions') or {}).items():
            zeros[f'{side}_{joint}'] = float(value)

    # Define the joint_state_publisher_gui node
    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        parameters=[robot_description, {"zeros": zeros}] if zeros else [robot_description],
    )
    # Define the robot_state_publisher node to publish the robot state
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description],
    )

    ###### Rviz ######
    # Define the RViz node for visualization
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    # List of nodes to start
    nodes_to_start = [
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node,
    ]

    # Return the launch description
    return LaunchDescription(nodes_to_start)
