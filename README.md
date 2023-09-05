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

#### SIMPIFY SSH AND SOURCING ROS 
1. To enter ssh from CUDA11
```bash
bash nimbrossh.sh
```
2. To source ROS workspace
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


### ERRORS AND NEED FIXES
1. Need sudo to install ceres dependency on CUDA11 desktop
```bash
CMake Error at /home/roblab/Documents/clins_ws/src/clins/CMakeLists.txt:50 (find_package):
  By not providing "FindCeres.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Ceres", but
  CMake did not find one.

  Could not find a package configuration file provided by "Ceres" with any of
  the following names:

    CeresConfig.cmake
    ceres-config.cmake

  Add the installation prefix of "Ceres" to CMAKE_PREFIX_PATH or set
  "Ceres_DIR" to a directory containing one of the above files.  If "Ceres"
  provides a separate development package or SDK, be sure it has been
  installed.


cd /home/roblab/Documents/clins_ws/build/clins; catkin build --get-env clins | catkin env -si  /usr/bin/cmake /home/roblab/Documents/clins_ws/src/clins --no-warn-unused-cli -DCATKIN_DEVEL_PREFIX=/home/roblab/Documents/clins_ws/devel/.private/clins -DCMAKE_INSTALL_PREFIX=/home/roblab/Documents/clins_ws/install; cd -

.............................................................................................................................................................................................................................................................................................................................
Failed     << clins:cmake                          [ Exited with code 1 ]                                                                                                                                                                                                                                                    
Failed    <<< clins                                [ 1.8 seconds ]                                                                                                                                                                                                                                                           
[build] Summary: 1 of 2 packages succeeded.                                                                                                                                                                                                                                                                                  
[build]   Ignored:   None.                                                                                                                                                                                                                                                                                                   
[build]   Warnings:  None.                                                                                                                                                                                                                                                                                                   
[build]   Abandoned: None.                                                                                                                                                                                                                                                                                                   
[build]   Failed:    1 packages failed.                                                                                                                                                                                                                                                                                      
[build] Runtime: 2.7 seconds total.                                                                                                                                                                                                                                                                                          
[build] Note: Workspace packages have changed, please re-source setup files to use them.
roblab@cuda11:~/Documents/clins_ws/src$ sudo apt-get install libceres-dev
[sudo] password for roblab: 
roblab is not in the sudoers file.  This incident will be reported.
```
