import sys
sys.path += ['.']

import os

from pytexutils.graphs.pie_chart import pie_chart

if __name__ == '__main__':


    data = {'coffee':38, 'tea':36, 'croissant':11, 'pastries':10, 'juice':5}
    latex_pie_chart = pie_chart(data, caption='My pie chart 1', label='pie1', preamble=True, ctype="classic")

    print(latex_pie_chart)

    save_folder = os.path.join('tmp', 'test_make_chart')
    os.makedirs(save_folder, exist_ok=True)
    
    with open(os.path.join(save_folder, 'main-1.tex'), 'w') as texfile:
        texfile.writelines(latex_pie_chart)


    latex_pie_chart = pie_chart(data, caption='My pie chart 2', label='pie2', preamble=True, ctype="square")

    print(latex_pie_chart)

    save_folder = os.path.join('tmp', 'test_make_chart')
    os.makedirs(save_folder, exist_ok=True)
    
    with open(os.path.join(save_folder, 'main-2.tex'), 'w') as texfile:
        texfile.writelines(latex_pie_chart)