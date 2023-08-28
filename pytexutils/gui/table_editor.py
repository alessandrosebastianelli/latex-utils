
from tkinter import simpledialog
import tkinter as tk
import numpy as np

import sys
sys.path += ['.', './tables/']
from pytexutils.tables.table import table


def table_editor():
    '''
        Opens a GUI with table editor that produces LaTeX code to display a table.

        Parameters:  
        -----------
        - Nothing

        Returns:  
        --------  
        - latex_table : str  
            LaTeX code to display a table  

        Usage:
        ------

        ```python
            latex_table = table_editor()
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


    def get_value():
        data = []
        for i in range(rows):
            ddd = []
            for j in range(cols):
                try:
                    d = float(entries[i,j].get())
                except Exception:
                    d = str(entries[i,j].get())
                ddd.append(d)
            data.append(ddd)
        
        data = np.array(data)
        columns = data[0,:]

        global latex_table
        latex_table = table(columns_name=columns, data=data[1:,:])
    
    
    rows = simpledialog.askinteger(title='Number of Rows',    prompt='Number of Rows:',)#   parent=window)
    cols = simpledialog.askinteger(title='Number of Columns', prompt='Number of Columns:' )#, parent=window)

    window = tk.Tk()
    window.title('Table Editor')
    window.attributes("-zoomed", True)

    entries = []
    for i in range(rows):
        eee = []
        for j in range(cols):
            e = tk.Entry(window, width=10)
            eee.append(e)
            e.grid(row=i, column=j)
            e.insert(tk.END, "")
        entries.append(eee)
    entries = np.array(entries)

    b = tk.Button(window, text='Save', command=get_value)
    b.grid(row=i+1, column=0)

    b2 = tk.Button(window, text='Exit', command=window.destroy)
    b2.grid(row=i+1, column=1)

    window.mainloop()

    return latex_table