from .make_table import make_table
import numpy as np

def make_image(image_full_path : str, caption : str = "image_caption", label : str = "image_label", preable : bool = False) -> str:
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
        - preable : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)  

        Returns:  
        --------  
        - p : str  
            LaTeX code to display an image  
        
        Usage:
        ------

        ```python
    
        latex_table = make_table('fig1.png', caption='My image 1', label='img1', preable=True)
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
    if preable:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\usepackage{graphicx}\n"
        p += "\\begin{document}\n\n"
        

    # Table
    p += "\\begin{figure}[!ht]\n"
    p += "\t\\centering\n"
    
    p += "\t\\includegraphics[width=\\columnwidth]{"+str(image_full_path)+"}\n"

    p += "\t\\caption{"+str(caption)+"}\\label{fig:"+label+"}\n"
    p += "\\end{figure}\n"

    if preable:
        # End document
        p += "\n\\end{document}\n"

    return p


def make_tabular_image(images_full_path : np.ndarray, caption : str = "table_caption", label : str = "table_label", preable : bool = False) -> str:
    '''
        Produces LaTeX code to display a table of images.

        Parameters:  
        ----------- 
        - images_full_path
            2D ndarry of strings, path of the image in the LaTeX project
        - caption : str  
            string for the caption of LaTeX table (default: "table_caption")  
        - label : str  
            string for the label of LaTeX table (default: "table_label")  
        - preable : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)

        Returns:  
        --------  
        - p : str  
            LaTeX code to display a table of images.
        
        Usage:
        ------

        ```python

        import numpy as np

        images = np.array(  
            [["fig1.png", "fig2.png"],["fig1.png", "fig2.png"]]  
        )  
    
        latex_table = make_tabular_image(images, caption='My image 1', label='img1', preable=True)  
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
                \\caption{My image 1}\\label{tab:img1}
                \\resizebox{\\columnwidth}{!}{
                \begin{tabular}{cc}
                        \\toprule
                            \\includegraphics[width=\\columnwidth]{fig1.png}     &     \\includegraphics[width=\\columnwidth]{fig2.png}     \\\\
                            \\includegraphics[width=\\columnwidth]{fig1.png}     &     \\includegraphics[width=\\columnwidth]{fig2.png}     \\\\
                        \\bottomrule
                \\end{tabular}}
        \\end{table}
        ```
    '''

    if len(images_full_path.shape) != 2:
        raise Exception("Error Message: images_full_path must be a 2D array")

    images_full_path = images_full_path.astype(object)

    for i in range(images_full_path.shape[0]):
        for j in range(images_full_path.shape[1]):
            images_full_path[i,j] = "\\includegraphics[width=\\columnwidth]{"+str(images_full_path[i,j])+"}"

    p = make_table(None, images_full_path, caption=caption, label=label, preable=preable)

    return p