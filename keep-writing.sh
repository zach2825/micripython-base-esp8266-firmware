#!/usr/bin/env bash

while :;
do
    ampy reset && ./connect.sh;

    echo "Waiting 2 seconds and re-running. This timeout is to allow you to press ctrl+c to kill the script";
    sleep 2

    ./copy-all.sh;
done