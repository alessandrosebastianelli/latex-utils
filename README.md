# latex-utils



## Documentation

The documentation has been produced using [pdoc](https://pdoc.dev).

```pdoc latexutils -o ./docs```


## Build and install libraries

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

```python setup.py bdist_wheel```

after building the wheels, you can install the library bu running

```pip install dist/latex_utils-0.0.1-py3-none-any.whl```

**be aware that version (0.0.1) can change**.

