#!/bin/bash -x

originalDir=$PWD
mgScript=$1
mg5=$2
output=$3

cd /afs/cern.ch/user/a/aschuy/work/private/VBS_WGamma/muon_collider/event-generation
source setup.sh
cd $output
$mg5 < "${mgScript}"
cd $originalDir