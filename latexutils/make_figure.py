from .make_table import make_table

def make_image(image_full_path, caption="table_caption", label="table_label", preable=False):
    '''
        Create a string with plain LaTeX file with an image.

        Keyword arguments:
        image_full_path -- string, path of the image in the LaTeX project
        caption -- string for the caption of LaTeX table (default: "table_caption")
        label -- string for the label of LaTeX table (default: "table_label")
        preable -- bolean value, if True the function will return a full LaTeX document, if False the function will return only the table (default: False)
    '''

    p = ""
    # LaTeX preamble
    if preable:
        p += "\\documentclass[11pt]{article}\n"
        p += "\\begin{document}\n\n"

    # Table
    p += "\\begin{figure}[!ht]\n"
    p += "\t\\centering\n"
    
    p += "\t\\includegraphics[width=\\columnwidth]{"+str(image_full_path)+"}\n"

    p += "\t\\caption{"+str(caption)+"}\\label{tab:"+label+"}\n"
    p += "\\end{figure}\n"

    if preable:
        # End document
        p += "\n\\end{document}\n"

    return p

def make_tabular_image(images_full_path, caption="table_caption", label="table_label", preable=False):
    '''
        Create a string with plain LaTeX file with a table of images.

        Keyword arguments:
        images_full_path -- 2D ndarry of strings, path of the image in the LaTeX project
        caption -- string for the caption of LaTeX table (default: "table_caption")
        label -- string for the label of LaTeX table (default: "table_label")
        preable -- bolean value, if True the function will return a full LaTeX document, if False the function will return only the table (default: False)
    '''

    images_full_path = images_full_path.astype(object)

    for i in range(images_full_path.shape[0]):
        for j in range(images_full_path.shape[1]):
            images_full_path[i,j] = "\\includegraphics[width=\\columnwidth]{"+str(images_full_path[i,j])+"}"

    p = make_table(None, images_full_path, caption=caption, label=label, preable=preable)

    return p