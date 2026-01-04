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
   - The generated PDF is uploaded as a GitHub Actions artifact (90-day retention)
   - LaTeX build logs are uploaded as artifacts (30-day retention) for debugging
   - Each workflow run creates:
     - `book-pdf` artifact: Contains `main.pdf` (only on successful build)
     - `latex-build-logs` artifact: Contains `.log`, `.aux`, and other build files (always uploaded)

### Accessing the PDF and build logs

After a workflow run:

1. Go to the **Actions** tab in the GitHub repository
2. Click on the workflow run you're interested in
3. Scroll down to the **Artifacts** section
4. Download the artifacts:
   - **book-pdf**: The compiled PDF (available only if build succeeded)
   - **latex-build-logs**: LaTeX log files for debugging (always available)

Both artifacts are .zip files that need to be extracted after download.

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

1. **Download the build logs**: 
   - Go to the Actions tab and find the failed workflow run
   - Scroll to the **Artifacts** section
   - Download the `latex-build-logs` artifact
   - Extract the .zip file and open `main.log` to see detailed error messages

2. **Check the workflow logs**:
   - Click on the failed job in the Actions tab
   - Review the "Compile LaTeX document" step for immediate error output

3. **Common issues**:
   - Missing figures: Ensure all PDF/PNG files referenced in main.tex are in the book/ directory
   - LaTeX syntax errors: Check the .log file for line numbers and error context
   - Missing bibliography: The workflow expects inline bibliography (using `\begin{thebibliography}`)

### Future enhancements

Possible improvements to consider:
- Add automatic release creation for tagged versions
- Cache TeX Live packages for faster builds
- Add PDF validation/linting
