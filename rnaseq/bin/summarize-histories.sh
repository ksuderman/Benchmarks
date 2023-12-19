#!/usr/bin/env bash

for hid in $(abm costs history list | grep costs | awk '{print $1}') ; do
	name=$(abm costs history show $hid | jq -r .name | tr ' ' '_')
	echo "Getting results for history $hid $name"
	abm costs history summarize $hid > results/$name.csv
	abm costs history summarize --markdown --sort-by runtime $hid > results/$name.md
done