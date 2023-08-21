def make_pie_chart(data : dict, caption : str = "image_caption", label : str = "image_label", preamble : bool = False, ctype : str = 'classic') -> str:
    '''
        Produces LaTeX code to display a pie chart.  

        Parameters:  
        -----------  
        - data : dict
            dictionary containing data, e.g.

            ```python 
                # Morning sales
                data = {'coffee':38, 'tea':36, 'croissant':11, 'patries':10, 'juice':5s}
            ```
        - caption : str  
            string for the caption of LaTeX table (default: "table_caption")  
        - label : str  
            string for the label of LaTeX table (default: "table_label")  
        - preamble : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)  
        - ctype : str  
            Type of pie chart, can be classic, polar, square or cloud

        Returns:  
        --------  
        - p : str  
            LaTeX code to display a pie chart  
        
        Usage:
        ------

        ```python
        data = {'coffee':38, 'tea':36, 'croissant':11, 'pastries':10, 'juice':5}
        latex_pie_chart = make_pie_chart(data, caption='My pie chart 1', label='pie1', preamble=True, ctype="classic")
        ```

        Output:
        -------

        ```latex
        \\documentclass[11pt]{article}
        \\usepackage{pgf-pie}
        \\usepackage{graphicx}
        \\begin{document}

        \\begin{figure}[!ht]
                \\centering
                    \\begin{tikzpicture}
                    \\pie{38/coffee, 36/tea, 11/croissant, 10/pastries, 5/juice}
                    \\end{tikzpicture}
                \\caption{My pie chart 1}\\label{fig:pie1}
        \\end{figure}

        \\end{document}
        ```
    '''

    if ctype not in ['classic', 'polar', 'square', 'cloud']:
        raise Exception("Error Message: pie chart, can be classic, polar, square or cloud.")
    
    p = ""
    # LaTeX preamble
    if preamble:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\usepackage{pgf-pie}\n"
        p += "\\usepackage{graphicx}\n"
        p += "\\begin{document}\n\n"
        

    # Pie Chart
    p += "\\begin{figure}[!ht]\n"
    p += "\t\\centering\n"
    p += "\t\t\\begin{tikzpicture}\n"

    if ctype == 'classic': p += "\t\t\\pie{"
    else: p += "\t\t\\pie["+ctype+"]{"

    for key, value in data.items():
        p += str(value) + "/" + str(key) + ","
    p = p[:-1]
    p += "}\n"

    p += "\t\t\\end{tikzpicture}\n"
    p += "\t\\caption{"+str(caption)+"}\\label{fig:"+label+"}\n"
    p += "\\end{figure}\n"

    if preamble:
        # End document
        p += "\n\\end{document}\n"

    return p
    return p