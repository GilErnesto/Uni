#!/bin/bash
# Calculate the sum of a series of numbers.
SCORE="0"
SUM="0"
MEDIA="0"
NUM="0"
while true
do
	echo -n "Enter your score [0-10] ('q' to quit): "
	read SCORE;

	if [[ "$SCORE" == "r" ]]; then
                SUM=0
                NUM=0
                echo "Count and sum reset."

	elif (("$SCORE" < "0")) || (("$SCORE" > "10")); then
		echo "Try again: "
	elif [[ "$SCORE" == "q" ]]
	then
		MEDIA=$((SUM / NUM))
		echo "Sum: $SUM."
		echo "Media: $MEDIA."
		break
	else
		SUM=$((SUM + SCORE))
		NUM=$((NUM + 1))
	fi
done
echo "Exiting."
