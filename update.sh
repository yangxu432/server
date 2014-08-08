#!/bin/sh

printf "Update sci-wms ... \n"
cd sci-wms
git checkout .
git pull
printf "Put back fvcom \n"
cd ..
./git_change.py
