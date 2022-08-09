from pathlib import Path 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('lhe', nargs='+')
parser.add_argument('--delphes_dir', default='../delphes')
parser.add_argument('--delphes_card', default='../delphes_card_MuonColliderDet.tcl')
parser.add_argument('--executable', default='../delphesPythia.sh')
args = parser.parse_args()
delphes_dir = str(Path(args.delphes_dir).resolve())
delphes_card = str(Path(args.delphes_card).resolve())
executable = str(Path(args.executable).resolve())
for p in args.lhe:
    p = str(Path(p).resolve())
    with Path('template.sub').open('r') as f:
        template_text = f.read()
        template_text = template_text.format(executable=executable, lhe=p, delphes_dir=delphes_dir, delphes_card=delphes_card)
    with Path(f'{Path(p).stem}.sub').open('w') as f:
        f.write(template_text)
    