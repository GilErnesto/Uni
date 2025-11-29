#!/bin/bash
#This script opens 4 terminal windows.
i="0"
while [[ $i -lt 4 ]]
do
	kitty &
	i=$(($i+1))
done
