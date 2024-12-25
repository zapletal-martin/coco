#!/bin/bash

code2prompt ../../benchmark/reuse_single_file --output=out.txt
python3 gpt-4o-mini.py out.txt


