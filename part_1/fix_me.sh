#!/bin/bash

# Reading data from the user's input

#pos_int="^[0-9]+$" Originally had this set as a variable. However, the variable "number"
#accounts for positives and negatives, so it's not required to set a variable.

printf "Please no decimal numbers!\n"

while :                               #Sets a loop that allows you to keep trying until you enter a number.
do
    echo 'Enter a : '
    read a
    if [[ $a == "exit" ]] ; then      #Allows you to exit the script. Not really necessary but it's cool.
        exit
    elif ! [[ $a =~ $number ]] ; then #If the input is not a number the script cycles.
        echo 'Please enter a number or type "exit" to exit.'
    else
            break                     #Stops the infinite loop once the condition of a number is met.
    fi

done

#I found out that you have to set the "exit" condition first before the second one. If the condition where
#$a isn't equal to a number is set first, it ignores the exit condition as it sees "exit" as not a number.

while :
do
    echo 'Enter b : '
    read b
    if [[ $b == "exit" ]] ; then
        exit
    elif ! [[ $b =~ $number ]] ; then
        echo 'Please enter a number or type "exit" to exit.'
    else
            break
    fi
done

add=$((a + b))

echo Addition of a and b are $add

sub=$((a - b))
echo Subtraction of a and b are $sub

mul=$((a * b))
echo Multiplication of a and b are $mul

div=$((a / b))
echo division of a and b are $div

mod=$((a % b))
echo Modulus of a and b are $mod

((++a))
echo Increment operator when applied on "a" results into a = $a

((--b))
echo Decrement operator when applied on "b" results into b = $b

((--c))
echo What was the default value \ of c if its value is now $c\?
