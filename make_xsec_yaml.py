
import argparse
from pathlib import Path
import yaml



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--madgraph_dir', default='/data/schuya/muon_collider/ntuples/madgraph/heavy_higgs')

    args = parser.parse_args()
    madgraph_dir = Path(args.madgraph_dir).resolve()

    xsec_dict = {}    
    # loop over directories in madgraph_dir
    failed_dirs = []
    for cm_energy in madgraph_dir.iterdir():
        if not cm_energy.is_dir():
            continue
        for mass in cm_energy.iterdir():
            if not mass.is_dir():
                continue
            if 'charged' in mass.name:
                continue
            # get the cross section
            try:
                text = (mass / 'Events/run_01/run_01_tag_1_banner.txt').read_text()
                xsec = float(text.split('Integrated weight (pb)')[1].split(':')[1].split('\n')[0])
                xsec_dict[f'{mass.name}_{cm_energy.name}'] = xsec * 1000
            except Exception as e:
                print(f'Failed to get cross section for {mass.name}_{cm_energy.name}')
                failed_dirs.append(f'{mass.name}_{cm_energy.name}')
                print(e)

    print('Failed dirs:', failed_dirs)
    output_path = madgraph_dir / 'cross_section.yaml'
    print(f'Writing cross_section.yaml to {output_path}')
    # sort xsec_dict by cm_energy, then by mass
    xsec_dict = dict(sorted(xsec_dict.items(), key=lambda x: (int(x[0].split('_')[-1][:-3]), int(x[0].split('_')[-2][:-3]))))
    print('xsec_dict:', xsec_dict)
    output_path.write_text(yaml.dump(xsec_dict, sort_keys=False))


if __name__ == "__main__":
    main()