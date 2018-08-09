#!/usr/bin/env bash

files=( $(find -maxdepth 1 -name "*.py" -type f -not -name "*example*" -print0 | xargs -0) )

for f in "${files[@]}" ; do
    f=`echo "${f}" | sed 's/\.\///g'`

    echo "copying ${f}" &&
    ampy put "${f}" "${f}" &&
    sleep .5
done