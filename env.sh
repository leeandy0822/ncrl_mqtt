#!/usr/bin/env bash

catkin_make
source devel/setup.bash
roscd mqtt_client/launch
vim params.yaml
