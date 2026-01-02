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

### Book Branch

The book branch contains a comprehensive LaTeX manuscript that provides the theoretical foundation for the course:

- **LaTeX Source Files**: 
  - `book/main.tex` - Main manuscript file (246KB, ~4200 lines) containing comprehensive theoretical content
  - `book/methods-old.tex` - Legacy manuscript file
  
- **Supporting Figures and Diagrams**:
  - Crystal structure diagrams: `crystal.pdf`, `lattice.pdf`, `brillouin.pdf`
  - Material-specific examples: `BaTiO3.pdf` (barium titanate), `Fe2SiO4-1.pdf` and `Fe2SiO4-2.pdf` (iron orthosilicate), `FeSe.pdf` (iron selenide)
  - Methodology illustrations: `diagram.pdf`, `gap-hyb.pdf` (hybrid functionals), `pseudopots-new.pdf` (pseudopotentials), `rare-earths.pdf`, `usp.pdf` (ultrasoft pseudopotentials)
  - Other assets: `Jacob.jpg`, `Fxs.png`

- **Book Content Structure**:
  - **Introduction**: Historical development of DFT and ab initio methods, from Schrödinger equation to modern density functional theory
  - **Chapter 1 - Electron Interactions**: Fundamental quantum mechanics, Hartree-Fock approximation, electronic correlations, homogeneous electron gas, hydrogen molecule example (Heitler-London method)
  - **Chapter 2 - Stany elektronowe w krysztale** (Electronic States in Crystals, in Polish): Crystal lattices, Bravais lattices, reciprocal space, Bloch's theorem, band structure theory
  - Additional chapters covering DFT theory, electronic structure methods, orbital-dependent functionals, insulators/semiconductors, electric polarization, van der Waals interactions, and many-body effects

## Key Technologies

- **Python 3**: Primary programming language
- **Jupyter Notebooks**: Interactive computational environment
- **ASE (Atomic Simulation Environment)**: Framework for atomic simulations
- **NumPy/SciPy/Matplotlib**: Scientific computing and visualization libraries
- **ABINIT**: Ab initio computational materials science calculator
- **LaTeX**: Document preparation system for the textbook manuscript

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

### LaTeX Guidelines
- Follow standard LaTeX best practices for academic manuscripts
- Maintain consistency in mathematical notation throughout the document
- Use descriptive labels for equations, figures, and sections (e.g., `\label{eq:schrodinger}`, `\label{fig:crystal}`)
- Ensure all references and citations are properly formatted using BibTeX
- Keep figure files organized in the `book/` directory
- Use comments to mark sections requiring review (e.g., `% **[REVIEW NEEDED]**: Description of issue`)
- Preserve multi-language content structure (English and Polish sections)

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
- LaTeX formatting and structure improvements
- Cross-referencing between notebooks and book content
- Figure and diagram organization in the book directory
- Build scripts for LaTeX compilation (if needed)

❌ **Academic tasks Copilot should NOT modify unless directly requested:**
- Lecture content in PDF files
- Physics equations and theoretical derivations
- Mathematical proofs and derivations in `main.tex`
- Scientific conclusions or interpretations
- Bibliography and references
- Academic authorship information

## Testing and Validation

- Test notebooks by running them in a clean Jupyter environment
- Verify that computational examples produce expected physical results
- Ensure backward compatibility with existing notebooks
- Check that notebooks run successfully in Binder environment
- Verify LaTeX compilation succeeds without errors (for book branch)
- Ensure all figures referenced in LaTeX are present in book directory

## Special Considerations

- **Performance**: Some calculations are computationally intensive; maintain reasonable execution times
- **Reproducibility**: Random seeds and computational parameters should be documented
- **Educational Value**: Changes should enhance learning, not just optimize code
- **Environment**: Must work in both local JupyterLab and cloud Binder environments
- **Multi-language Content**: The book manuscript contains sections in English and Polish (Polish sections start at Chapter 2/Rozdział 2)
- **Branch Structure**: Main branch focuses on interactive materials; book branch adds comprehensive textbook manuscript
- **Figure Management**: Keep book figures organized and ensure LaTeX references are correct

## Branch-Specific Notes

### Main Branch
- Focus: Interactive Jupyter notebooks and lecture PDFs
- Target: Hands-on computational exercises

### Book Branch
- Focus: Comprehensive LaTeX textbook manuscript with supporting materials
- Target: Theoretical foundation and detailed methodology
- Key File: `book/main.tex` (main manuscript source)
- Build Process: LaTeX compilation to PDF (build system TBD)

## Contact and Context

- **Authors**: Przemysław Piekarz, Paweł T. Jochym
- **Institution**: Institute of Nuclear Physics PAN, Cracow, Poland
- **Level**: PhD candidate coursework
- **License**: CC BY-SA 4.0
