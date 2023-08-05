import numpy as np

def make_table(columns_name, data, caption="table_caption", label="table_label", preable=False):
    '''
        Create a string with plain LaTeX file with a table using columns name and 2D array data.

        Keyword arguments:
        columns_name -- list of strings containing table columns name
        data -- 2D ndarray containing data used to fill the table
        caption -- string for the caption of LaTeX table (default: "table_caption")
        label -- string for the label of LaTeX table (default: "table_label")
        preable -- bolean value, if True the function will return a full LaTeX document, if False the function will return only the table (default: False)
    '''

    assert data.shape[1] == len(columns_name), "Error Message: mismatch between number of columns and shape of data"

    p = ""
    # LaTeX preamble
    if preable:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\usepackage{booktabs}\n\n"
        p += "\\begin{document}\n\n"

    # Table
    p += "\\begin{table}[!ht]\n"
    p += "\t\\centering\n"
    p += "\t\\caption{"+str(caption)+"}\\label{tab:"+label+"}\n"
    p += "\t\\begin{tabular}{" + "".join([char*len(columns_name) for char in "c"]) + '}\n'
    p += "\t\t\\toprule\n"

    # Columns name
    l = "\t\t"
    for i in range(len(columns_name)):
        l+= "{:<5s}{:<5s}{:<5s}{}".format("", str(columns_name[i]), "", "&")
    l = l[:-1]
    p += l + "\\\\\n"
    p += "\t\t\\midrule\n"

    # Data
    for i in range(data.shape[0]):
        l = "\t\t"
        for j in range(data.shape[1]):
            l+= "{:<5s}{:<5s}{:<5s}{}".format("", str(data[i,j]), "", "&")
        l = l[:-1]

        p += l + "\\\\\n"
    p += "\t\t\\bottomrule\n"
    p += "\t\\end{tabular}\n"
    p += "\\end{table}\n"

    if preable:
        # End document
        p += "\n\\end{document}\n"

    return p