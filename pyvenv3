#!/usr/bin/env bash


echo "Bem vindo ao criador de venvs Python3"
nome_venv=$1

#LISTAR DIRETORIOS NO DIRETORIO CORRENTE
arquivos=$(ls)

function verificar_se_a_pasta_existe (){
	for i in $arquivos 
	do
		if [ "$i" == "$1" ]; then
			return 
			# echo "$i, $nome_venv"
		fi
	done
}


verificar_se_a_pasta_existe $nome_venv
echo $?
