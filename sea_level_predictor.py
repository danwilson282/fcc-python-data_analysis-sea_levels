import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit

    l1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_line = np.arange(df['Year'].min(),2051)
    y_pred = l1.intercept + l1.slope*x_line
    plt.plot(x_line,y_pred, color="green", label="Predicted 1880-2050")

    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    l2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    x_line2 = np.arange(2000,2051)
    y_pred2 = l2.intercept + l2.slope*x_line2
    plt.plot(x_line2,y_pred2, color="red", label="Predicted 2000-2050")
    # Add labels and title
    plt.legend(['Predicted 1880-2050','Predicted 2000-2050'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()