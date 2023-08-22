def image(image_full_path : str, caption : str = "image_caption", label : str = "image_label", preamble : bool = False) -> str:
    '''
        Produces LaTeX code to display an image.  

        Parameters:  
        -----------  
        - image_full_path : str  
            path of the image in the LaTeX project  
        - caption : str  
            string for the caption of LaTeX table (default: "table_caption")  
        - label : str  
            string for the label of LaTeX table (default: "table_label")  
        - preamble : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)  

        Returns:  
        --------  
        - p : str  
            LaTeX code to display an image  
        
        Usage:
        ------

        ```python
    
        latex_table = image('fig1.png', caption='My image 1', label='img1', preamble=True)
        ```

        Output:
        -------

        ```latex
        \\documentclass[11pt]{article}
        \\usepackage{graphicx}
        \\begin{document}

        \\begin{figure}[!ht]
                \\centering
                \\includegraphics[width=\\columnwidth]{fig1.png}
                \\caption{My image 1}\\label{fig:img1}
        \\end{figure}

        \\end{document}
        ```
    '''

    p = ""
    # LaTeX preamble
    if preamble:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\usepackage{graphicx}\n"
        p += "\\begin{document}\n\n"
        

    # Table
    p += "\\begin{figure}[!ht]\n"
    p += "\t\\centering\n"
    
    p += "\t\\includegraphics[width=\\columnwidth]{"+str(image_full_path)+"}\n"

    p += "\t\\caption{"+str(caption)+"}\\label{fig:"+label+"}\n"
    p += "\\end{figure}\n"

    if preamble:
        # End document
        p += "\n\\end{document}\n"

    return p