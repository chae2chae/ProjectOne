echo "export ROS_DOMAIN_ID=30" #TURTLEBOT3 >> ~/.bashrc
source ~/.bashrc
sudo apt update
sudo apt install libudev-dev
cd ~/turtlebot3_ws/src
git clone -b humble-devel https://github.com/ROBOTIS-GIT/ld08_driver.git
cd ~/turtlebot3_ws/src/turtlebot3 && git pull
rm -r turtlebot3_cartographer turtlebot3_navigation2
cd ~/turtlebot3_ws && colcon build --symlink-install
echo 'export LDS_MODEL=LDS-01' >> ~/.bashrc
source ~/.bashrc

# OpenCR
sudo dpkg --add-architecture armhf
sudo apt update
sudo apt install libc6:armhf

export OPENCR_PORT=/dev/ttyACM0
export OPENCR_MODEL=burger
rm -rf ./opencr_update.tar.bz2

wget https://github.com/ROBOTIS-GIT/OpenCR-Binaries/raw/master/turtlebot3/ROS2/latest/opencr_update.tar.bz2
tar -xvf ./opencr_update.tar.bz2

cd ~/opencr_update
./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr