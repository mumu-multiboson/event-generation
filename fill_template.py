
from pathlib import Path
import numpy as np

def main():
    couplings = np.array([-0.02, -0.01, -0.001, -0.0001, 0.0001, 0.0005, 0.001, 0.01])
    base = 1e-12
    couplings = couplings * base

    for ft1 in couplings:
        out_path = Path(f'mumu_nunuww/INT_QUAD_T1_{ft1:.0E}.txt')
        template_path = Path('mumu_nunuww/INT_QUAD_T1_template.txt')
        with template_path.open('r') as f:
            template = f.read()
        out = f'mumu_nunuww_INT_QUAD_T1_{ft1:.0E}_6TeV'
        template = template.replace('{out}', out)
        template = template.replace('{ft1}', f'{ft1:.0E}')
        with out_path.open('w') as f:
            f.write(template)



if __name__ == '__main__':
    main()