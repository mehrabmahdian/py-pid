#!/bin/bash
set -e

# Build Sphinx docs
cd ../docs
make html

# Go to the generated HTML folder
cd _build/html

# Initialize a new git repo (or reuse existing)
git init

# Add remote repo (change if needed)
git remote add origin https://github.com/mehrabmahdian/py-pid.git || true

# Checkout or create gh-pages branch
git checkout -B gh-pages

# Add all files
git add --all

# Commit changes
git commit -m "Deploy docs: $(date +'%Y-%m-%d %H:%M:%S')"

# Force push to gh-pages branch
git push -f origin gh-pages

echo "Docs deployed to GitHub Pages branch 'gh-pages'."
