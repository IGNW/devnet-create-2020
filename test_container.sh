#!/bin/bash

if docker inspect -f '{{.State.Running}}' devnet_create_2020
then
  echo Stopping the container
  docker stop devnet_create_2020
else
  echo No need to stop the container
fi