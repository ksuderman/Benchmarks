#!/usr/bin/env bash

if [[ $# = 0 ]] ; then
	echo "ERROR: No server provided"
	exit 1
fi

SERVER=$1

for h in rna rna-20 rna-50 ; do
	echo "Importing historu $h"
	abm $SERVER history import $h
done
abm $SERVER	workflow import rnaseq-pe
echo "Server $SERVER is ready."