#!/bin/bash

cp .env ./api/
cp .env ./app/
heroku git:remote -a img2h
heroku stack:set container
git add .
git commit -m "novo deploy para heroku"
git push origin heroku