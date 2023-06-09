# Fractal Dragon
ROS2 repository for a turtlesim Fractal dragon.

The dragon is simple, if you want to check it out you should install ROS2, Foxy etc. for the perfect inviorment.

if you got my repo you need only the .py files and the setup.py

after  you should build the repo with colcon and you can use the command below:
Set the data:
ros2 topic pub /fractal_dragon_level std_msgs/msg/Int32 "data: 25"

the 25 is a parameter you should change it smaller or bigger number if you like it.
here are some pre made commands with size i thought are cool:
- ros2 topic pub /fractal_dragon_level std_msgs/msg/Int32 "data: 7"
- ros2 topic pub /fractal_dragon_level std_msgs/msg/Int32 "data: 15"
- ros2 topic pub /fractal_dragon_level std_msgs/msg/Int32 "data: 50"

Start the node:
ros2 run ros2_course listener
this will run the turtle as manny fractals as you gave in as the parameter

Simple fractal:
ros2 run ros2_course fractal
this command draws out a fix gradient fractal  it should be gradient but it appears just red



