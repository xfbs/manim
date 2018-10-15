#!/bin/bash

# fixes SVG files by simplt importing and re-exporting them.
for file in files/Tex/*.svg; do
  cairosvg "$file" -f svg -o "$file"
done
