# MENPs_Suppl
- Uncommenting line 97 in the "Simple Myelinated Axon.py" file, and running the file produces graphs of three action potentials along with the corresponding ion channel behavior.
- Uncommenting line 101 in the "Simple Myelinated Axon.py" file, and running the file produces strength-duration data.
- Uncommenting line 105 in the "Simple Myelinated Axon.py" file, and running the file produces a strength-duration curve based on the data.
- Running "Fig4.py" file produces four graphs of modeled I-V characteristics for an MENP.
- Uncommenting line 103 in the "Simple Myelinated Axon.py" file, and running the file produces the data for distance vs. number of MENPs to trigger an action potential.
- Uncommenting line 107 in the "Simple Myelinated Axon.py" file, and running the file produces a distance vs. number of MENPs curve based on the data.
- Uncommenting line 99 in the "Simple Myelinated Axon.py" file, and running the file produces the data for number of layers of MENPs vs. membrane voltage change.
- Uncommenting line 109 in the "Simple Myelinated Axon.py" file, and running the file produces a number of layers of MENPs vs. membrane voltage change curve based on the data.

Note that this work relies on Brian 2: https://brian2.readthedocs.io/en/stable/

Further note that this code makes use of C++ code generation: https://brian2.readthedocs.io/en/stable/introduction/install.html#requirements-for-c-code-generation

The code can also be run without C++ code generation, but that requires an additional line: prefs.codegen.target = "numpy"
