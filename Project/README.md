# Data and Computatations for Spring 2020 Undergraduate Research at UC Riverside

## Overview

In this project we apply tools and methods from Topological Data Analysis (specifically, Persistent Homology) to the data from [this study](https://www.cs.cmu.edu/~keystroke/) on keystroke dynamics. More specifically, we compute Persistence and Barcode diagrams from the subjects' typing data, and then we utilize the Bottleneck distance metric to try identify subjects by their typing data.

The file `bottleneck_distance.ipynb` contains an brief introduction and examples of Persistence diagrams, Barcode diagrams, and the Bottleneck distance.

The file `identify_users.ipynb` contains our approach to identifying subjects by their typing data using Persistent Homology.

Typing data can be found in the `data` directory.
