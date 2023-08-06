import sys
sys.path += ['.']

from latexutils.make_table import make_table
import numpy as np
import os

if __name__ == '__main__':

    columns_name = ['A', 'B', 'C']
    data         = np.array(
        [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
            [0.7, 0.8, 0.9],
            [1.1, 1.2, 1.3]
        ]
    )

    latex_table = make_table(columns_name, data, caption='My table 1', label='tab1', preable=True)
    print(latex_table)

    save_folder = os.path.join('tmp', 'test_make_table')
    os.makedirs(save_folder, exist_ok=True)
    with open(os.path.join(save_folder, 'main.tex'), 'w') as texfile:
        texfile.writelines(latex_table)