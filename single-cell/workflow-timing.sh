#!/usr/bin/env bash

#input_file=results/Single-Cell-Experiment.md
input_file=results/10k.md
tool_list=$(cat $input_file | tail -n +3 | awk -F\| '{print $5}' | sort -u)
for data in 10k_ ; do
  echo $data
  for tool in $tool_list ; do
    memory=$(../rnaseq/bin/colavg.py $input_file -c 5,6 --filter $data $tool ok | tail -n 1 | awk -F: '{print $2}')
    echo $memory
  done
done
exit

for tool in $(cat $1 | awk -F\| '{print $5}' | tail -n +3 | sort -u) ; do
	runtime=$(../rnaseq/bin/colavg.py $1 -c 5,6 -f $tool ok | tail -n 2 | head -n 1 | awk -F: '{print $2}')
	echo "\"$tool\"	$runtime"
	#echo $tool
#	../rnaseq/bin/colavg.py $1 -c 3,4 -f $tool ok
done