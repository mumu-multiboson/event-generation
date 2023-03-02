from pathlib import Path 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mg_scripts', nargs='+')
parser.add_argument('--mg5', default='../MG5_aMC_v3_1_1/bin/mg5_aMC')
parser.add_argument('--output', required=True)
parser.add_argument('--executable', default='../madgraph.sh')
parser.add_argument('--condor_dir', default='/afs/cern.ch/user/a/aschuy/work/public/muon_collider/mumu_multiboson/ntuples/condor/generation')
args = parser.parse_args()
mg5 = str(Path(args.mg5).resolve())
output_dir = Path(args.output).resolve()
executable = str(Path(args.executable).resolve())
condor_dir = Path(args.condor_dir).resolve()
for p in args.mg_scripts:
    p = Path(p).resolve()
    higgs_mass = p.parent.stem
    cm_energy = p.parent.parent.stem
    name = f'heavy_higgs_{higgs_mass}_{cm_energy}'
    output = output_dir / cm_energy
    with Path('madgraph.tmp').open('r') as f:
        template_text = f.read()
        template_text = template_text.format(executable=executable, mg_script=str(p), mg5=mg5, output=str(output), condor_dir=str(condor_dir))
    with (condor_dir / 'submit' / Path(f'{name}.sub')).open('w') as f:
        f.write(template_text)
    