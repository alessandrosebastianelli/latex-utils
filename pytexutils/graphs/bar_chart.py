def bar_chart(data : dict, x_label : str = "xlabel", y_label : str = "ylabel", caption : str = "image_caption", label : str = "image_label", preamble : bool = False) -> str:
    '''
        Produces LaTeX code to display a bar plot.  

        Parameters:  
        -----------  
        - data : dict
            dictionary containing data. Must contains  
                - 1) x axis value
                - 2) y axis value 
                - 3) label
                - 4) color in rgb format e.g.

            ```python 
                data = {
                    'men' : {
                        'x'     : [2012,   2011,   2010,   2009]
                        'y'     : [408184, 408348, 414870, 412156]
                        'color' : [0.54, 0, 0]
                    },
                    'women' : {
                        'x'     : [2012,   2011,   2010,   2009]
                        'y'     : [388950, 393007, 398449, 395972]
                        'color' : [0, 0.50, 0.50]
                    }
                }
            ```

        - caption : str  
            string for the caption of LaTeX graph (default: "image_caption")  
        - label : str  
            string for the label of LaTeX graph (default: "image_label")  
        - preamble : bool  
            If True the function will return a full LaTeX document, if False the function will return only the table (default: False)  

        Returns:  
        --------  
        - p : str  
            LaTeX code to display a pie chart  
        
        Usage:
        ------

        ```python
        data = {
        'men' : {
                'x'     : [2012,   2011,   2010,   2009],
                'y'     : [408184, 408348, 414870, 412156],
                'color' : [0.54, 0, 0],
            },
        'women' : {
                'x'     : [2012,   2011,   2010,   2009],
                'y'     : [388950, 393007, 398449, 395972],
                'color' : [0, 0.50, 0.50],
            }
        }
        latex_bar_plot = bar_chart(data, caption='My pie chart 1', label='pie1', preamble=True)
        ```

        Output:
        -------

        ```latex
        \\documentclass[11pt]{article}
        \\usepackage{pgfplotstable}
        \\pgfplotsset{compat=1.17}
        \\usepackage{pgf-pie}
        \\usepackage{graphicx}
        \\usepackage{xcolor}
        \\begin{document}

        \\definecolor{color1}{rgb}{0.54,0,0}
        \\definecolor{color2}{rgb}{0,0.5,0.5}

        \\pgfplotstableread{
                x       men     women
                0       408184  388950
                1       408348  393007
                2       414870  398449
                3       412156  395972
        }\\datatable

        \\begin{figure}[!ht]
                \\centering
                \\resizebox{\\columnwidth}{!}{    
                \\begin{tikzpicture}
                \\begin{axis}[
                ylabel=ylabel,
                xlabel=xlabel,
                xtick=data,
                xticklabels={2012,2011,2010,2009},
                legend style={at={(0.5,-0.2)}, anchor=north,legend columns=-1},
                enlarge x limits=0.0005,
                ybar interval=0.7,
                width=10cm,
                height=7cm,
                ]

                \\addplot[style = {fill=color1}] table [y index=1] {\\datatable};
                \\addplot[style = {fill=color2}] table [y index=2] {\\datatable};

                \\legend{men,women}

                \\end{axis}
                \\end{tikzpicture}}
                \\caption{My bar chart 1}\\label{fig:bar1}
        \\end{figure}

        \\end{document}
        ```
    '''

    p = ""
    if preamble:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\usepackage{pgfplotstable}\n"
        p += "\\usepackage{pgf-pie}\n"
        p += "\\usepackage{graphicx}\n"
        p += "\\usepackage{xcolor}\n"
        p += "\\pgfplotsset{compat=1.17}\n"
        p += "\\begin{document}\n\n"

    # Define colors

    for i, col in enumerate(data):
        rgb = data[col]['color']
        p += "\\definecolor{color"+str(i+1)+"}{rgb}{"+str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])+"}\n"
    p += "\n"

    # Data in pgf format
    p += "\\pgfplotstableread{\n"
    p += "\tx\t" 
    for col in data: p += f"{col}\t"
    p += "\n\t"

    for i in range(len(data[col]['x'])):
        #x = data[col]['x'][i]
        p += f"{i}\t"
        for col in data:
            y = data[col]['y'][i]
            p += f"{y}\t"
        p += "\n\t"
    
    p += f"{i+1}\t"
    for col in data:
        y = data[col]['y'][i]
        p += f"{y}\t"
    p += "\n\t"


    p = p[:-1]
    p += "}\\datatable\n\n"
                 

    # Bar Chart
    p += "\\begin{figure}[!ht]\n"
    p += "\t\\centering\n"
    p += "\t\\resizebox{\columnwidth}{!}{\n"
    p += "\t\\begin{tikzpicture}\n"

    p += "\t\\begin{axis}[\n"
    p += "\t  ylabel="+str(y_label)+",\n"
    p += "\t  xlabel="+str(x_label)+",\n"
    p += "\t  xtick=data,\n"
    p += "\t  enlarge x limits=0.0005,\n"
    p += "\t  xticklabels={"

    for x in data[col]['x']:
        p += f"{x},"
    
    p = p[:-1]
    p += "},\n"
    p += "\t  legend style={at={(0.5,-0.2)}, anchor=north,legend columns=-1},\n"
    p += "\t  ybar interval=0.7,\n"
    p += "\t  width="+str(int(3*len(data[col]['x'])))+"cm,\n"
    p += "\t  height="+str(int(3*len(data[col]['x'])/1.4))+"cm,\n\t]\n\n"
    
    for i,_ in enumerate(data):
        p += "\t\\addplot[style = {fill=color"+str(i+1)+"}] table [y index="+str(i+1)+"] {\\datatable};\n"

    p += "\n"
    p += "\t\\legend{"

    for col in data: p += f"{col},"
    p = p[:-1]
    p += "}\n\n"
    p += "\t\\end{axis}\n"

    p += "\t\\end{tikzpicture}}\n"
    p += "\t\\caption{"+str(caption)+"}\\label{fig:"+label+"}\n"
    p += "\\end{figure}\n"

    if preamble:
        # End document
        p += "\n\\end{document}\n"

    return p