#!/bin/bash

VENV_DIR="venv"

echo "Seleccione su sistema operativo:"
echo "1) Linux o macOS"
echo "2) Windows"
read -p "Ingrese el número de la opción deseada: " os

echo "Creando entorno virtual..."
if [ $os -eq 1 ]; then
    pip install --upgrade pip
    python3 -m venv $VENV_DIR
elif [ $os -eq 2 ]; then
    python.exe -m pip install --upgrade pip
    python -m venv $VENV_DIR
fi

echo "Activando entorno virtual..."
if [ $os -eq 1 ]; then
    . $VENV_DIR/bin/activate
elif [ $os -eq 2 ]; then
    source $VENV_DIR/Scripts/activate
fi

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Run.."
if [ $os -eq 1 ]; then
    python3 main.py
elif [ $os -eq 2 ]; then
    python main.py
fi
