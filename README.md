# WiFi-SLAM

WiFi Augmented Loop Closure

## TO-Do
1. Create node to pubish
   ```
   iwlist scan
   ```
2. Find out other information about wifi received data like AOA, phase, ...
3. Improve node with extra info
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

#### SOME FACTS
1. A Single router can have mutipe NICs
2. A singe NIC can have ony a singe SSID and channel
3. Two different NICs from a single router can have same SSID and channel

#### SOME IDEAS
1. Channel State Information (CSI) from Wi-Fi signals to predict Angle of Arrival (AoA) 
