# GitHub Push Instructions

The prepared repository is named **astro-ai-prosthetics** and is intended to be published at:

```text
https://github.com/justingracie-defender/astro-ai-prosthetics
```

The connected GitHub token in the current environment did not have permission to create repositories, so the safest next step is to create the empty public repository manually on GitHub and then push this prepared code.

## Option A — Create Empty Repo on GitHub, Then Let Manus Push

1. Go to GitHub and create a new **public** repository named `astro-ai-prosthetics` under `justingracie-defender`.
2. Do not initialize it with a README, license, or `.gitignore`; this package already contains those files.
3. Send the new repository URL back to Manus.
4. Manus can then push the existing local Git commit.

## Option B — Push Locally Yourself From the ZIP

From a machine with GitHub permissions, unzip the package and run:

```bash
cd astro-ai-prosthetics
git init -b main
git add .
git commit -m "Initial Astro — AI Prosthetics safety scaffold"
git remote add origin https://github.com/justingracie-defender/astro-ai-prosthetics.git
git push -u origin main
```

If you already initialized Git and `origin` already exists, run:

```bash
git remote set-url origin https://github.com/justingracie-defender/astro-ai-prosthetics.git
git push -u origin main
```
