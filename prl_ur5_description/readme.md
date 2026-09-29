# prl_ur5_description

The `prl_ur5_description` package provides the UR5 workbench description, including 3D model files necessary for visualizing and simulating the UR5 robot in a ROS 2 environment. 

It is part of the PRL (Paris Robotics Lab) ecosystem and is designed to facilitate the use of the UR5 robot in simulation.

## Content

### Launch Files
- **`view_mantis.launch.py`**  

Refer to the built-in documentation in the launch file header for more details.

### URDF Files
- **`mantis.urdf.xacro`**: the whole robot, built from the setup file of `prl_ur5_robot_configuration`
- **`_workcell_mantis.urdf.xacro`**: Mantis Vention table and walls (`workcell: mantis`)
- **`_workcell_bimanual_stand.urdf.xacro`**: bimanual stand with two angled mounting plates (`workcell: bimanual_stand`), with aluminium masses and inertias
- **`ur5_complete_arm.urdf.xacro`**: one UR arm (`ur_type`) with its F/T sensor, gripper, wrist camera and ros2_control
- **`_gripper.urdf.xacro`**: grippers, including the Robotiq 2F-85 (`robotiq-2f-85`)
- **`_force_sensor.urdf.xacro`**
- **`_fixed_cameras.urdf.xacro`**: scene cameras, with or without the Mantis camera post (`fixture`)
- **`_camera_sensor.urdf.xacro`**: RealSense D435i, Orbbec Femto Mega, ZED Mini, ZED 2i
- **`_zed.urdf.xacro`**: ZED cameras (`zed_description`) with generic Gazebo colour and depth sensors
- **`_d435_gazebo.urdf.xacro`**

In Gazebo, the bimanual stand is fixed to the world unless `anchored: false`.

### STL models
- **`vention_table.stl`**
- **`RG_connector_simple.stl`**
- **`RG_connector_simple_convex.stl`**
- **`bimanual_stand/`**: frame, angled brackets and mounting plates of the bimanual stand (exported in cm)


## Usage

```bash
ros2 launch prl_ur5_description view_mantis.launch.py
```
