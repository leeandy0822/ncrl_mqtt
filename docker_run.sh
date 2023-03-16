#!/usr/bin/env bash
xhost +local:

    docker run \
    -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -p 2233:22 \
    --rm \
    --name ncrl_mqtt \
    --user root \
    --network host \
    -e GRANT_SUDO=yes \
    -v ~/ncrl_mqtt:/root/catkin_ws \
    leeandy90833/ncrl:ncrl_mqtt \
    bash