import sys
sys.path += ['.']

from pytexutils.tables.table import table
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

    print(type(data[0,0]))
    print(type(data[0,1]))

    latex_table = table(columns_name, data, bold_axis=1, caption='My table 1', label='tab1', preamble=True)
    print(latex_table)

    save_folder = os.path.join('tmp', 'test_table')
    os.makedirs(save_folder, exist_ok=True)
    with open(os.path.join(save_folder, 'main.tex'), 'w') as texfile:
        texfile.writelines(latex_table)