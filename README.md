# ConveyorGrasp
A simulation to Detect, Track, Synthesize Grasp and execute grasp for objects on a moving conveyor belt.

![image](https://github.com/user-attachments/assets/8a3769be-1846-4550-ab78-e30d3b7b74c3)


### To launch the environment:
```bash
ros2 launch panda_ros2_moveit2 panda_interface.launch.py
```

### To start the open loop grasping:
```bash
ros2 run pandarobotmove pandarobotcloseloopyolo
```

### To spawn the YCB object in our environment:
```bash
ros2 run ros2_grasping spawn_ycb.py --x 0.5 --y -0.7  --name "gelatin_box"
```

### To move the robot to a specific pose:
```bash
ros2 action send_goal -f /MoveXYZW ros2_data/action/MoveXYZW "{positionx: 0.50, positiony: 0.05, positionz: 0.6, yaw: 45.00, pitch: 180.00, roll: 0.00, speed: 1.0}"
```
or 
```bash
ros2 topic pub /robotaction std_msgs/msg/String "data: '{\"action\": \"MoveXYZW\", \"value\": {\"positionx\": 0.5, \"positiony\": 0.05, \"positionz\": 0.6, \"yaw\": 45.00, \"pitch\": 180.00, \"roll\": 0.00}, \"speed\": 1.0}'" --once
```

### To power the conveyor belt and control it:
```bash
ros2 service call /CONVEYORPOWER conveyorbelt_msgs/srv/ConveyorBeltControl "{power: 2.5}"
```

### To run yolo for overhead:
```bash
ros2 run image_processing overhead_cam_process 
```

### To run grasp service:
```bash
ros2 run grasp_gen_service grasp_gen_service 
```

### To get the grasp:
```bash
ros2 service call /generate_grasp grasp_gen_interface/srv/GraspGen "{input: '{\"grasp_type\": \"generate_grasp_grconvnet\", \"crop\": [230, 191, 391, 262]}'}"
```

### For cluttered objects:
```bash
ros2 run grasp_gen_service grasp_gen_service_clutter 
```

#### open a new terminal
```bash
ros2 service call /generate_grasp grasp_gen_interface/srv/GraspGen "{input: '{\"grasp_type\": \"generate_grasp_grconvnet\", \"crop\": [230, 191, 391, 262], \"id\": _insert_id_no_}'}"
```

