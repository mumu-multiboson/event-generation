if [[ `basename $PWD` != "event-generation" ]]; then echo "Execute from event-generation dir"; exit; fi

source /cvmfs/sft.cern.ch/lcg/views/LCG_101_ATLAS_7/x86_64-centos7-gcc11-opt/setup.sh

export LD_LIBRARY_PATH=${PWD}/delphes:$LD_LIBRARY_PATH
export ROOT_INCLUDE_PATH=${PWD}/delphes/external/:$ROOT_INCLUDE_PATH
export prodBase=$PWD

if [[ $HOSTNAME == "login.snowmass21.io" ]]; then
    #important
    module load python/2.7.15
    module load py-numpy/1.15.2-py2.7
    module load py-six/1.11.0-py2.7
    . /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.22.08/x86_64-centos7-gcc48-opt/bin/thisroot.sh
    
    #convenient
    module load emacs
else
    which root >> /dev/null
    if [[ $? -ne 0 ]]; then
	echo "Please ensure ROOT is available and retry"
    fi
fi
