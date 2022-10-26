from d3blocks import D3Blocks

# Initialize
d3 = D3Blocks()

# Import example
df = d3.import_example('energy')

# Create the heatmap
d3.heatmap(df, showfig=True, stroke='red', vmax=10, figsize=(700,700))