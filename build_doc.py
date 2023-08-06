"""
Build the documentation using pdoc (not pdoc3)
"""
import os
import shutil


# Clean documentation folder
shutil.rmtree('./docs/', ignore_errors=True)

os.mkdir("./docs/")
os.mkdir("./docs/pytexutils/")

# Build documentation
os.system("pdoc ./pytexutils -o ./docs --docformat numpy -t ./docs_assets/")

#shutil.copy2("./docs_assets/logo.png", "./docs/logo.png")
#shutil.copy2("./docs_assets/favicon.ico", "./docs/favicon.ico")