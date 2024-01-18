#!/usr/bin/env bash

TOOLS="rna_star cutadapt"
tool=$1

for col in d e f g h ; do
	for file in $(find results -name "*_costs_col-$col*.md") ; do
		file_parts=$(echo $file | awk -F_ '{print $(NF-2),$(NF-1)}')
		#for tool in $TOOLS ; do
		echo "$file_parts $tool $(bin/average.py -t $tool $file)"
		#done
	done
done