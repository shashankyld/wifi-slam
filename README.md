# WiFi-SLAM

WiFi Augmented Loop Closure

## TO-Do
1. [DONE] Create node to pubish
   ```
   iwlist scan
   ```
2. Find out other information about wifi received data like AOA, phase, ...
3. Improve node with extra info
4. Install clins(Lidar-Inertial SLAM) on Cuda11 as it is computationally heavy and works better offline
```shell
https://github.com/JanQuenzel/clins
```
6. Use fancy-bag library
```shell
https://github.com/xqms/rosbag_fancy
```
7. [DONE] Move the wifi package to the lidar_ws
```shell
# Current location inside tiago
~/Documents/wificlosure/wifi_ws/src
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

### Important launch files
To launch the fisheye camera
```shell
roslaunch camera_v4l2 brio.launch 
```
To launch the ouster lidar parallel to fisheye camera 
```shell
roslaunch ouster_ros driver.launch 
TODO: Add lidar, camera, imu, wifi, and bag record node - all in one launch file
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
