# ncrl_mqtt

This repo is the docker for mqtt_ros of Ubuntu 20.04.
Edit from https://github.com/ika-rwth-aachen/mqtt_client 

- Environment Setup
```bash
source env.sh
```
- Change the broker port to your custom IP address
```bash
cd ~/catkin_ws/src/mqtt_client/launch
vim params.yaml
```
- Run the mqtt-ros serviece
```bash
roslaunch mqtt_client standalone.launch
```
