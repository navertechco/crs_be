#!/bin/bash

origin=$1
destination=$2
originname=$(basename $origin)
origindir=$(dirname $origin)


echo "ORIGIN: "$origin
echo "DESTINATION: "$destination
echo "ORIGINNAME: "$originname
echo "ORIGINDIR: "$origindir


if ! [ -d $destination ]; then
    cp -r $origin $destination
fi

shopt -s globstar
rename.ul -f "s/$originname/$destination/g" $destination/**/* 
# find $destination -type d -name "__pycache__" -exec rm -rf {} \;
find $destination -type f -exec sed -i "s/$originname/$destination/g" {} \;

cp -r $destination $origindir/$destination
rm -rf $destination

 



