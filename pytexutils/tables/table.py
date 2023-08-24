import numpy as np

def table(columns_name : list, data : np.ndarray, round_val : int = 4, bold_axis : int = None, caption : str = "table_caption", label : str = "table_label", preamble : bool = False) -> str:
    '''
        Produces LaTeX code to display a table.

        Parameters:  
        -----------
        - columns_name  
            list of strings containing table columns name
        - data : np.ndarray
            2D ndarray containing data used to fill the table
        - round_val : int
            integer representing the decimal rounding
        - bold_axis : int
            integer representing the axis to wich get the max value and to set bold, if None no bold text will be added
            if 0 the maximum will be calculated column-wise, if 1 the maximum will be calculated row-wise
        - caption : str  
            string for the caption of LaTeX table (default: "table_caption")  
        - label : str  
            string for the label of LaTeX table (default: "table_label")  
        - preamble : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)  

        Returns:  
        --------  
        - p : str  
            LaTeX code to display a table  

        Usage:
        ------

        ```python
        import numpy as np  

        columns_name = ['A', 'B', 'C']  
        data         = np.array(  
            [  
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]  
            ]  
        )  

        latex_table = table(columns_name, data, caption='My table 1', label='tab1', preamble=True)
        ```

        Output:
        -------

        ```latex
        \\documentclass[11pt]{article}
        \\usepackage{booktabs}
        \\usepackage{graphicx}

        \\begin{document}

        \\begin{table}[!ht]
                \\centering
                \\caption{My table 1}\\label{tab:tab1}
                \\resizebox{\\columnwidth}{!}{
                \\begin{tabular}{ccc}
                        \\toprule
                            A     &     B     &     C     \\\\
                        \\midrule
                            0.1     &     0.2     &     0.3     \\\\
                            0.4     &     0.5     &     0.6     \\\\
                            0.7     &     0.8     &     0.9     \\\\
                            1.1     &     1.2     &     1.3     \\\\
                        \\bottomrule
                \\end{tabular}}
        \\end{table}

        \\end{document}
        ```
    '''

    if len(data.shape) != 2:
        raise Exception("Error Message: shape of data must be equals to two.")

    if columns_name is not None: 
        if data.shape[1] != len(columns_name):
            raise Exception("Error Message: mismatch between number of columns and shape of data")
        
    if round_val < 1:
        round_val = 1

    if bold_axis is not None:
        if bold_axis < 0 or bold_axis > 1:
            bold_axis = None
    
    p = ""
    # LaTeX preamble
    if preamble:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\usepackage{booktabs}\n"
        p += "\\usepackage{graphicx}\n\n"
        p += "\\begin{document}\n\n"

    # Table
    p += "\\begin{table}[!ht]\n"
    p += "\t\\centering\n"
    p += "\t\\caption{"+str(caption)+"}\\label{tab:"+label+"}\n"
    p += "\t\\resizebox{\\columnwidth}{!}{\n"
    p += "\t\\begin{tabular}{" + "".join([char*data.shape[1] for char in "c"]) + '}\n'
    p += "\t\t\\toprule\n"

    if columns_name is not None:
        # Columns name
        l = "\t\t"
        for i in range(len(columns_name)):
            l+= "{:<5s}{}{:<5s}{}".format("", str(columns_name[i].strip()), "", "&")
        l = l[:-1]
        p += l + "\\\\\n"
        p += "\t\t\\midrule\n"

    if bold_axis is not None:
        min_pos = np.argmin(data.astype(str), axis=bold_axis)
        max_pos = np.argmax(data.astype(str), axis=bold_axis)

    # Data
    for i in range(data.shape[0]):
        l = "\t\t"
        for j in range(data.shape[1]):

            d = data[i,j]
            if type(d) is float: d = round(d, round_val)
            d = str(d).strip()
            
            if bold_axis is None:
                l+= "{:<1s}{}{:<1s}{}".format("", d, "", "&")
            elif bold_axis == 0:
                if min_pos[j] == i:
                    l+= "{:<1s}{}{:<1s}{}".format("", "\\bf{"+d+"}", "", "&")
                elif max_pos[j] == i:
                    l+= "{:<1s}{}{:<1s}{}".format("", "\\texit{"+d+"}", "", "&")
                else:
                    l+= "{:<1s}{}{:<1s}{}".format("", d, "", "&")
            elif bold_axis == 1:
                if min_pos[i] == j:
                    l+= "{:<1s}{}{:<1s}{}".format("", "\\bf{"+d+"}", "", "&")
                elif max_pos[i] == j:
                    l+= "{:<1s}{}{:<1s}{}".format("", "\\textit{"+d+"}", "", "&")
                else:
                    l+= "{:<1s}{}{:<1s}{}".format("", d, "", "&")

        l = l[:-1]

        p += l + "\\\\\n"
    p += "\t\t\\bottomrule\n"
    p += "\t\\end{tabular}}\n"
    p += "\\end{table}\n"

    if preamble:
        # End document
        p += "\n\\end{document}\n"

    return p