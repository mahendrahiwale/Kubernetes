#!/bin/bash

kubectl get pods

if [ $? -eq 0 ]
then
    echo "Success"
else
    echo "Fail"
fi