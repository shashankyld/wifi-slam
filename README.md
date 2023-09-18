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
28. [DONE] Install eduroam-cs connection
```bash
https://www.hrz.uni-bonn.de/en/all-services/internet-network-access/wifi-eduroam-reinstallation
```
29. [DONE] Fix time for wifi topic
30. Visuaize colour coded path based on the wifi reception
31. Trianguate wifi based on different assumptions of signal propagation
32. Read Frank Dellaert's report on factor graphs for clarity and revision
```bash
https://www.annualreviews.org/doi/pdf/10.1146/annurev-control-061520-010504
```
33. Try to think of a better way to initialize wifi based edge than track method proposed in the paper
34. alternatives to iwlist
```bash
nmcli device wifi list
```
35. Write ROS Node for
```bash
sudo airodump-ng wlx00c0cab04510 | grep iPhone
```
36. Clear all airodump threads
37. ```bash
    sudo setcap cap_net_raw=eip ./your_program
    ```
38. Figure out if you can update airodump-ng csv at a faster rate
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
1. "." is "~" or home for rsync (for PC from which we are transfering file)
2. "." is current directory (for PC to which we are transfering file)
3. --progress shows the progress
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
```bash
# Try this
nmcli device wifi list ifname wlx00c0cab04510
```
```bash
# Aternatives to iwlist
Between iwlist and airodump-ng, airodump-ng is generally faster for scanning and providing real-time updates
about nearby Wi-Fi networks and their associated devices. airodump-ng is a powerful tool specifically designed
for Wi-Fi network monitoring and packet capturing. It can continuously scan and update the information about
Wi-Fi networks, including signal strength, encryption, and connected devices, at a high frequency.

On the other hand, iwlist is a simpler command-line utility for scanning Wi-Fi networks and provides a
static snapshot of available networks at the time of the scan. It doesnt continuously update the information
in real-time, and you would need to run it multiple times to see changes in network status as the environment changes.

If you need to monitor Wi-Fi networks in real-time, especially for applications like robotics or tracking
signal changes as a device moves, airodump-ng or similar Wi-Fi monitoring tools are more suitable due to
their ability to provide continuous updates. However, keep in mind that airodump-ng is typically used for
monitoring and security assessment, so it may require additional configuration and permissions to run.

In summary, if you require real-time network scanning and updates, airodump-ng is the faster and more appropriate choice.
1. iwlist (snapshot of the last scan)
2. airodump-ng (online continous updates - test)
3. pywifi (python - not updating -tested)
4. nmcli (updates but very very slow - 1/10 hz)
```
```bash
## TO RUN WIFI PUBLISHER - airodump-ng - Updates real time
# 1. Delete existing file and Launch airodump-ng
find /home/nimbro_home/lidar_ws/src/wifi_lookup/src/ -type f -name 'airodump*.csv' -exec rm {} \; && sudo airodump-ng wlx00c0cab04510 --output-format csv -w /home/nimbro_home/lidar_ws/src/wifi_lookup/src/airodump | grep iPhone
# 2. Launch wifi data pubisher that reads the csv
rosrun wifi_lookup wifi_airodump_publisher.py
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

#### CHECK THESE REPOS
1. https://github.com/RMiyagusuku/ros-wifi-localization/tree/master
2. http://wiki.ros.org/rtabmap_ros/Tutorials/WifiSignalStrengthMappingUserDataUsage#How_to_Publish_User_Data_.28wifi_signal_pub.29
3. https://github.com/aircrack-ng/aircrack-ng/discussions/2574#discussioncomment-7026621
4. https://github.com/clearpathrobotics/wireless


## ROBOT LOCATION 
-----------------1



-----------------2

1 :
```bash
 00:F6:63:81:CA:32  -62       32        0    0   6  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:2C:34:F2  -48       54       16    0  11  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:AD:7F:72  -51       56        0    0   1  195   WPA  CCMP   MGT  eduroam-cs
```
1 rotated:
```bash

 00:F6:63:2C:34:F2  -43       11        0    0  11  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:AD:7F:72  -56       13        0    0   1  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:81:CA:32  -63        4        0    0   6  195   WPA  CCMP   MGT  eduroam-cs
```

2:
```bash
 00:F6:63:AD:7F:72  -43       22        0    0   1  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:2C:34:F2  -61       20        0    0  11  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:9E:C9:C2  -62       17        0    0   6  195   WPA  CCMP   MGT  eduroam-cs

 (not associated)   5C:61:99:44:5E:F7  -46    0 - 1      0        1         eduroam-cs                                                                        
 (not associated)   6E:2F:6E:2F:27:24  -52    0 - 1      0        2         eduroam-cs                                                                        
 (not associated)   6E:35:16:F5:FF:88  -62    0 - 5      0        1         eduroam-cs  
```

2 rotated:
```bash
 00:F6:63:AD:7F:72  -39        7        0    0   1  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 00:F6:63:2C:34:F2  -56        6        0    0  11  195   WPA  CCMP   MGT  eduroam-cs                                                                        
 (not associated)   6E:35:16:F5:FF:88  -63    0 - 5      0        2         eduroam-cs
```
