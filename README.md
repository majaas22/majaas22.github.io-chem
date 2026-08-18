# Computational Simulation of Chemical Kinetics

## Overview
This project uses Python simulations to investigate how concentrations of both reactants and products change over time in chemical reactions. Instead of solving equations by hand, I built a mathematical model that simulates this.

## Simulations

### Simulation 1 – Simple Reversible Reaction
Simulates a simple reversible reaction (A ⇌ B). Investigates how the concentrations of reactants and products will change over time until dynamic equilibrium is reached. 

### Simulation 2 – Irreversible Step
An irreversible step was added to the simple reversible reaction (A ⇌ B → C). This allowed to investigate how an intermediate species behaves and what effect this has on the proportion of reactants converted to the final product.

### Simulation 3 – Temperature Dependence
The reaction system A ⇌ B → C was used in this simulation. Arrhenius equation is incorporated to investigate how varying temperature affects the reaction rate and time taken for the reaction to reach completion. 3 temperatures were simulated.

## Requirements
- Python
- NumPy
- Matplotlib

## Running the Simulations
Each simulation can be run directly from its corresponding Python file. No changes to the code or parameters are needed.

## Repository Structure
├── images/                    - contains png files of the generated graphs 
├── simulations/
│   ├── simulation_1.py
│   ├── simulation_2.py
│   └── simulation_3.py
├── code.html
├── conclusion.html
├── index.html
├── introduction.html
├── limitations.html
├── modelandmethod.html
├── references.html
├── resultsandanalysis.html
├──style.css
├──theory.html 
└── README.md

## Limitations
-Eulers Method: numerical approximation used to estimate solutions to differential equations when a discrete value cannot be found.  The accuracy of the result is dependent on the size of the time step chosen
-Perfect Mixing Assumed: assumes physical properties of the mixture, such as temperature and concentration, stay uniform throughout. Simplifies the calculations by allowing the concentration to be defined as a single value that changes with time. 
-Constant Conditions:  pressure, temperature and volume remained fixed. This can influence the behaviour of the system so accuracy is reduced.
-Simplified Reaction Mechanism: most real reactions involve several steps and multiple intermediates. Side reactions also occur leading to a loss in product.

