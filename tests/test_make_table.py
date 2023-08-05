import sys
sys.path += ['.']

from latexutils.make_table import make_table
import numpy as np

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

    latex_table = make_table(columns_name, data, caption='My table', label='tab1', preable=False)
    print(latex_table)

    latex_table_2 = make_table(columns_name, data, caption='My table', label='tab1', preable=True)
    print(latex_table_2)