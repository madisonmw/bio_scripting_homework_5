#!/bin/bash

#Very simple script with simple variables. Mainly just formatting everything to look nice.

cur_date=`date`
people=`who | awk '{print $1}'`
how_long=`uptime`

printf "Please check the current directory for a file named sys_info_output.txt.\n"

printf "The current time and date is $cur_date\n\n" >> sys_info_output.txt

printf "Here is a list of all currently logged-in users:\n$people\n\n" >> sys_info_output.txt

printf "The system uptime is $how_long\n\n" >> sys_info_output.txt

echo ------------------------------------------------------------------------------ >> sys_info_output.txt
