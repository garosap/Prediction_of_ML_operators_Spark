#!/bin/bash
count=0
while [ $count -lt 10000 ]
do
    clear
    free -m
    sleep 3
    count=$((count + 1))
done
