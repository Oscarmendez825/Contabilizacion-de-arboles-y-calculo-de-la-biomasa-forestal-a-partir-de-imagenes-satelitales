# Forest Biomass Estimation

This folder focuses on the estimation of forest biomass using a specific equation derived from the study "Equation to estimate tree biomass in tropical forests of Costa Rica". The equation is used to estimate the biomass of an individual tree, which can then be used to calculate the total biomass of all trees in a given area, such as a region captured in a satellite image.

## Equation

The equation used to estimate the biomass of a tree is as follows:

$$
B^{2/5} = 0.1438 + 0.2051 \cdot dap + 0.3216 \cdot dap \cdot \delta - 0.0744 \cdot (dap - 50) \cdot X
$$

Where:

- **B**: Biomass of the tree in kg. This is the variable that we are estimating using the equation.
- **dap**: Diameter at breast height in cm. This is measured at 1.3 m height of the tree. This is a measure commonly used in forestry and biomass studies.
- **δ**: Basic specific weight in g/cm³. This is a measure of the density of a tree's wood. This measure can vary significantly between different tree species and can influence the amount of biomass a tree can store.
- **X**: Dichotomous variable. It takes the value of 1 if dap is greater than or equal to 50 cm, and 0 if dap is less than 50 cm.

## Total Biomass Calculation

The total biomass of all trees in a given area (such as a region captured in a satellite image) can be calculated as follows:

$$
\text{Total Biomass} = \text{Number of Trees} \times \text{Individual Tree Biomass}
$$

Where the individual tree biomass is estimated using the equation discussed above. Please note that the unit of the total biomass remains in kg.

This approach provides an estimate of the total forest biomass based on the number of trees detected in the satellite image and the estimated biomass of an individual tree. However, it's important to note that this is an approximation and the actual biomass may vary depending on factors such as the accuracy of the tree count and the variability in tree sizes and species.
