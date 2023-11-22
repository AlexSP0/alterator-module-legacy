#!/bin/bash

export DISPLAY=:0
clean_up=1
if /usr/bin/xhost | tail -n+2 | grep -Fxq "SI:localuser:root"
then
	clean_up=0 
else
	/usr/bin/xhost +SI:localuser:root
fi

/usr/sbin/alterator-standalone $1
	
if [ "$clean_up" -eq 1 ]
then
	/usr/bin/xhost -SI:localuser:root
fi
