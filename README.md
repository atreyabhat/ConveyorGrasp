# Vision-Based Robotic Manipulation: Pick-and-Place from Moving Conveyors

This project develops a robotic system for precise pick-and-place operations on moving conveyor belts, focusing on dynamic and cluttered environments. A dual-camera setup ensures reliable object detection, tracking, and grasping using fine-tuned algorithms and real-time control.

---

## Key Features
- **Dual-Camera System**:
  - Overhead camera for initial object detection and tracking.
  - Eye-in-hand camera for position correction near the grasp point.
- **Algorithmic Integration**:
  - **YOLO**: Object detection fine-tuned on YCB dataset.
  - **GRConvNet**: Grasp synthesis with RGB-D inputs for real-time grasp generation.
- **Dynamic Control Loop**: Real-time end-effector adjustments based on object position updates and grasp planning.

---

## Implementation
1. **Object Detection**:
   - Overhead camera detects objects and tracks their movement.
   - In-hand camera refines object positions for final grasp.
2. **Grasp Planning**:
   - GRConvNet generates grasp parameters, including position, angle, and gripper width.
3. **Motion Control**:
   - MoveIt framework handles manipulator movement and end-effector adjustments.
4. **End-to-End Process**:
   - Objects are detected, tracked, re-evaluated dynamically, grasped, and placed.

---

## Results
- **Position Error Robustness**: Corrects position errors up to 9 cm.
- **Conveyor Speed**: Reliable grasps at speeds up to 0.04 m/s.
- **Clutter Handling**: Adaptive cropping improves accuracy in dense environments.


![image](https://github.com/user-attachments/assets/8a3769be-1846-4550-ab78-e30d3b7b74c3)

![image](https://github.com/user-attachments/assets/0ea7376b-f661-4d98-a26e-9ef2719abae5)


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

