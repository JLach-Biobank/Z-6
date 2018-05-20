# BiohackPL

This tool was created during BioHack Bioinformatics Hackathon, 18-20 may 2018.

The purpose of this script is to use machine learning in detection of impact of various polymorphisms in the 15 chromosome sequence on eye colours. This script, for clarity, only deals with two types of eye colours: dark and bright.

Requirements
These packages are required for using this tool:
csv
pandas
matplotlib.pyplot
numpy
sklearn.datasets
sklearn.ensemble

Detection
The script firsts deals with the dataset. Creates a csv file from a ped file. This csv file is used in the statistical analysis and prediction methods.
It deletes all rows of data with unknown eye colour (marked as '-9') and later filters polymorphism by their uniqueness. Such dataset is further filtered and data points unknown polymorphisms in certain positions (marked as '0 0') are also discarded. The remaining data points are used to calculate difference in the polymorphisms at remaining positions within the tested group. The default value of uniqueness is 3%, which filters only polymorphisms positions that are different in 3%.


Prediction
The csv dataset is used in machine learning. The set is modified, by adding dummies and deleting unknown polymorphisms (marked as '0 0') in order to run the Random Forrest algorithm.
