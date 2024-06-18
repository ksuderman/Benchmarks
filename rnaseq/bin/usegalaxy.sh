#!/usr/bin/env bash

# Generate runtime averages from the markdown file for the usegalaxy experiment

DATASETS='SRR24043307-20  SRR24043307-50 SRR24043307-full'

echo "Tool, Dataset, Runtime, Memory"
for tool in rna_star cufflinks ; do
	for dataset in $DATASETS ; do	
# 		echo "$tool $dataset"
		bin/colavg.py --filter $tool --filter $dataset --columns 5,6 results/usegalaxy.md
	done
done

