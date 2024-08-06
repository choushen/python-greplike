#!/bin/zsh

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: ./run_regex.sh <word> <regex>"
    exit 1
fi

# Assign arguments to variables
word=$1
regex=$2

# Run the Python script with the provided arguments
python3 main.py "$word" "$regex"
