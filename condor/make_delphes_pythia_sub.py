from pathlib import Path 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('lhe', nargs='+')
parser.add_argument('--delphes_dir', default='/afs/cern.ch/user/a/aschuy/work/private/VBS_WGamma/muon_collider/event-generation/delphes')
parser.add_argument('--delphes_card', default='/afs/cern.ch/user/a/aschuy/work/private/VBS_WGamma/muon_collider/event-generation/delphes_card_MuonColliderDet.tcl')
parser.add_argument('--executable', default='/afs/cern.ch/user/a/aschuy/work/private/VBS_WGamma/muon_collider/event-generation/delphesPythia.sh')
parser.add_argument('--condor_dir', default='/afs/cern.ch/user/a/aschuy/work/public/muon_collider/mumu_multiboson/ntuples/condor/delphes_pythia')
args = parser.parse_args()
delphes_dir = str(Path(args.delphes_dir).resolve())
delphes_card = str(Path(args.delphes_card).resolve())
executable = str(Path(args.executable).resolve())
condor_dir = Path(args.condor_dir).resolve()
def make_if_needed(d):
    if not d.exists():
        d.mkdir(parents=True)
make_if_needed(condor_dir)
make_if_needed(condor_dir / 'output')
make_if_needed(condor_dir / 'condor')
make_if_needed(condor_dir / 'error')
make_if_needed(condor_dir / 'submit')

for p in args.lhe:
    p = str(Path(p).resolve())
    with Path('delphes_pythia.tmp').open('r') as f:
        template_text = f.read()
        template_text = template_text.format(executable=executable, lhe=p, delphes_dir=delphes_dir, delphes_card=delphes_card, condor_dir=str(condor_dir))
    with (condor_dir / 'submit' / Path(f'{Path(p).stem}.sub')).open('w') as f:
        f.write(template_text)
    