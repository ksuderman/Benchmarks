#!/usr/bin/env bash

while read hid ; do
	name=$(abm c3 history show $hid | jq -r .name | awk '{print $NF}')
	echo "$hid,$name"
done < histories.txt