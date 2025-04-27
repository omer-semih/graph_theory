# Define PYTHON conditionally based on availability of python3 or python
ifeq ($(shell command -v python3),)
    ifeq ($(shell command -v python),)
        $(error No suitable Python interpreter found)
    else
        PYTHON = python
    endif
else
    PYTHON = python3
endif


all: adjacencymatrix euleriancycles gt isomorphisms matchings multisource simplegraphs singlesource solverubik topologicalsort


adjacencymatrix:
	${PYTHON} -m pytest tests/adjacencymatrix*_test.py

euleriancycles:
	${PYTHON} -m pytest tests/euleriancycles*_test.py

gt:
	${PYTHON} -m pytest tests/gt*_test.py

isomorphisms:
	${PYTHON} -m pytest tests/isomorphisms*_test.py

matchings:
	${PYTHON} -m pytest tests/matchings*_test.py

multisource:
	${PYTHON} -m pytest tests/multisource*_test.py

simplegraphs:
	${PYTHON} -m pytest tests/simplegraphs*_test.py

singlesource:
	${PYTHON} -m pytest tests/singlesource*_test.py

solverubik:
	${PYTHON} -m pytest tests/solverubik*_test.py

topologicalsort:
	${PYTHON} -m pytest tests/topologicalsort*_test.py



