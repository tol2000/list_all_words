#!/bin/bash

pushd ./out_binary_dir_by_pyinstaller
pyinstaller --onefile ../zho2.py
popd
