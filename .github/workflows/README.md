# GitHub Actions Workflows

## Build Book PDF

The `build-book-pdf.yml` workflow automatically builds the LaTeX book manuscript into a PDF.

### How it works

1. **Triggers**: The workflow runs when:
   - Changes are pushed to the `book` branch in the `book/` directory
   - Pull requests target the `book` branch with changes in `book/` directory
   - Manually triggered from the Actions tab

2. **Build process**:
   - Checks out the repository
   - Uses the `xu-cheng/latex-action@v3` to compile the LaTeX document
   - Runs `latexmk` which automatically handles multiple pdflatex passes for cross-references
   - Compiles `book/main.tex` into `book/main.pdf`

3. **Output**:
   - The generated PDF is uploaded as a GitHub Actions artifact
   - Artifacts are available for download from the Actions tab for 90 days
   - Each workflow run creates a `book-pdf` artifact containing `main.pdf`

### Accessing the PDF

After a successful build:

1. Go to the **Actions** tab in the GitHub repository
2. Click on the workflow run you're interested in
3. Scroll down to the **Artifacts** section
4. Download the `book-pdf` artifact (will be a .zip file containing main.pdf)

### Accessing build logs for debugging

For every workflow run (successful or failed), LaTeX build logs are automatically uploaded:

1. Go to the **Actions** tab in the GitHub repository
2. Click on the workflow run you want to debug
3. Scroll down to the **Artifacts** section
4. Download the `latex-logs` artifact (will be a .zip file containing log files)
5. The artifact includes:
   - `main.log` - Main LaTeX compilation log with detailed error messages
   - `main.aux` - Auxiliary file with cross-references
   - `main.out` - Hyperref output file
   - `main.toc` - Table of contents data
   - `main.bbl` - Bibliography file (if generated)
   - `main.blg` - Bibliography log (if generated)

The `main.log` file is especially useful for debugging compilation errors, as it contains:
- Line numbers where errors occurred
- Detailed error messages from LaTeX
- Warnings about missing packages, figures, or references
- Information about which files were processed

### Manual triggering

You can manually trigger a build:

1. Go to **Actions** tab
2. Select **Build Book PDF** workflow
3. Click **Run workflow** button
4. Select the `book` branch
5. Click **Run workflow**

### LaTeX packages

The workflow uses a full TeX Live distribution that includes all required packages:
- graphicx, epsfig (for figures)
- amsmath (for mathematical notation)
- hyperref (for hyperlinks and cross-references)
- geometry (for page layout)
- longtable, dcolumn (for tables)
- bm (for bold math)
- And many more standard packages

### Troubleshooting

If the build fails:
1. Download the `latex-logs` artifact from the Actions tab (see "Accessing build logs" above)
2. Open `main.log` to see detailed error messages with line numbers
3. Check the workflow logs in the Actions tab for the summary output
4. Common issues:
   - Missing figures: Ensure all PDF/PNG files referenced in main.tex are in the book/ directory
   - LaTeX syntax errors: Check main.log for the specific line number and error message
   - Missing bibliography: The workflow expects inline bibliography (using `\begin{thebibliography}`)
   - Package conflicts: Check main.log for package loading errors or conflicts

### Future enhancements

Possible improvements to consider:
- Add automatic release creation for tagged versions
- Cache TeX Live packages for faster builds
- Add PDF validation/linting
- Generate HTML or other output formats alongside PDF
