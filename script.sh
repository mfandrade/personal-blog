#!/bin/sh
#
# Este script contém os passos para se ter a aplicação rodando do zero.
#
git clone https://github.com/mfandrade/personal-blog
cd personal-blog
docker compose up --build --remove-orphans
if test -f .env.local; then
  www-browser http://localhost:8000
fi
