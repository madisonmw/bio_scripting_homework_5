#!/bin/bash

# Reading data from the user's input

number='^[0-9]+$' #Setting a variable through regular expression. ^ indicates matching the beggining
                  #of a line. + matches one or more occurences of the expression. $ matches
                  # the regular expression to the end of a line.

echo 'Enter a : '
read a
if ! [[ $a =~ $number ]] ; then #If the input is not a number, the script exits.
    echo "Please enter a number!"
    exit
fi

echo 'Enter b : ' 
read b

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
