#!/bin/bash

echo "Hello"
export MY_NAME='ashish kumar singh'
set -a
var1='krishna'
sh called_script_1.sh ## - echo is not done. When export is used echo is done.
#source called_script_1.sh ## - echo is done
#./called_script_1.sh ## running like this permission denied. With export echo is done
#. ./called_script_1.sh ## - echo is done
#export MY_NAME