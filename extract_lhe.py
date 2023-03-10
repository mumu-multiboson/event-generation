import argparse
from pathlib import Path
import subprocess

def main():
    parser = argparse.ArgumentParser(description='extract .lhe or .lhe.gz files from madgraph run directories and give them a corresponding name.')
    parser.add_argument('location')
    parser.add_argument('--prefix', '-p', default='')
    parser.add_argument('--append_energy', action='store_true')
    args = parser.parse_args()

    location = Path(args.location)
    if args.append_energy:
        energy = location.stem
    for d in location.glob('*'):
        if not d.is_dir():
            continue
        if not str(d.stem).startswith(args.prefix):
            continue
        event_dir = d / 'Events'
        if not event_dir.exists():
            print(f"Error: {str(d)} does not contain 'Events' directory. Skipping...")
            continue
        if (event_dir / 'run_02').exists():
            print(f"Error: {str(event_dir)} contains multiple runs, which is unsupported. Skipping...")
            continue
        run_dir = event_dir / 'run_01'
        if not run_dir.exists():
            print(f"Error: {str(event_dir)} does not contain a 'run_01' directory. Skipping...")
            continue
        gz_files = [f for f in run_dir.glob('*.lhe.gz')]
        for f in gz_files:
            print(f'unzipping {f}')
            subprocess.run(['gunzip', str(f)])

        lhe_files = [f for f in run_dir.glob('*.lhe')]
        if len(lhe_files) > 1:
            print(f"Error: {str(run_dir)} contains multiple LHE files. Skipping...")
            continue
        try:
            lhe_file = lhe_files[0]
        except IndexError:
            print(f"Error: {str(run_dir)} does not contain an LHE file. Skipping...")
            continue
        if args.append_energy:
            output_name = location / f'{d.stem}_{energy}.lhe'
        else:
            output_name = location / f'{d.stem}.lhe'
        if output_name.exists():
            print(f"Error: {str(output_name)} already exists! Skipping...")
            continue
        print(f'moving {lhe_file} to {output_name}')
        lhe_file.rename(output_name)

if __name__ == '__main__':
    main()


