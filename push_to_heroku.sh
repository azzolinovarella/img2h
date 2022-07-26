#!/bin/bash

heroku git:remote -a img2h
heroku stack:set container
git add .
git commit -m "new deploy to heroku"
git push origin heroku