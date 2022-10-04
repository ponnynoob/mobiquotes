#!/bin/bash
input="quotes/all.txt"
COUNTER=1
randomNumber=$(shuf -i 1000000000-9999999999 -n1)
sed -i'' -e "s/Array(/Array($randomNumber,/g" javascript/loadQuotes.js
while IFS= read -r line
do
  if (( $COUNTER == 1000 ))
  then
    randomNumber=$(shuf -i 1000000000-9999999999 -n1)
    sed -i'' -e "s/Array(/Array($randomNumber,/g" javascript/loadQuotes.js
    let "COUNTER=1"
  fi
  
  echo "$line" >> quotes/$randomNumber.txt

  COUNTER=$[$COUNTER +1]
done < "$input"