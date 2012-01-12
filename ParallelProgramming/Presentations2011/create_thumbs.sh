#!/bin/bash

for pdf in cd/presentations/*.pdf; do
  pdfbase=`basename $pdf`
  lecture=${pdfbase%.pdf}

  echo $lecture

  # TODO:
  #  1. Too big density.
  #  2. Generate thumbnail from first JPG page.

  # Create 200x150 thumb.
  convert -scale 200x150 -density 300 $pdf\[0\] cd/images/presentations/thumbs/$lecture.jpg

  # Create full-size images for all slides.
  convert -scale 1024x768 -density 300 $pdf cd/images/presentations/$lecture.jpg
done
