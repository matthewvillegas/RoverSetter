# How to publish RoverSetter as its own GitHub repository

**Publication is not yet complete.** Create the repository on your GitHub account before using the URL below.

## Fastest approach: browser + GitHub Desktop

1. Download the ready-to-publish ZIP and extract the `RoverSetter` folder.
2. On GitHub, choose **New repository** (or visit `https://github.com/new`). Owner: `matthewvillegas`, repository name: `RoverSetter`.
3. Use the description: **Independent mechanical engineering project investigating mobile monument handling, robotic positioning, and longitudinal stability through physical prototyping, CAD, and mathematical modeling.**
4. Select **Public** only after checking the exact files listed for publication. Keep **Initialize this repository with a README** unchecked (the folder already has one).
5. Open GitHub Desktop; choose **File → Add local repository** and select the extracted folder. If prompted, choose **Create a repository here**. Make the initial commit and publish/connect it to the GitHub repository you created.
6. Confirm that `https://github.com/matthewvillegas/RoverSetter` shows the CAD image and README.

## Git command line alternative

Create the empty repository via GitHub first. Inside the extracted `RoverSetter` folder:

```bash
git init -b main
git add .
git commit -m "Initial RoverSetter engineering case study"
git remote add origin https://github.com/matthewvillegas/RoverSetter.git
git push -u origin main
```

If `git init -b main` is unsupported, use `git init` then `git branch -M main` before committing. Authentication is handled by your local Git client/GitHub sign-in.

## Before making public

- Review first-person statements for historical accuracy; edit those you don't personally endorse.
- Ensure no private customer, cemetery, or business information is present.
- Verify the README CAD image, reports, and graph appear on GitHub.
- Keep the *separate private originals backup* in at least two locations. Its timestamps and SHA-256 checksums preserve current bytes, not historical creation dates.
- Do not upload the deleted old folder's imagined contents, present theoretical results as measured trials, or claim a verified lifting rating.

You can link the public repo from your existing portfolio website. No modification to your website is required to create this repository.
