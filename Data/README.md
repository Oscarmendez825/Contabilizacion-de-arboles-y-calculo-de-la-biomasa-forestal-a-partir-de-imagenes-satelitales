# Data Package

This package contains the necessary data for testing the DeepForest model. The data includes images of tree crowns and a file containing the names of the images along with the approximate count of tree crowns manually determined.

## Overview

The images in the `Images` folder serve as the test dataset for verifying the performance of the DeepForest model. These images are annotated with tree crown counts to facilitate model evaluation and testing.

## Contents

1. **Images**: This folder contains the images used as the test dataset for the DeepForest model. Each image is annotated with tree crown counts to aid in model evaluation.
2. **TestData.csv**: This CSV file contains metadata about the images present in the `Images` folder. It includes the filename of each image along with the approximate count of tree crowns manually counted in the image.

## Usage

The images in the `Images` folder can be used to test the performance of the DeepForest model. You can evaluate the model's accuracy by comparing its predictions against the manual counts provided in the `TestData.csv` file.

## How to Use

To use this dataset for testing the DeepForest model:

1. Clone or download this repository to your local machine.
2. Access the images in the `Images` folder to provide input to the DeepForest model.
3. Utilize the `TestData.csv` file to compare the model's predictions with the manual counts of tree crowns.
