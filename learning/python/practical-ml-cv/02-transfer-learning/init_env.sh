#!/bin/bash

#wget https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/download/train.zip
#kaggle competitions download -c dogs-vs-cats-redux-kernels-edition
unzip train.zip

mv train data
cd data
mkdir train val
mkdir train/cat train/dog
mkdir val/cat val/dog

ls | grep cat | sort -R | head -250 | xargs -I {} mv {} train/cat/
ls | grep dog | sort -R | head -250 | xargs -I {} mv {} train/dog/
ls | grep cat | sort -R | head -250 | xargs -I {} mv {} val/cat/
ls | grep dog | sort -R | head -250 | xargs -I {} mv {} val/dog/
