"""
    This package contains basic functionalities to speed-up the process of creating 
    tables, images, figures for LaTeX documents.
    
"""


__all__ = ["make_image", "make_tabular_image", "make_table"]


from .figures import make_image, make_tabular_image
from .tables import make_table