# robo_base

## Required Packages
`sudo apt-get install ros-melodic-teb-local-planner`  
`sudo apt-get install ros-melodic-eband-local-planner`  
`sudo apt-get install ros-melodic-move-base-sequence`   
`sudo apt-get install ros-melodic-cartographer-ros`  
`sudo apt-get install ros-melodic-cartographer-rviz`  
`sudo apt-get install ros-melodic-ira-laser-tools`  


## Simulation

**robo_base** is a mecanum wheel robot devoeloped on ROS melodic.  
Current sensors used are:
- Wheel Encoders
- LIDAR

## Resources
- [Turtlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)
## Launch Simulation World
starts the simulation in Gazebo  
`roslaunch robo_base_gazebo robo_base_house.launch`   
or for the robot with 2 laser scanner    
`roslaunch robo_base_gazebo robo_base_house.launch model:=robot_2lidar`
use  
`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`  
to controll the robot manually with "ijkl,"  
or try  
`roslaunch robo_base_slam robo_base_slam.launch slam_methods:=explore`  
for autonomous exploration

## SLAM 
to start gmapping  
`roslaunch robo_base_slam robo_base_slam.launch`  
if you still have teleop running you can now move around and generate a map.

## save map
PS: don't close gazebo and rviz before you haven't saved the map  
cd into folder where you want to save the map  
`rosrun map_server map_saver -f <map_name>`

## Navigation
close the SLAM node.  
the map and the world need to match, you can change the map with ,map_file:=$HOME/maps/map.yaml. With the path to the yaml file.  
`roslaunch robo_base_navigation robo_base_navigation.launch map_file:=$HOME/maps/map.yaml`  
or  
`roslaunch robo_base_navigation robo_base_navigation.launch planner:=move_base_eband model:=robot_2lidar`  



## move to navigation goal
`roslaunch simple_navigation_goals move_base_seq.launch`   
move to a single goal which is hardcoded in the simple_navigation_goals.py file.   
`roscd simple_navigation_goals/scripts/`  
`python simple_navigation_goals.py`  
  
move to several locations sequantually, specified in the launch file as "p_seq">[x,y,z,...]
`roslaunch simple_navigation_goals movebase_seq.launch`

## Resources
- [Gazebo/Fusion to navigation Youtube tutorial](https://www.youtube.com/watch?v=o7w7yv-Nros&list=PLFnCFnTZNyU8-omA_VFztWfeFn2gCyY4_)
- [Another Gazebo/Fusion to mapping Youtube tutorial](https://www.youtube.com/watch?v=cQh0gNfb6ro&list=PLXM8kq-f3YucvPdqchLU22WfUfjKCIqlO_)
- [Gazebo plugins](http://gazebosim.org/tutorials?tut=ros_gzplugins_)
- [move to navigation goals](https://hotblackrobotics.github.io/en/blog/2018/01/29/seq-goals-py/_)