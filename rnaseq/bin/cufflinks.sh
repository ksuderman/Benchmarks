#!/usr/bin/env bash

DATASETS="SRR24043307 SRR24043307-50 SRR24043307-full"
COLUMNS="d e f g h"
INPUT_FILE=results/combined.md

for data in $DATASETS ; do
	for col in $COLUMNS ; do
		echo "$data col-$col $(bin/average.py $INPUT_FILE -t cufflinks -f col-$col)"
	done
done