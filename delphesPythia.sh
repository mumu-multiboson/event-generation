#!/bin/bash
lhe=$1
echo "input lhe = $lhe"
delphes_dir=$2
echo "delphes dir = $delphes_dir"
delphes_card=$3
echo "delphes card = $delphes_card"
cd $delphes_dir/..
source setup.sh
cd $delphes_dir
output=${lhe%%.lhe}.root  #set delphes output path/name
echo "output file = $output"
n=`grep -c \<event\> $lhe`
echo "n = $n"
sed s%examples/Pythia8/events.lhe%$lhe% examples/Pythia8/configLHE.cmnd > ${lhe%%.lhe}.cmnd #this will create a new config pointing to your lhe
sed "s%Main:numberOfEvents = 10%Main:numberOfEvents = $n%" --in-place ${lhe%%.lhe}.cmnd
echo "current directory = $PWD"
echo "command = " ./DelphesPythia8 $delphes_card ${lhe%%.lhe}.cmnd $output
./DelphesPythia8 $delphes_card ${lhe%%.lhe}.cmnd $output  #this runs delphes using your new config