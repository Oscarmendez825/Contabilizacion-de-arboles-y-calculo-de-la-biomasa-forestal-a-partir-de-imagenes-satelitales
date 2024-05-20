# Tree Counting and Forest Biomass Estimation

This project focuses on the automated counting of trees and estimation of forest biomass using satellite images. 

## Project Structure

The project is organized into the following main directories:

### 1. Forest Biomass Estimation
This directory contains the implementation of biomass estimation based on a specific equation from the study "Equation to estimate tree biomass in tropical forests of Costa Rica".

### 2. Data Package
This directory includes test data for verifying the performance of the DeepForest model, consisting of annotated images and metadata.

### 3. DeepForest Crown Tree Detector
This directory holds the implementation of the DeepForest model for detecting and counting tree crowns. It includes necessary scripts and installation instructions.

### 4. Tree Counting and Biomass Calculation GUI
This directory contains a Python script implementing a GUI for loading satellite images and using a machine learning model to count trees and calculate biomass.

### 5. Tree Crown Counting Image Processing Filters
This directory includes various image processing scripts for enhancing input images to improve the tree crown counting model's performance.

### 6. Main
This directory contains the main script for running the entire application.

## Installation

To install and set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Oscarmendez825/Contabilizacion-de-arboles-y-calculo-de-la-biomasa-forestal-a-partir-de-imagenes-satelitales.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Contabilizacion-de-arboles-y-calculo-de-la-biomasa-forestal-a-partir-de-imagenes-satelitales
   ```

3. **Install dependencies:**
   In each directory of the project, there are installers with the necessary libraries. Run each installer before executing the system.

## Usage

To execute the application:

1. Navigate to the `Main` directory:
   ```bash
   cd Main
   ```

2. Run the `Main.py` script:
   ```bash
   python Main.py
   ```

## Requirements

- Windows 10 or 11
- Git
- Python 3.11 or higher
- PIP

## Note

Make sure to execute each installer in the project directories to ensure all necessary libraries are installed.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
