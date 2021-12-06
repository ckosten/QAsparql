#!/bin/bash
set -e


echo "Downloading Glove"
cd glove/
curl http://www-nlp.stanford.edu/data/glove.840B.300d.zip -O -J -L
unzip -q glove.840B.300d.zip
