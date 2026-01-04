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
   - Lists all generated LaTeX log files for visibility
   - Uploads compilation logs regardless of build success/failure

3. **Output**:
   - The generated PDF is uploaded as a GitHub Actions artifact (90-day retention)
   - LaTeX compilation logs are uploaded as artifacts (30-day retention)
   - Each workflow run creates:
     - `book-pdf` artifact: Contains `main.pdf` (only on successful builds)
     - `latex-logs` artifact: Contains all LaTeX log files (always uploaded for debugging)

### Accessing build artifacts

After a workflow run:

1. Go to the **Actions** tab in the GitHub repository
2. Click on the workflow run you're interested in
3. Scroll down to the **Artifacts** section
4. Download artifacts:
   - `book-pdf`: Contains the compiled PDF (only available on successful builds)
   - `latex-logs`: Contains compilation logs (.log, .aux, .blg, .bbl, .out, .toc, .fls, .fdb_latexmk files)

Both artifacts are downloaded as .zip files.

### Manual triggering

You can manually trigger a build from any branch:

1. Go to **Actions** tab
2. Select **Build Book PDF** workflow
3. Click **Run workflow** button
4. Select the branch you want to run the workflow from (the workflow will run on this branch)
5. Optionally, specify a different branch to build in the **"Branch to build PDF from"** input field
   - This allows you to run the workflow from `main` branch but build the PDF from the `book` branch
   - If left empty, it will build from the branch selected in step 4
6. Click **Run workflow**

**Note**: The workflow input allows you to build a PDF from a different branch than the one the workflow is running on. This is useful for testing changes on feature branches before merging to `book`.

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
1. Check the workflow logs in the Actions tab for error messages
2. **Download the `latex-logs` artifact** to examine detailed compilation logs:
   - `main.log`: Main LaTeX compilation log with error messages and line numbers
   - `main.aux`: Auxiliary file with cross-reference information
   - `main.blg`: BibTeX log file (if bibliography is used)
   - Other files: `.out`, `.toc`, `.fls`, `.fdb_latexmk` for additional debugging info
3. Common issues:
   - Missing figures: Ensure all PDF/PNG files referenced in main.tex are in the book/ directory
   - LaTeX syntax errors: Check the error log for line numbers
   - Missing bibliography: The workflow expects inline bibliography (using `\begin{thebibliography}`)

### Debugging features

The workflow includes comprehensive debugging support:
- **Always-available logs**: The `latex-logs` artifact is uploaded regardless of build success or failure
- **Immediate visibility**: Log files are listed in the workflow output before upload
- **Complete log coverage**: All LaTeX-generated files are captured for thorough debugging

### Future enhancements

Possible improvements to consider:
- Add automatic release creation for tagged versions
- Cache TeX Live packages for faster builds
- Add PDF validation/linting
