from pathlib import Path

delphes_dir = Path("/afs/cern.ch/work/a/aschuy/private/VBS_WGamma/muon_collider/event-generation/delphes")
delphes_card = Path("/afs/cern.ch/work/a/aschuy/private/VBS_WGamma/muon_collider/event-generation/delphes_card_MuonColliderDet.tcl")


condor_output_path = Path("/afs/cern.ch/user/a/aschuy/work/private/VBS_WGamma/afs/ntuples/condor/delphes_pythia/output")

for p in sorted(condor_output_path.glob("*.out")):
    cmnd = f'{p.stem}.cmnd'
    with p.open('r') as f:
        lines = f.readlines()
        for l in lines:
            if not l.startswith('output file'):
                continue
            output_file = Path(l.split('=')[1].strip())
        print(f'./DelphesPythia8 {delphes_card} {cmnd} {output_file}')