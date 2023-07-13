#!/bin/bash

for f in test*.py; do
    output=$(python3 "$f" | tr '[:upper:]' '[:lower:]')

    if [[ $output ]]; then
        echo "Error: Test case failed in $f"
        exit 1
    fi
done