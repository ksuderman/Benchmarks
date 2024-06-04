#!/usr/bin/env bash

#input_file=results/Single-Cell-Experiment.md
input_file=results/VC-2.md
#tool_list=$(cat $input_file | tail -n +3 | awk -F\| '{print $5}' | sort -u)
for data in 2GB 5GB 10GB ; do
  echo $data
  while read tool ; do
#    echo $tool
#    value=$(bin/colavg.py $input_file -c 11,14 --filter $data $tool ok | tail -n 2 | head -n 1 | awk -F: '{print $2}')
    memory=$(bin/colavg.py $input_file -c 5,6 --filter $data $tool ok | tail -n 1 | awk -F: '{print $2}')
#    value=$(bin/colavg.py $input_file -c 5,6 --filter $data $tool ok | tail -n 2 | head -n 1 | awk -F: '{print $2}')
#    bin/colavg.py $input_file -c 11,14 --filter $data $tool ok
    echo $memory
#    echo $tool
  done < tool-list-versioned.txt
  echo
done
exit

for tool in $(cat $1 | awk -F\| '{print $5}' | tail -n +3 | sort -u) ; do
	runtime=$(../rnaseq/bin/colavg.py $1 -c 3,4 -f $tool ok | tail -n 2 | head -n 1 | awk -F: '{print $2}')
	echo "\"$tool\"	$runtime"
	#echo $tool
#	../rnaseq/bin/colavg.py $1 -c 3,4 -f $tool ok
done