#!/bin/bash

# Reading data from the user's input

exec 2>/dev/null

number="^[-+]?[0-9]+\.?[0-9]*$" #Crazy regular expression accounting for all numbers.
                                #^ indicates string must start with - or +, which is made optional
                                #by ? (once or no match). \. is a literal period, allowing us
                                #to have an optional decimal via the next "?". * is zero or more
                                #matches of 0-9, and $ indicates the end of the string.

#bc is used extensively through the script. bc calls the command line calculator and allows
#floats to be used in mathematical calculations. "scale" refers to the amount of decimal places.

printf 'Please enter a number or type "exit" to quit.'
echo

while :                               #Sets a loop that allows you to keep trying until you enter a number.
do
    echo 'Enter a : '
    read a
    if [[ $a == "exit" ]] ; then      #Allows you to exit the script. Not really necessary but it's cool.
        exit
    elif ! [[ $a =~ $number ]] || [[ -z $a ]] ; then #If the input is not a number or blank the script cycles. || indicates "or."
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
    elif ! [[ $b =~ $number ]] || [[ -z $b ]] ; then
        echo 'Please enter a number or type "exit" to exit.'
    else
            break
    fi
done

echo

add=`echo "scale=3 ; $a+$b" | bc`

echo Addition of a and b is $add

sub=`echo "scale=3 ; $a- $b" | bc`
echo Subtraction of a and b is $sub

mul=`echo "scale=3 ; $a*$b" | bc`
echo Multiplication of a and b is $mul

div=`echo "scale=3 ; $a / $b" | bc`
if [[ $b == 0 ]] ; then               #Message indicating 0 division is impossible. Replaces the ugly error message.
    printf "Division of a and b is nothing! You can't divide by 0!\n"
else
echo Division of a and b is $div
fi

mod=`echo "$a % $b" | bc`
if [[ $b == 0 ]] ; then
    printf "Modulus of a and b is nothing! You can't divide by 0!\n"
else
echo Modulus of a and b is $mod
fi

inc=`echo "var=$a ; ++var" | bc`
echo Increment operator when applied on "a" results into a = $inc

dec=`echo "var=$b ; --var" | bc`
echo Decrement operator when applied on "b" results into b = $dec

((--c))
echo What was the default value\ of c if its value is now $c\?
echo If c is now $c, the original value must be 0
