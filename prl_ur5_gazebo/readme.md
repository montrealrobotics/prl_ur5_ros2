# prl_ur5_gazebo

The `prl_ur5_gazebo` package provides the UR5 workbench launch and files, necessary for simulating the UR5 robot in Gazebo.

It is part of the PRL (Paris Robotics Lab) ecosystem and designed to facilitate the use of the UR5 robot in simulation.

## Content

### Launch Files
- **`start_gazebo_sim.launch.py`**  

Refer to the built-in documentation in the launch file header for more details.

### Configuration files
- **`gz_bridge.yaml`**
- **`camera_bridge.yaml`**

### Setup script
- **`generate_cameras_bridge.py`**

## Usage

### Camera topics

The camera bridge is generated at launch from the camera config of the setup (`cameras_config_file` in
`prl_ur5_robot_configuration`): every activated camera publishes `camera/<camera_name>/color/...` and
`camera/<camera_name>/depth/...`. `config/camera_bridge.yaml` is no longer used by the launch file.

To generate a bridge file by hand:

```bash
python3 <path_to_ws>/src/prl_ur5_ros2/prl_ur5_gazebo/scripts/generate_cameras_bridge.py -o camera_bridge.yaml
```



### Launch Simulation

```bash
ros2 launch prl_ur5_gazebo start_gazebo_sim.launch.py
```

#### Parameters:
- **`launch_rviz`**: Set to `true` to launch RViz alongside the simulation.
- **`gazebo_gui`**: Set to `true` to enable the Gazebo graphical interface.
- **`activate_cameras`**Set to `true` to activate the cameras in the simulation.**

Example usage:

```bash
ros2 launch prl_ur5_gazebo start_gazebo_sim.launch.py launch_rviz:=true gazebo_gui:=true
```
