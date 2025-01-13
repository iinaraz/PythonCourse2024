import pandas as pd
import numpy as np

# Parameters
num_proteins = 20  # Number of proteins (rows)
num_samples_per_celltype = 5  # Number of samples per cell type
cell_types = ['CellType_A', 'CellType_B', 'CellType_C']  # Sorted cell types
log2_range = (2, 15)  # Log2 intensity range

# Generate random log2 intensity values
np.random.seed(42)  # For reproducibility
data = {
    f"{cell_type}_Sample_{i+1}": np.random.uniform(
        low=log2_range[0], high=log2_range[1], size=num_proteins
    )
    for cell_type in cell_types
    for i in range(num_samples_per_celltype)
}

# Create DataFrame with protein names
protein_names = [f"Protein_{i+1}" for i in range(num_proteins)]
expression_matrix = pd.DataFrame(data, index=protein_names)

# Output the matrix
print(expression_matrix)

# Save to CSV (optional)
expression_matrix.to_csv("protein_expression_matrix.csv")
