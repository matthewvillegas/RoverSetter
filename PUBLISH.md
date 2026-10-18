# RoverSetter — Public repository maintenance

**Published:** https://github.com/matthewvillegas/RoverSetter

This repository is a curated public engineering case study. It is not a fabrication package or a record of independently certified lifting capacity.

## Public-release checks

1. Confirm the README images and links resolve under the repository's `main` branch.
2. Review `docs/` and `HISTORY.md` for accurate distinction between designer recollections, CAD documentation, and hypothetical calculations.
3. Run the model locally:

   ```bash
   python -m unittest discover -s analysis/tests -v
   python analysis/src/roversetter_stability.py
   ```

4. Review the [Python test workflow](.github/workflows/python-tests.yml) in GitHub Actions. A successful run means the software tests and scenario reproduction executed; it does **not** physically validate the machine.
5. Keep the complete original CAD/STEP file backup separate from the curated public repository, with independent backups in at least two places.
6. Refresh `FILE_MANIFEST_SHA256.txt` after content changes when you want the snapshot checksum list to cover the new revision. The manifest intentionally excludes itself. Checksums prove byte identity, not the date a design was first created.

## Website linking

Link to this repository from your personal project portfolio. A separate `website/` directory is **not** included in the public GitHub repository.

## Evidence boundaries

- The three physical builds and approximately 70 lb test are the designer's historical account.
- Current CAD exports document the design, not independently authenticated as-built dimensions.
- The statics results are hypothetical model predictions, not experimentally measured reactions.
- Motor-startup pitching, original operating limits, and 2,000 lb lifting performance remain unverified.

Do not backdate files or present unperformed validation as completed work.
