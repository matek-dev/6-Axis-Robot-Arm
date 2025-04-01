# 6-Axis Robotic Arm

## Overview

The **6-Axis Robotic Arm** is a custom-designed robotic manipulator featuring 3D-printed components, servo motors, and an advanced control system. Initially controlled via an Arduino microcontroller with **potentiometer-based manual control**, the project evolved to incorporate **FreeRTOS** for real-time task management, a touchscreen HMI connected through bluetooth for remote control and later integrated **ROS (Robot Operating System)** for enhanced control and automation.

## Project Life Cycle

### **Phase 1: Potentiometer-Based Manual Control**

- The robotic arm was originally controlled using **potentiometers** directly wired to an Arduino.
- Each servo motor’s movement was mapped to a corresponding potentiometer position, allowing for manual positioning.
- This phase provided a simple and direct control mechanism but lacked automation and precision.

![image](https://github.com/matek-dev/Arduino-Robot-Arm/assets/137855238/4bdfd85c-0569-41df-93ef-66a9be137099)

### **Phase 2: Arduino-Based Automated Control**

- The system was upgraded to accept predefined motion sequences through Arduino programming.
- Basic inverse kinematics were introduced to improve movement efficiency.
- The arm could execute simple pick-and-place operations autonomously.

### **Phase 3: FreeRTOS Integration**

- The control system was migrated to a **FreeRTOS-supported microcontroller**, enabling multitasking.
- Separate FreeRTOS tasks were created for motor control, sensor reading, and command processing.
- This upgrade improved real-time performance, making the system more responsive.

### **Phase 4: Human-Machine Interface (HMI) with Tkinter**

- A **GUI interface was developed using Tkinter** on a Raspberry Pi touchscreen.
- The user could send motion commands and monitor the arm’s status in real time.
- The Raspberry Pi communicated with the microcontroller via **Bluetooth**, enabling remote control.

<img width="416" alt="Screen Shot 2025-04-01 at 6 46 24 PM" src="https://github.com/user-attachments/assets/7ccba2fa-2a91-4489-bd65-d966591aaa47" />

### **Phase 5: ROS Integration (Ongoing Development)**

- The system is being integrated with **ROS Noetic/ROS2 Humble**, allowing for scalable and modular control.
- The robotic arm will be capable of being simulated and controlled through **MoveIt!**.
- Future ROS integration will include advanced motion planning, collision avoidance, and sensor feedback processing.

## Features

- **3D-Printed Structure** – Designed and printed for durability and flexibility.
- **6 Degrees of Freedom (DoF)** – Provides a wide range of motion and precision.
- **FreeRTOS Integration** – Enables multitasking and real-time control.
- **Human-Machine Interface (HMI)** – Developed using a Raspberry Pi and touchscreen with a **Tkinter-based GUI**.
- **Bluetooth Remote Control** – The HMI communicates with the microcontroller via Bluetooth for wireless operation.
- **ROS Integration (In Progress)** – Bridging the robotic arm with ROS for scalable and modular control.

## Hardware Components

- **Microcontroller**: Arduino Mega 2560 (Upgraded to a FreeRTOS-supported board)
- **Actuators**: SG90 Micro Servo Motors
- **Controller Interface**: Raspberry Pi with 7" Touchscreen HMI
- **Communication**: HC-05 Bluetooth Module (for remote control), UART/I2C/SPI (for microcontroller-ROS communication)
- **Power Supply**: External power source for servo motors

## Software Stack

- **Embedded System**: FreeRTOS for real-time scheduling
- **Control Interface**: **Python with Tkinter** for Raspberry Pi HMI
- **Robot Simulation & Control**: ROS Noetic/ROS2 (planned full integration)
- **ROS Packages**: MoveIt Motion Planning Framework
- **Firmware Development**: C/C++ for microcontroller programming

## Installation & Setup

### 1. Setting Up FreeRTOS on the Microcontroller

1. Clone the repository and install necessary dependencies:
   ```sh
   git clone https://github.com/matek-dev/Arduino-Robot-Arm.git
   cd robotic-arm
   ```
2. Flash the FreeRTOS-based firmware to the microcontroller.
3. Connect the microcontroller to the Raspberry Pi via Bluetooth for wireless communication.

### 2. Running the HMI on Raspberry Pi

1. Install dependencies:
   ```sh
   sudo apt update && sudo apt install -y python3-pip
   pip3 install tk
   ```
2. Run the HMI interface:
   ```sh
   python3 hmi/Robot_Control_GUI.py
   ```
3. Ensure the Bluetooth connection is established between the Raspberry Pi and the microcontroller.

### 3. ROS Integration (Ongoing Development)

1. Install ROS Noetic:
   ```sh
   sudo apt install ros-noetic-desktop-full
   ```
2. Initialize the ROS workspace:
   ```sh
   mkdir -p ~/catkin_ws/src
   cd ~/catkin_ws/
   catkin_make
   ```
3. Build and run the ROS node for the robotic arm.

## Future Enhancements

- **Full ROS Control** – Implement MoveIt! for path planning and motion control.
- **Computer Vision Integration** – Add an object recognition system.
- **Inverse Kinematics** – Improve motion accuracy with real-time kinematics calculations.
- **Mobile App Support** – Extend remote control capabilities using a mobile application.

## Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

## License

This project is licensed under the MIT License.

## Contact

For inquiries, reach out via LinkedIn or GitHub:

- **GitHub**: [github.com/matek-dev](https://github.com/yourusername)
- **LinkedIn**: [linkedin.com/in/matthew-koniecko](https://linkedin.com/in/matthew-koniecko)
