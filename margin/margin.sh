#!bin/sh
echo "Calculating Margin"
echo
echo
echo "Enter total no of hours: "
read no_t
echo
echo "Enter the no of hours absent: "
read no_a
echo

percent=( $no_t - $no_a)/($no_t *100)
margin=( $no_t *0.7)-($no_t -$no_a)
echo "The attendence percentage is :" $percent
echo
echo "The margin is :" $margin

