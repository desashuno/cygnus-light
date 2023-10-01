#!/bin/bash

virtualenv  venv  

source ./venv/bin/activate

pip install -r requeriments.txt  

llm install llm-llama-cpp

lm llama-cpp add-model models/Cygnus-7B.gguf 