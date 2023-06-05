#!/bin/bash

# rm -rf ./build/
rm -rf ./dist/

python -m black src/*.py

source .venv/Scripts/activate
pip freeze > requirements.txt
deactivate

python -m PyInstaller --distpath ./dist --workpath ./build --paths .venv/Lib/site-packages/ --add-data "data;data" --noconfirm --windowed --clean --onefile src/main.py
