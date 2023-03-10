if [[ `basename $PWD` != "event-generation" ]]; then echo "Execute from event-generation dir"; exit; fi

baseDir=$PWD
source setup.sh

#MadGraph
wget https://launchpad.net/mg5amcnlo/3.0/3.1.x/+download/MG5_aMC_v3.1.1.tar.gz
tar -xzvf MG5_aMC_v3.1.1.tar.gz
if [[ $? -ne 0 ]]; then
    echo "ERROR getting madgraph"
    exit
fi
rm MG5_aMC_v3.1.1.tar.gz

git clone https://github.com/delphes/delphes.git
cd delphes
git checkout tags/3.5.0
make HAS_PYTHIA8=true -j -I/cvmfs/sft.cern.ch/lcg/views/LCG_101_ATLAS_7/x86_64-centos7-gcc11-opt/include/Pythia8
if [[ $? -ne 0 ]]; then
    echo "ERROR compiling delphes"
    exit
fi
cd ..



# #Whizard
# wget http://whizard.hepforge.org/whizard-3.0.3.tar.gz
# tar -xzf whizard-3.0.3.tar.gz
# rm whizard-3.0.3.tar.gz
# cd whizard-3.0.3
# ./configure --prefix=$baseDir
# /afs/cern.ch/user/a/aschuy/work/private/VBS_WGamma/muon_collider/event-generation
# make -j
# make install
# if [[ $? -ne 0 ]]; then
#     echo "ERROR compiling Whizard"
#     exit
# fi
# cd ..