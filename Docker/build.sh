#!/bin/sh
docker build --rm --build-arg USER_ID=$UID -t leeandy90833/ncrl:ncrl_mqtt .