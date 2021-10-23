#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Paremeter needed. State number of executions"
    exit 1
fi


for i in $(eval echo {1..$1});
  do
    python3 ./main.py;
done

# reading dictionary usually takes around 2 seconds
a=$(echo "$1 * 2" | bc)

total=$(echo "$SECONDS-$a" | bc)
echo "Elapsed time while not reading dictionary: $total"
