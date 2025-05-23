#!/bin/bash

git init
git add .
git commit -m "Add web UI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/remove-bg-ui.git
git push -u origin main
