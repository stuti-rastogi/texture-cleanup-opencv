#!/bin/sh
for filename in tex/*.png; do
	echo "File $filename"
	python clean.py "$filename" "Clean/$(basename "$filename" .png)_clean.png"
	# python face.py "$filename"
done