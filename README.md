# carl_cv

This repository contains two simple ROS2 (Foxy) nodes for publishing and subscribing to video frames generated by the Pi Camera onboard the CARL robot.

The img_publisher node is run on the CARL robot, and the img_subscriber node can then be run from a remote Linux workstation on the same local area network (LAN).  A window will pop up on the remote Linux workstation showing a feed of the video from the CARL robot, enabling a teleoperator to navigate the robot manually (utilizing the teleop_carl node from the carl_ros2foxy_baseline package).

To install, clone this repo to your {ROS2 Workspace}/src/ folder.  Then navigate to your {ROS2 Workspace}/ directory and execute 'colcon build --packages-select carl_cv'