import math


def estimate_biomass(dap, delta):
    """
    This function calculates the biomass of a tree based on its diameter at breast height (dap)
    and basic specific weight (delta).

    Parameters:
    dap (float): The diameter at breast height of the tree in cm.
    delta (float): The basic specific weight of the tree in g/cm³.

    Returns:
    B (float): The estimated biomass of the tree in kg.
    """

    # Determine the value of X based on dap
    if dap >= 50:
        x = 1
    else:
        x = 0

    # Calculate B^(2/5) using the equation
    b_2_5 = 0.1438 + 0.2051 * dap + 0.3216 * dap * delta - 0.0744 * (dap - 50) * x
    # Calculate B by raising B_2_5 to the power of 5/2
    biomass = math.pow(b_2_5, 5/2)
    return biomass


def estimate_total_biomass(number_of_trees, dap, delta):
    """
    This function estimates the total biomass of a forest based on the number of trees and the average diameter at
    breast height (dap) and basic specific weight (delta) of the trees.

    Parameters:
    number_of_trees (int): The number of trees in the forest.
    dap (float): The average diameter at breast height of the trees in cm.
    delta (float): The average basic specific weight of the trees in g/cm³.

    Returns:
    total_biomass (float): The estimated total biomass of the forest in kg.
    """

    individual_biomass = estimate_biomass(dap, delta)
    total_biomass = individual_biomass * number_of_trees
    return total_biomass


# Example of using the function
dap_x = 60  # Diameter at breast height in cm
delta_x = 0.6  # Basic specific weight in g/cm³
trees = 10

biomass_x = estimate_total_biomass(trees, dap_x, delta_x)
print(f'The estimated biomass is {biomass_x} kg')
