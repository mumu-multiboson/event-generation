from pathlib import Path 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mg_scripts', nargs='+')
parser.add_argument('--mg5', default='../MG5_aMC_v3_1_1/bin/mg5_aMC')
parser.add_argument('--output', default='/data/schuya/muon_collider/ntuples/madgraph/heavy_higgs')
parser.add_argument('--executable', default='../madgraph.sh')
parser.add_argument('--condor_dir', default='/data/schuya/muon_collider/ntuples/condor/generation')
args = parser.parse_args()
mg5 = str(Path(args.mg5).resolve())
output_dir = Path(args.output).resolve()
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


for p in args.mg_scripts:
    p = Path(p).resolve()
    higgs_mass = p.parent.stem
    cm_energy = p.parent.parent.stem
    name = f'heavy_higgs_{higgs_mass}_{cm_energy}'
    output = output_dir / cm_energy
    make_if_needed(output)
    with Path('madgraph.tmp').open('r') as f:
        template_text = f.read()
        template_text = template_text.format(executable=executable, mg_script=str(p), mg5=mg5, output=str(output), condor_dir=str(condor_dir))
    submit_dir = condor_dir / 'submit'
    submit_dir.mkdir(parents=True, exist_ok=True)
    with (submit_dir / Path(f'{name}.sub')).open('w') as f:
        f.write(template_text)
    print(f'Created {name}.sub in {submit_dir} for {higgs_mass} GeV Higgs at {cm_energy} with output in {output}')
print(f'Run "python submit_jobs.py {submit_dir}/*" to submit jobs')
    