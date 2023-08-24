from tkinter import filedialog
import os

def write_to_file(content : str, path : str = None) -> None:
    '''
       Saves latex produced using pytexutils code to a file.

        Parameters:  
        -----------  
        - conntent : str:
            latex code procude using pytexutils to be saved
        - path : sting
            path where to save the file, whitout extension (default : None), if None a filedialog will pop up to ask for the save path.
                
        Returns:  
        --------  
        Nothing the file will be saved
        
        Usage:
        ------

        ```python
            latex_code =  "\\documentclass[11pt]{article}\n\\usepackage{graphicx}\n\\begin{document}\n\\begin{figure}[!ht]\n\\centering\n
            \\includegraphics[width=\\columnwidth]{fig1.png}\n\\caption{My image 1}\\label{fig:img1}\n\\end{figure}\n\\end{document}"

            write_to_file('path/')
        ```

        Output:
        -------
        Nothing, the file will be saved.
    '''
     
    if path is not None:
        os.makedirs(path, exist_ok=True)
    else:
        path = filedialog.askdirectory()
        if path is None: raise Exception("Error Message: path not defined")
    
    with open(os.path.join(path,'pytexutils.tex'), 'w') as texfile:
        texfile.writelines(content)