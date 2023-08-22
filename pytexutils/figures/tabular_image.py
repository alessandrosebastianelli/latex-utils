from ..tables.table import table
import numpy as np

def tabular_image(images_full_path : np.ndarray, caption : str = "table_caption", label : str = "table_label", preamble : bool = False) -> str:
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
        - preamble : bool  
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
    
        latex_table = tabular_image(images, caption='My image 1', label='img1', preamble=True)  
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

    p = table(None, images_full_path, caption=caption, label=label, preamble=preamble)

    return p