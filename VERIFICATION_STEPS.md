# Verification Steps for Push Trigger Fix

## After Merging This PR to the Book Branch

Follow these steps to verify that the push trigger is working correctly.

### Prerequisites
- This PR must be merged into the `book` branch (NOT main)
- Wait for the merge to complete successfully

### Step 1: Verify Workflow File Exists on Book Branch

```bash
# Check out the book branch
git checkout book
git pull origin book

# Verify the workflow file exists
ls -la .github/workflows/build-book-pdf.yml

# Expected: File should exist and be approximately 2507 bytes, 90 lines
```

### Step 2: Test Automatic Push Trigger

Make a small test change to trigger the workflow:

```bash
# Ensure you're on the book branch
git checkout book
git pull origin book

# Create a test change in the book directory
cd book
echo "% Test change $(date)" >> main.tex

# Commit and push the change
git add main.tex
git commit -m "Test: Trigger workflow with timestamp comment"
git push origin book
```

### Step 3: Verify Workflow Triggered

1. Go to the GitHub repository: https://github.com/jochym/abinitio-methods
2. Click on the **Actions** tab
3. Look for a new workflow run named "Build Book PDF"
4. The run should have been triggered by the push event
5. Status should show either:
   - 🟡 Running (yellow) - in progress
   - ✅ Success (green) - completed successfully
   - ❌ Failure (red) - build failed (check logs)

### Step 4: Check Workflow Details

Click on the workflow run to see:
- **Trigger**: Should show "push" not "workflow_dispatch"
- **Branch**: Should show "book"
- **Commit**: Should show your test commit message
- **Files changed**: Should list `book/main.tex`

### Step 5: Verify Build Artifacts (if successful)

If the workflow succeeds:
1. Scroll to the bottom of the workflow run page
2. Find the "Artifacts" section
3. You should see two artifacts:
   - `book-pdf` - The compiled PDF (only on success)
   - `latex-logs` - Compilation logs (always available)
4. Download and verify the PDF opens correctly

### Step 6: Clean Up Test Change

Remove the test comment from main.tex:

```bash
# Edit book/main.tex to remove the test comment line
# Or use git to revert:
git checkout book
git revert HEAD --no-edit
git push origin book
```

This will also trigger the workflow again (verifying it works consistently).

### Step 7: Test Pull Request Trigger

Create a test PR to verify PR triggers work:

```bash
# Create a test branch from book
git checkout book
git pull origin book
git checkout -b test-pr-trigger

# Make a small change
cd book
echo "% PR test $(date)" >> main.tex
git add main.tex
git commit -m "Test: PR trigger verification"
git push origin test-pr-trigger
```

Then:
1. Go to GitHub and create a PR from `test-pr-trigger` to `book`
2. Check the Actions tab - workflow should trigger automatically
3. Close the PR without merging after verification
4. Delete the test branch

### Step 8: Test Manual Trigger (should still work)

Verify manual triggering still works:

1. Go to **Actions** tab
2. Select **Build Book PDF** workflow
3. Click **Run workflow**
4. Verify options:
   - "Use workflow from" - select `book` (or any branch)
   - "Branch to build PDF from" - leave as `book` or change to test
5. Click green **Run workflow** button
6. Verify it starts and runs successfully

## Expected Results

✅ **All triggers should work:**
- Push to book branch → Automatic trigger ✓
- PR to book branch → Automatic trigger ✓  
- Manual dispatch → Manual trigger ✓

❌ **What should NOT trigger:**
- Push to `main` branch (workflow configured for book only)
- Push to other branches
- Changes outside the `book/` directory (filtered by paths)

## Troubleshooting

### Workflow doesn't trigger on push

1. **Check file location**: 
   ```bash
   git ls-tree book:.github/workflows/
   ```
   Should show `build-book-pdf.yml`

2. **Check YAML syntax**:
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('.github/workflows/build-book-pdf.yml'))"
   ```
   Should output nothing if valid

3. **Check changed files**:
   - Workflow only triggers for changes in `book/**`
   - Changes to other files won't trigger

4. **Check branch name**:
   - Workflow is configured for `book` branch only
   - Pushing to other branches won't trigger

### Workflow triggers but fails

1. **Download latex-logs artifact** from the failed run
2. **Check main.log** for LaTeX compilation errors
3. Common issues:
   - Missing figures
   - LaTeX syntax errors
   - Missing packages (unlikely with full TeXLive)

### Manual trigger doesn't work

1. **Check you're triggering from the right branch**:
   - Workflow file must exist on the branch you select in "Use workflow from"
   - You can trigger from `main` or `book` (both have the file after this PR)

2. **Check the branch input**:
   - The "Branch to build PDF from" input determines which branch's code to build
   - Defaults to `book` if not specified

## Success Criteria

The fix is successful when:
- [x] Workflow file exists on book branch
- [ ] Push to book/** files triggers workflow automatically
- [ ] PR to book branch triggers workflow automatically  
- [ ] Manual trigger continues to work
- [ ] Workflow runs successfully and produces PDF artifact

## Additional Testing

For thorough testing, try:
1. **Push with no changes in book/**: Should NOT trigger
2. **Push with changes only in book/**: SHOULD trigger
3. **Push with changes in book/ and elsewhere**: SHOULD trigger (book/ changes)
4. **Multiple rapid pushes**: Each should trigger separately
5. **PR with multiple commits**: Should trigger once per push to PR branch

## Rollback Plan

If issues occur after merge:
1. The workflow file can be removed from book branch
2. Or the triggers can be disabled by commenting out the `on:` section
3. Manual triggers will still work from other branches (main)

## Questions or Issues

If you encounter problems:
1. Check the Actions tab for error messages
2. Review the workflow logs for details
3. Compare the workflow file on book vs main
4. Ensure the PR was merged to book, not main

## Additional Documentation

- See `SOLUTION.md` for detailed problem analysis
- See `.github/workflows/README.md` for workflow documentation
- See GitHub Actions docs: https://docs.github.com/en/actions
