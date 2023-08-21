#!/usr/bin/env bash

echo "Enter commit: "
read message

if [ -n "$message" ]
then
    git add .
    git commit -m "$message"
    git push
    clear
    echo "Git push was successfull"
else
    echo "Invalid commit message"
fi
