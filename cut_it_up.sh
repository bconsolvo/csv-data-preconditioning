#!/bin/bash

#END=end of loop (starts from 1 if i=1)
END=4
i=1

while [ $i -le $END ]
do 

csv_cuts.py name${i}.csv 

i=$(($i+1))

done


