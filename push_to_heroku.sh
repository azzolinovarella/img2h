#!/bin/bash

cp .env ./app/
heroku git:remote -a img2h
heroku stack:set container
git add .
git commit -m "solucao 1 container heroku"
git push origin heroku