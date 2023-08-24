import sys
sys.path += ['.']

from pytexutils.graphs.bar_chart import bar_chart
from pytexutils.utils.writer import write_to_file

if __name__ == '__main__':


    data = {
        'men' : {
            'x'     : [2012,   2011,   2010,   2009],
            'y'     : [408184, 408348, 414870, 412156],
            'color' : [0.54, 0, 0],
        },
        'women' : {
            'x'     : [2012,   2011,   2010,   2009],
            'y'     : [388950, 393007, 398449, 395972],
            'color' : [0, 0.50, 0.50],
        }
        }
    latex_bar_chart = bar_chart(data, caption='My bar chart 1', label='bar1', preamble=True)
    print(latex_bar_chart)

    write_to_file(latex_bar_chart, 'tmp/test_bar_chart')
    write_to_file(latex_bar_chart, None)