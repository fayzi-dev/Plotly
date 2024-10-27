import plotly.express as px
import pandas as pd

# Create a sample dataset
data = {
    "sepal_length": [5.1, 4.9, 4.7, 6.3, 5.0, 5.8, 6.5, 5.7],
    "sepal_width": [3.5, 3.0, 3.2, 3.3, 3.6, 3.9, 2.8, 4.1],
    "species": ["setosa", "setosa", "setosa", "versicolor", "setosa", "virginica", "versicolor", "virginica"]
}

df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(
    df, 
    x="sepal_length", 
    y="sepal_width", 
    color="species", 
    size="sepal_length", 
    hover_name="species", 
    title="Scatter Plot of Sepal Dimensions"
)

# Show the plot
fig.show()
