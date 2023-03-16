#!/usr/bin/env bash

source devel/setup.bash
catkin_make
roscd mqtt_client/launch
vim params.yaml
