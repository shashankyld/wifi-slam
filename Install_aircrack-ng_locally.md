## Steps to install aircrack-ng(airodump-ng) locally

1. Download source code
```bash
https://github.com/aircrack-ng/aircrack-ng
```
2. Install dependencies
```bash
sudo apt-get install build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libpcap-dev libsqlite3-dev libpcre2-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils expect
```
3. Run pre-configure script in the source folder
```bash
autoreconf -i
```
or 
```bash
env NOCONFIGURE=1 ./autogen.sh
```
4. Configure Installation Location (Modify Prefix and Libdir if needed):
```bash
# Replace /home/roblab/local with your desired installation directory.
./configure --with-experimental --prefix=/home/roblab/local --libdir=/home/roblab/local/lib
```
5. Compile Aircrack-ng
```bash
make
```
6. Install
```bash
make install
```
7. Add Aircrack-ng binaries to the PATH
```bash
export PATH="/home/roblab/local/bin:$PATH"
```
8. Source shell profile
```bash
source ~/.bashrc
```
9. Run the aircrack-ng command
```bash
~/local/bin/aircrack-ng
```
10. Run the airodump-ng command
```bash
# Give full path to the bin, incase required
~/local/bin/aircrack-ng airodump-ng
# For Nimbro_home
/home/nimbro_home/aircrack/local/bin/
```
