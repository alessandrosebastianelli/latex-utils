def make_table(columns_name, data, caption : str = "table_caption", label : str = "table_label", preable : bool = False) -> str:
    '''
        Produces LaTeX code to display a table.

        Parameters:  
        -----------
        - columns_name  
            list of strings containing table columns name
        - data  
            2D ndarray containing data used to fill the table
        - caption : str  
            string for the caption of LaTeX table (default: "table_caption")  
        - label : str  
            string for the label of LaTeX table (default: "table_label")  
        - preable : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)  

        Returns:  
        --------  
        - p : str  
            LaTeX code to display a table  
    '''

    if data.shape != 2:
        raise Exception("Error Message: shape of data must be equals to two.")

    if columns_name is not None: 
        if data.shape[1] != len(columns_name):
            raise Exception("Error Message: mismatch between number of columns and shape of data")
    
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
    p += "\t\\begin{tabular}{" + "".join([char*data.shape[1] for char in "c"]) + '}\n'
    p += "\t\t\\toprule\n"

    if columns_name is not None:
        # Columns name
        l = "\t\t"
        for i in range(len(columns_name)):
            l+= "{:<5s}{}{:<5s}{}".format("", str(columns_name[i]), "", "&")
        l = l[:-1]
        p += l + "\\\\\n"
        p += "\t\t\\midrule\n"

    # Data
    for i in range(data.shape[0]):
        l = "\t\t"
        for j in range(data.shape[1]):
            l+= "{:<5s}{}{:<5s}{}".format("", str(data[i,j]), "", "&")
        l = l[:-1]

        p += l + "\\\\\n"
    p += "\t\t\\bottomrule\n"
    p += "\t\\end{tabular}\n"
    p += "\\end{table}\n"

    if preable:
        # End document
        p += "\n\\end{document}\n"

    return p