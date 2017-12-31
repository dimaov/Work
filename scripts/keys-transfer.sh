#!/bin/bash

for (( i=1; i<5; i++)); do
	for (( j=1; j<5; j++)); do
		ssh-copy-id root@192.168.73.$i$j
	done
done
