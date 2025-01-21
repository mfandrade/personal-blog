#!/bin/sh
# Este script contém os passos para se ter a aplicação rodando do zero.
# Se você já clonou este repositório localmente seu conteúdo é redundante.
# Neste caso, cada vez que quiser ter a aplicação rodando no seu ambiente
# de desenvolvimento apenas execute:
#
# make

# Clone
git clone https://github.com/mfandrade/personal-blog
cd personal-blog

# Selecione a versão
git checkout v1.0.0

# Execute
docker compose up --build --remove-orphans

echo '[INFO] Aplicação disponível em http://localhost:8080'
