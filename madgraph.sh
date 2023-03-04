#!/bin/bash

originalDir=$PWD
mgScript=$1
mg5=$2
output=$3

echo "mgScript: $mgScript"
echo "mg5: $mg5"
echo "output: $output"

cd /home/schuya/muon_collider/event-generation
source setup.sh
cd $output
$mg5 < "${mgScript}"
cd $originalDir