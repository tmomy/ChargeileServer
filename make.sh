#!/bin/bash

cname="dgg_appapi"
data_folder=$PROJECT_ROOT_PATH"/$cname/"


cp ./app $data_folder -rf
cp ./framework $data_folder -rf
cp ./createOrder $data_folder -rf
cp ./requirements.txt $data_folder -rf
cp ./run.py $data_folder -rf

mkdir -p $PROJECT_ROOT_PATH"/dgg_2nginx/www/static_file"
cp ./static_file/* $PROJECT_ROOT_PATH"/dgg_2nginx/www/static_file"  -rf


rm -f $data_folder"/make.sh"