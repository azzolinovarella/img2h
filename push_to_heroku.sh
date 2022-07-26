#!/bin/bash

heroku git:remote -a img2h
heroku container:push web
heroku container:release web