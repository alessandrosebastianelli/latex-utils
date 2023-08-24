import sys
sys.path += ['.']

from pytexutils.graphs.bar_chart import bar_chart
from pytexutils.utils.writer import write_to_file

import numpy as np

if __name__ == '__main__':

    size = 3
    data = {
        'a' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [0.54, 0, 0],
        },
        'b' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [0, 0.50, 0.50],
        },
        'c' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [0, 0, 0.50],
        },
        'd' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [1, 0.50, 0.50],
        },
        'e' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [0, 1, 0.50],
        },
        'f' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [1, 1.00, 0.50],
        },
        'g' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [0, 0.0, 1.0],
        },
        'h' : {
            'x'     : np.arange(0, size),
            'y'     : np.random.randint(0, 100, size),
            'color' : [1, 0.50, 1.00],
        }
        }
    latex_bar_chart = bar_chart(data, caption='My bar chart 1', label='bar1', preamble=True)
    print(latex_bar_chart)

    write_to_file(latex_bar_chart, 'tmp/test_bar_chart')
    #write_to_file(latex_bar_chart, None)