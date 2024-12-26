#!/bin/bash

#code2prompt ../../benchmark/reuse_single_file/context --output=out.txt
#python3 gpt-4o-mini.py out.txt ../../benchmark/reuse_single_file/prompt.txt

#code2prompt ../../benchmark/reuse_single_file_question/context --output=out2.txt
#python3 gpt-4o-mini.py out2.txt ../../benchmark/reuse_single_file_question/prompt.txt

code2prompt ../../benchmark/reuse_tensorflow/context --output=out3.txt
python3 gpt-4o-mini.py out3.txt ../../benchmark/reuse_tensorflow/prompt.txt
