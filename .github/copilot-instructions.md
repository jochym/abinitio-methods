# Copilot Instructions for Ab Initio Methods Repository

## Repository Overview

This repository contains an interactive academic book for computational solid state physics lectures aimed at PhD candidates. The materials combine theoretical lecture content with hands-on computational examples.

## Purpose

This is a work-in-progress (WIP) educational resource. Copilot is intended to help with the technical side of preparation for release of this material, not the academic content itself.

## Repository Structure

- **Lecture Materials**: PDF files in the `lecture/` directory covering topics from electron interactions to lattice thermodynamics
- **Interactive Notebooks**: Numbered Jupyter notebooks (`.ipynb` files) providing hands-on examples:
  - `00_Index.ipynb` - Main index and introduction
  - `01_Hydrogen_Molecule.ipynb` through `11_Nanoparticle_MD.ipynb` - Progressive exercises
- **Support Libraries**: 
  - `abilib.py` - Core support functions for the exercises
  - `ase_patch.py` - ASE (Atomic Simulation Environment) patches
  - `make-am-files.py` - Utility script for file generation
- **Data Directories**: `data/`, `psp/` contain supporting data files
- **Configuration**: `anphon/` and related files for phonon calculations

## Key Technologies

- **Python 3**: Primary programming language
- **Jupyter Notebooks**: Interactive computational environment
- **ASE (Atomic Simulation Environment)**: Framework for atomic simulations
- **NumPy/SciPy/Matplotlib**: Scientific computing and visualization libraries
- **ABINIT**: Ab initio computational materials science calculator

## Coding Guidelines

### General Principles
1. **Educational Focus**: Code should be clear and pedagogical, suitable for PhD students learning computational physics
2. **Reproducibility**: Maintain consistency in computational examples and results
3. **Documentation**: Comment code to explain physics concepts, not just implementation details
4. **License Compliance**: All code is under CC BY-SA 4.0 license

### Python Style
- Follow PEP 8 conventions for Python code
- Use clear, descriptive variable names that reflect physical quantities
- Include docstrings for functions explaining both the code and the physics
- Use type hints where they improve clarity

### Notebook Guidelines
- Ensure notebooks are self-contained and can run independently
- Include markdown cells explaining the physics and methodology
- Keep computational cells focused and well-commented
- Ensure outputs are cleared before committing (to reduce repository size)

### Dependencies
- Minimize external dependencies beyond the core scientific stack
- Document any new dependencies clearly
- Ensure compatibility with JupyterLab/Binder environments

## What Copilot Should Help With

✅ **Technical tasks Copilot should assist with:**
- Code refactoring and optimization
- Bug fixes in Python code and notebooks
- Improving code documentation and comments
- Ensuring consistent coding style
- File organization and repository structure
- Build and deployment configurations
- Testing and validation scripts
- Integration with JupyterLab/Binder environments

❌ **Academic tasks Copilot should NOT modify:**
- Lecture content in PDF files
- Physics equations and theoretical derivations
- Scientific conclusions or interpretations
- Bibliography and references
- Academic authorship information

## Testing and Validation

- Test notebooks by running them in a clean Jupyter environment
- Verify that computational examples produce expected physical results
- Ensure backward compatibility with existing notebooks
- Check that notebooks run successfully in Binder environment

## Special Considerations

- **Performance**: Some calculations are computationally intensive; maintain reasonable execution times
- **Reproducibility**: Random seeds and computational parameters should be documented
- **Educational Value**: Changes should enhance learning, not just optimize code
- **Environment**: Must work in both local JupyterLab and cloud Binder environments

## Contact and Context

- **Authors**: Przemysław Piekarz, Paweł T. Jochym
- **Institution**: Institute of Nuclear Physics PAN, Cracow, Poland
- **Level**: PhD candidate coursework
- **License**: CC BY-SA 4.0
