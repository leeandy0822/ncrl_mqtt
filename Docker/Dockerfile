FROM softmac/sdc-course-docker:latest


RUN sudo apt-get -o Acquire::ForceIPv4=true update && sudo apt-get -o Acquire::ForceIPv4=true install -q -y \
        vim \ 
        git

RUN git clone https://github.com/ika-rwth-aachen/mqtt_client.git
WORKDIR /root/catkin_ws/src/mqtt_client
RUN rosdep install -r -y --ignore-src --from-paths .
WORKDIR /root/catkin_ws
