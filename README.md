# WiFi-SLAM

WiFi Augmented Loop Closure

## TO-Do in chronological order
1. [DONE] Create node to pubish
   ```
   iwlist scan
   ```
2. [Not Possible on the hardware] Find out other information about wifi received data like AOA, phase, ...
3. [Not neccessary] Improve node with extra info
4. [DONE] Install clins(Lidar-Inertial SLAM) on Cuda11 as it is computationally heavy and works better offline
```shell
https://github.com/JanQuenzel/clins
```
6. [DONE] Use fancy-bag library [added by Jan]
```shell
https://github.com/xqms/rosbag_fancy
```
7. [DONE] Move the wifi package to the lidar_ws
```shell
# Current location inside tiago
~/Documents/wificlosure/wifi_ws/src
```
8. [DONE] Apply static transform for the lidar with respect to body!
```bash
package='tf2_ros',
executable='static_transform_publisher',
arguments=['0.15', '0.00', '-0.07',  '-0.92', '0.00', '-0.38', '-0.00', 'torso_lift_link', 'os_sensor'],
parameters=[],
output='screen' 
```
9. [DONE] Record Data of Lidar, Camera, IMU, Wifi
10. [DONE] Understand CLINS supported datatype - timestamp for every point in the point cloud
11. [NOT REQUIRED - ouster already has timestamps] Create CLINS supported data from recorded bag or create a node that publishes clin supported format
12. [DONE] Run CLINS on downloaded data
13. [JAN FIXED IT] RUN CLINS on recorded data - current issue is "ring" field is not present in all the points of a scan
```bash
https://robotics.stackexchange.com/questions/89543/failed-to-find-match-for-field-intensity-with-ouster-lidar
```
15. [DONE] Write a launch file for recording data
16. [DONE] Write a launch file to view Rviz
17. [DONE] Run CLINS on empty_lab.bag
18. Write some code to understand wifi networks strength based on position
19. [DONE] Understand why iwlist gives 0 networks sometimes - [Not completely sure, but using sudo solves the issue but is slower]
20. [DONE] Install Open3D on the Cuda11
21. [DONE] Run kiss-icp on the empty_lab.bag - drifiting behaviour observed for dataset with jerky motion
22. Get Nimbro URDF to visuaize as well as to have transforms between sensor and the robot
23. Look for fish-eye monocular slam systems - [OrbSLAM3 paper says that they provide fish-eye camera support]
24. check out ORBSLAM-3 docker from the lab
25. inverse-wifi model
```bash
# Need to verify before using this
FSPL (dB) = 20log10(d) + 20log10(f) + K

d = distance
f = frequency
K= constant that depends on the units used for d and f
If d is measured in kilometers, f in MHz, the formula is:

FSPL (dB) = 20log10(d)+ 20log10(f) + 32.44
```
```bash
d = 10** [( dB-32.44 - 20log10(f) ) / 20]
https://stackoverflow.com/questions/11217674/how-to-calculate-distance-from-wifi-router-using-signal-strength
```
26. Install OrbSLAM3 dependencies
```bash
# Pangolin
# C++11 or C++0x Compiler
# Eigen3
# OpenCV
# DBoW2 and g2o (Included in Thirdparty folder)
```
27. Explore OrbSLAM3 Docker
```bash
https://github.com/shashankyld/orbslam3_ROS
```
28. Install eduroam-cs connection
```bash
https://www.hrz.uni-bonn.de/en/all-services/internet-network-access/wifi-eduroam-reinstallation
```
29. Fix time for wifi topic
30. Visuaize colour coded path based on the wifi reception
31. Trianguate wifi based on different assumptions of signal propagation
32. Read Frank Dellaert's report on factor graphs for clarity and revision
```bash
https://www.annualreviews.org/doi/pdf/10.1146/annurev-control-061520-010504
```
## Usage

### SSH Access

To SSH into the system from your personal PC with a LAN cable connection, use the following command:

```shell
ssh nimbro_home@192.168.3.130
```


To ssh from cuda11 with connection through Wifi!

```shell
ssh nimbro_home@10.7.3.130
```

#### SIMPIFY SSH AND SOURCING ROS 
1. To enter nimbro_home ssh from CUDA11
```bash
bash nimbrossh.sh
```
2. To source ROS workspace in nimbro_home
```bash
source wifislam.sh
```



### Important launch files
To launch the fisheye camera
```shell
roslaunch camera_v4l2 brio.launch 
```
To launch the ouster lidar parallel to fisheye camera 
```shell
roslaunch ouster_ros driver.launch
```
To launch lidar, camera, imu, wifi - all in one launch file
```shell
cd ~/lidar_ws/scripts && roslaunch run_sensors.launch 
```
To start rosbag_fancy recorder
```bash
# YET TO DO
cd ~/lidar_ws/src/rosbag_fancy/rosbag_fancy/sensor_data && rosbag_fancy record -o <name>.bag /ouster/points /ouster/imu /brio/image_raw/compressed /brio/camera_info /tf /tf_static /wifi_data

```
#### To copy files between machines
1. "." is "~" or home for rsync
2. --progress shows the progress
```bash
# Nimbro_home to Cuda11 (from Cuda11 terminal)
rsync -ravh --progress nimbro_home@10.7.3.130:./lidar_ws/src/rosbag_fancy/rosbag_fancy/sensor_data/bag1.bag ./Documents/nimbro_data
# Cuda11 to Nimbro_home (from Nimbro_home terminal)
rsync -ravh --progress /home/roblab/Documents/nimbro_data/URDF nimbro_home@10.7.3.130:./lidar_ws/src/nimbro_urdf
```

#### Echoing topic on another machine
When we transfer bag file, from nimbro robot to cuda11 pc, and we run bag file in cuda11 pc, we cannot echo ```/wifi_data``` topic, since we defined our own message type on nimbro pc, and that message type is not build on cuda11, so it cannot be echoed.
#### To open chrome in the nimbro
```bash
~/chrome/opt/google/chrome/chrome
```

#### SOME FACTS REGARDING WIFI
1. A Single router can have mutipe NICs
2. A singe NIC can have ony a singe SSID and channel
3. Two different NICs from a single router can have same SSID and channel
4. Wifi port:
```bash
wlx00c0cab04510
```
#### Workspaces used 
1. lidar_ws contains ouster, camera, and wifi packages - located in the ~ directory of tiago.
2. imu is on the ouster lidar and so ouster package pubishes imu data as well.

#### SOME IDEAS
1. Channel State Information (CSI) from Wi-Fi signals to predict Angle of Arrival (AoA) 


### ALL ABOUT CLINS
#### Installing clins - ROS
1. Need sudo to install ceres dependency on CUDA11 desktop
```bash
#Installed ceres seperately
```
2. Sophus is a dependency - this is cloned in subdirectory of the clins package
```bash
https://github.com/strasdat/Sophus.git
```
3. clins package is placed inside the clins_ws in CUDA11
4. Build clins workspace

#### CLINS Output
Here is the data with the ROS Timestamps
```~/.ros/clins_after_map_poses.txt```

Here is the data with relative Timestamps:
```/home/roblab/Documents/nimbro_data/bag_file_name/```

#### Fixing nimbro or a new lidar/imu system errors for CLINS
1. Change "ring" from int8 to int16
2. Change transformation between imu an lidar

#### PROBLEMS
1. rospy returns same timestamps for all fingerprints. I do not know why? We have to correct that, when we find out why
   
