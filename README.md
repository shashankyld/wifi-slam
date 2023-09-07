# WiFi-SLAM

WiFi Augmented Loop Closure

## TO-Do
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
8. Apply static transform for the lidar with respect to body!
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
13. RUN CLINS on recorded data - current issue is "ring" field is not present in all the points of a scan
14. https://robotics.stackexchange.com/questions/89543/failed-to-find-match-for-field-intensity-with-ouster-lidar
15. Write a launch file for recording data
16. Write a launch file to view Rviz


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
rsync -ravh --progress nimbro_home@10.7.3.130:./lidar_ws/src/rosbag_fancy/rosbag_fancy/sensor_data/bag1.bag ./Documents/nimbro_data
```

#### SOME FACTS REGARDING WIFI
1. A Single router can have mutipe NICs
2. A singe NIC can have ony a singe SSID and channel
3. Two different NICs from a single router can have same SSID and channel\

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
3. clins package is places inside the clins_ws in CUDA11
4. Build clins workspace

   
