#!/bin/bash

#comando para dar a permissão ao programa de escrever em um arquivo na pasta atual
sudo chmod o+w /home/maus/CEN0336_2023/

#captura o caminho atual através do comando "pwd"
caminho_atual="$(pwd)"
echo "O diretório atual é: $caminho_atual"

#volta até a pasta HOME
cd ~
caminho_atualizado="$(pwd )"

#adiciona ao começo do arquivo lista_HOME.txt o caminho atual (que no caso do meu home é: home/maus/)
echo "Estamos em: $caminho_atualizado" > lista_HOME.txt

#extrai uma lista detalhada da pasta atual (home) e salva no arquivo lista_HOME.txt
ls -l >> lista_HOME.txt
sudo mv lista_HOME.txt /home/maus/CEN0336_2023/

#retira a permissão cedida no começo do script
sudo chmod o-w /home/maus/CEN0336_2023/

#captura a data atual
data_atual=$(date)
echo "Hoje é: $data_atual"
