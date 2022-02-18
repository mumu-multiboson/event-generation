#!/bin/bash -x

if [[ `basename $PWD` != "event-generation" ]]; then echo "Execute from event-generation dir"; exit; fi
if [[ $# < 1 ]]; 
then 
    echo "Usage: ./generateEvents.sh <mg script> [delphes card]"
    echo "Example: ./generateEvents.sh foo delphes_card_MuonColliderDet.tcl"
    exit
else
    mgScript=$PWD/$1
    if [[ $# -gt 1 ]]; then
	delphesCard=$PWD/$2
    else
	delphesCard=$PWD/"delphes_card_MuonColliderDet.tcl"
    fi
fi

source setup.sh

touch dummy

#########################################################################

cd MG5_aMC_v3_1_1
./bin/mg5_aMC < "${mgScript}"
gzs=`find . -newer ../dummy -name "unweighted_events.lhe.gz" -exec echo $PWD/{} \;`
echo $gzs

cd ..

#------------------------------------------------------------------------

cd delphes
for gz in $gzs; do 
    lhe=${gz%%.gz}
    output=${lhe%%.lhe}.root  #set delphes output path/name

    gunzip $gz
    n=`grep -c \<event\> $lhe`
    echo $n
    sed s%examples/Pythia8/events.lhe%$lhe% examples/Pythia8/configLHE.cmnd > configLHE.cmnd #this will create a new config pointing to your lhe
    sed "s%Main:numberOfEvents = 10%Main:numberOfEvents = $n%" --in-place configLHE.cmnd
    ./DelphesPythia8 $delphesCard configLHE.cmnd $output  #this runs delphes using your new config
done
