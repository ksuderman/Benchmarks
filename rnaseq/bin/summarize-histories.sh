#!/usr/bin/env bash

if [[ $# = 0 ]] ; then
	echo "ERROR: No instance name provided"
	exit 1
fi

cloud=$1

if [[ ! -e results/$cloud ]] ; then
	mkdir results/$cloud
fi

for hid in $(abm $cloud history list | grep $cloud | awk '{print $1}') ; do
	echo "Getting name for history $hid"
	name=$(abm $cloud history show $hid | jq -r .name | tr ' ' '_')
	echo "Generating CSV for history $name"
	abm $cloud history summarize $hid > results/$cloud/$name.csv
	echo "Generating markdown for history $name"
	abm $cloud history summarize --markdown --sort-by runtime $hid > results/$cloud/$name.md
done