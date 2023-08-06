"""
Build the documentation using pdoc (not pdoc3)
"""
import shutil
import glob
import os

# Clean documentation folder
shutil.rmtree('./docs/', ignore_errors=True)

os.mkdir("./docs/")
os.mkdir("./docs/pytexutils/")

# Build documentation
os.system("pdoc ./pytexutils -o ./docs --docformat numpy --logo logo.png -t ./docs_assets/") #--logo https://casperfibaek.github.io/buteo/logo.png --favicon https://casperfibaek.github.io/buteo/favicon.ico

shutil.copy2("./docs_assets/logo.png", "./docs/logo.png")
shutil.copy2("./docs_assets/logo.png", "./docs/pytexutils/logo.png")
#shutil.copy2("./docs_assets/favicon.ico", "./docs/favicon.ico")

for p in glob.glob("./docs/pytexutils/*/"):
    shutil.copy2("./docs_assets/logo.png", p+"/logo.png")