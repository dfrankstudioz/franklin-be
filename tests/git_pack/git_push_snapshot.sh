#!/bin/bash

cd ~/docker/franklin-be
echo "[⬆️] Committing and pushing to GitHub..."
git init
git remote add origin git@github.com:your-user/franklin-be.git 2>/dev/null
git add .
git commit -m "Push Builder’s Edition snapshot"
git push -u origin main
