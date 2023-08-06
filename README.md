## LaTeX Utils - latexutils
This package contains basic functionalities to speed-up the process of creating tables, images, figures for LaTeX documents.

## Documentation
The documentation has been produced using [pdoc](https://pdoc.dev).

```pdoc latexutils -o ./docs```

and it is available [here](docs/index.html).

## Build and install the package

Move to latex-utils folder

latex-utils/  
├─ latexutils/  
├─ tests/  
├─ setup.py  
├─ LICENSE  
├─ README.md  
├─ docs  
├─ .gitignore  

and run

```python setup.py sdist bdist_wheel```

after building the wheels, you can install the library bu running

```pip install dist/latex_utils-0.0.1-py3-none-any.whl```

**be aware that version (0.0.1) can change**.


## Upload to PyPi

```python3 -m twine upload dist/* --verbose ```