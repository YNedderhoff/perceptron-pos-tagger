#!/bin/bash

CORPORA="../team-lab-ss2015/data/pos"

total=10

for (( j=1; j<=$(( $total )); j++ )) do
    screen -dmS "10_fold_cross_"$j python -u 10-fold-cross-validation.py -i $CORPORA/train.col -t $j -s 10 -o1 $CORPORA/one_fold_$j.col -o2 $CORPORA/nine_folds_$j.col
    
done
