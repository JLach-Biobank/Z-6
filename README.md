# BiohackPL

This tool was created during BioHack Bioinformatics Hackathon, 18-20 may 2018.

The purpose of this script is to use machine learning in detection of impact of various polymorphisms in the 15 chromosome sequence on eye colours. This script, for clarity, only deals with two types of eye colours: dark and bright.

## Requirements
These packages are required for using this tool:
category_encoders
matplotlib
numpy
sklearn
pandas


## Creation of CSV file
The script creates csv file from the a ped file.

## Detect useless polymorphisms
The script firsts deals with the dataset. It deletes all rows of data with unknown eye colour (marked as '-9') and later filters polymorphism by their uselessness and uniqueness. Such dataset is further filtered and data points unknown polymorphisms in certain positions (marked as '0 0') are also discarded.

## Detect best polymorphisms
The remaining data points are used to calculate difference in the polymorphisms at remaining positions within the tested group. The default value of uniqueness is 3%, which filters only polymorphisms positions that are different in 3%. These polymorphisms are saved as a new csv file. This set is tested pairwise: every polymorphism position is tested with each other.


## Prediction method 1
3 best, mutually independent polymorphisms in the dataset was used for training. Dataset is divided into training and validation part in 2:1 ratio. The variables were changed from categorical to numerical. SVC model was used for this part.

## Prediction method 2
The ped file was directly parsed into a pandas data frame for use in machine learning. The set is modified, by adding one-hot encoded binary variables and deleting unknown polymorphisms (marked as '0 0') in order to run the Random Forrest algorithm, from which the importance of different polymorphisms was retrieved.
