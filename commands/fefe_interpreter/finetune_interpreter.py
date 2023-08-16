async def finetune_interpreter(author_name):
    return [
{'role':'user','content':"""Create a 3D torus using plotly."""},
{'role':'assistant','content':f"""


import numpy as np
import plotly.graph_objects as go

# Create a 3D torus
theta = np.linspace(0, 2.*np.pi, 100)
phi = np.linspace(0, 2.*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
c, a = 2, 1
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

# Create a surface plot
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

# Set the title and axis labels
fig.update_layout(title='3D Torus', autosize=False,
                  width=800, height=800,
                  margin=dict(l=50, r=50, b=100, t=100))

# Set variable filename (required)
filename = "app/downloads/{author_name}/3d_torus.html"
# Save the figure as an HTML file
fig.write_html(filename)

# Show the figure
fig.show()
"""},
{'role':'user','content':"""Plot the function f(x) = 2x^2 + 3x +5. Add the tangent line at x = 1. Please add the equation of the tangent line as an annotation."""},
{'role':'assistant','content':f"""

import numpy as np
import plotly.graph_objects as go

# Define the function and its derivative
def f(x):
    return 2*x**2 + 3*x + 5

def df(x):
    return 4*x + 3

# Define the tangent line
def tangent_line(x, a):
    return df(a)*(x - a) + f(a)

# Define the x values
x = np.linspace(-10, 10, 400)
a = 1

# Create the figure
fig = go.Figure()

# Add the function to the figure
fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines', name="f(x) = 2x^2 + 3x + 5"))

# Add the tangent line to the figure
fig.add_trace(go.Scatter(x=x, y=tangent_line(x, a), mode='lines', name=f"Tangent line at x = {{a}}"))

# Set the title and labels
fig.update_layout(title="Function and Tangent Line", xaxis_title="x", yaxis_title="y")

# Add an annotation with the equation of the tangent line
slope = df(a)
intercept = f(a) - slope*a
fig.add_annotation(x=0, y=max(f(x)), text=f"Tangent line: y = {{slope:.2f}}x + {{intercept:.2f}}", showarrow=False)

# Save the figure
filename = "app/downloads/{author_name}/function_and_derivative.html"
fig.write_html(filename)

# Show the plot
fig.show()
"""},
{'role':'user','content':"""Can you plot it in plotly?"""},
{'role':'assistant','content':f"""
import numpy as np
import plotly.graph_objects as go

# Define the x and y range
x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 100)

# Create a meshgrid for x and y
X, Y = np.meshgrid(x, y)

# Define the z value as sin of sqrt of x^2 + y^2
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Create a 3D plot
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

# Update the layout
fig.update_layout(title='3D Sin Wave Surface', autosize=False,
                  width=500, height=500,
                  margin=dict(l=50, r=50, b=65, t=90))

# Save the figure
filename = "app/downloads/{author_name}/3D_sin_wave_plotly.html"
fig.write_html(filename)

# Show the plot
fig.show()
"""},
{'role':'user','content':"""Use mathematics to create a .png of a fractal."""},
{'role':'assistant','content':f"""
import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the fractal
width, height = 800, 800
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
max_iter = 256

# Generate a 2D grid of complex numbers
x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Initialize an empty image
img = np.zeros((width, height, 3), dtype=np.uint8)

# Generate the fractal
for i in range(width):
    for j in range(height):
        x, y = Z[i, j], 0
        for k in range(max_iter):
            if abs(y) > 2.0:
                break 
            y = y*y + x
        # Color gradient: change RGB with the number of iterations
        r, g, b = k % 8 * 32, k % 16 * 16, k % 32 * 8
        img[i, j] = (r,g,b)

# Save the fractal as a .png file
plt.imsave('app/downloads/{author_name}/fractal.png', img)

"""},
{'role':'user','content':"""Plot the function f(x) = x^2 between -1 and 1. Color int the portion between 0 and 1, and annotate the graph with the value of the integral of f(x) from 0 to 1."""},
{'role':'assistant','content':f"""
import numpy as np
import plotly.graph_objects as go
from scipy import integrate

# Function to integrate
f = lambda x: -3*x**2 + 2*x + 1

# Calculate integral
integral = integrate.quad(f, 2, 3)

x = np.linspace(-5, 5, 400)
y = f(x)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', fillcolor='rgba(0,176,246,0.2)', line_color='rgba(255,0,0,1)', name='f(x)=-3x^2+2x+1'))

fig.add_trace(go.Scatter(x=[2,3], y=[f(2),f(3)], fill='tozeroy', fillcolor='rgba(0,176,246,0.5)', name='Area'))

# Annotate integral value
integral_text = f"Integral = {{integral[0]:.2f}}"
fig.add_annotation(text=integral_text,
                   xref="paper", yref="paper",
                   x=0.8, y=0.8, showarrow=False)

fig.update_layout(title='Integration of f(x) = -3x^2+2x+1', xaxis_title='x', yaxis_title='f(x)')

fig.write_html("app/downloads/{author_name}/integral_plotly.html")

fig.show()
"""},
{'role':'user','content':"""Plot the function f(x) = x^2 between -1 and 1. Color int the portion between 0 and 1, and annotate the graph with the value of the integral of f(x) from 0 to 1."""},
{'role':'assistant','content':f"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the function
def f(x):
    return x**2

# Define the range for x
x = np.linspace(-1, 1, 1000)

# Calculate the integral from 0 to 1
integral, error = quad(f, 0, 1)

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot the function
plt.plot(x, f(x), 'b', linewidth=2)

# Fill the area between 0 and 1
x_fill = np.linspace(0, 1, 100)
plt.fill_between(x_fill, f(x_fill), color='skyblue', alpha=0.5)

# Annotate the graph with the value of the integral
plt.text(0.5, 0.2, f'Integral = {{integral:.2f}}', fontsize=12, ha='center')

# Set plot labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x^2')

# Save the plot as an image file
filename = "app/downloads/{author_name}/plot_integral.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""},
{'role':'user','content':"""Plot the function f(x) = x^2 between -1 and 1. Color in the portion between 0 and 1, and annotate the graph with the value of the integral of f(x) from 0 to 1 using plotly."""},
{'role':'assistant','content':f"""

import numpy as np
from scipy.integrate import quad
import plotly.graph_objects as go

# Define the function
def f(x):
    return x**2

# Calculate the integral from 0 to 1
integral, error = quad(f, 0, 1)

# Define the range for x and calculate y
x = np.linspace(-1, 1, 100)
y = f(x)

# Create a trace for the function
trace1 = go.Scatter(x=x, y=y, mode='lines', name='f(x) = x^2')

# Create a trace for the area under the curve between 0 and 1
x_fill = np.linspace(0, 1, 100)
y_fill = f(x_fill)
trace2 = go.Scatter(x=list(x_fill) + list(reversed(x_fill)),
                    y=list(y_fill) + [0]*len(y_fill),
                    fill='tozerox',
                    fillcolor='rgba(0,176,246,0.5)',
                    line=dict(color='rgba(255,255,255,0)'),
                    hoverinfo="skip",
                    showlegend=False)

# Create a layout with an annotation for the integral value
layout = go.Layout(annotations=[dict(x=0.5, y=0.2, text=f'Integral = {{integral:.2f}}', showarrow=False)])

# Create a figure from the traces and layout, and show it
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Save the figure
filename = "app/downloads/{author_name}/graph_of_integral.html"
fig.write_html(filename)

fig.show()
"""},
{'role':'user','content':"""Plot the golden spiral starting at radius 1."""},
{'role':'assistant','content':f"""

import numpy as np
import plotly.graph_objs as go

# Define the golden ratio
golden_ratio = (1 + np.sqrt(5)) / 2

# Define the angle and radius for generating the spiral
theta = np.linspace(-8 * np.pi, 8 * np.pi, 1000)
r = golden_ratio**(theta / (2*np.pi))

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create a scatter plot of the golden spiral
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# Set plot labels and title
fig.update_layout(title='Plot of the Golden Spiral',
                  xaxis_title='x',
                  yaxis_title='y')

# Save the figure
filename = "app/downloads/{author_name}/golden_spiral_plot.html"
fig.write_html(filename)

# Show the plot
fig.show()
"""},
{'role':'user','content':"""Plot f(x) = e^x mod 3 between -2 and 5. Use plotly."""},
{'role':'assistant','content':f"""

import numpy as np
import plotly.graph_objects as go

# Define the function
def f(x):
    return np.exp(x) % 3

# Generate x values
x = np.linspace(-2, 5, 400)

# Compute y values
y = f(x)

# Create the plot
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
fig.update_layout(title='Plot of f(x) = e^x mod 3', 
                  xaxis_title='x', 
                  yaxis_title='f(x)', 
                  autosize=False,
                  width=800,
                  height=500,
                  margin=dict(l=50,r=50,b=100,t=100,pad=4),
                  paper_bgcolor="LightSteelBlue",)

# Set variable filename (required)
filename = "app/downloads/{author_name}/modulo_function_plot.html"

# Save the figure
fig.write_html(filename)

# Open the HTML file in a web browser to view the plot
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""Plot the unit circle on the complex plane."""},
{'role':'assistant','content':f"""

import numpy as np
import plotly.graph_objects as go

# Define the unit circle in the complex plane
t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.sin(t)

# Create a scatter plot using Plotly
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# Set the aspect ratio to be equal so the circle doesn't look like an ellipse
fig.update_yaxes(
    scaleanchor="x",
    scaleratio=1,
  )

# Set plot labels and title
fig.update_layout(title='Unit Circle on the Complex Plane',
                  xaxis_title='Real Part',
                  yaxis_title='Imaginary Part')

# Save the figure
fig.write_html("app/downloads/{author_name}/unit_circle_complex_plane.html")

# Show the plot
fig.show()

"""},
{'role':'user','content':"""Plot the sphere f(u,v) = (cos(u)sin(v),sin(u)sin(v),cos(v)) for u between 0 and 2pi and v between 0 and pi using plotly."""},
{'role':'assistant','content':f"""
import numpy as np
import plotly.graph_objects as go

# Define the function
def f(u, v):
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    return (x, y, z)

# Create a grid of points at which to evaluate the function
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)

# Evaluate the function at each point in the grid
x, y, z = f(u, v)

# Create a 3D plot using Plotly
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Update layout
fig.update_layout(title='Plot of the Sphere', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

# Save the figure as a .html file before showing it
fig.write_html("app/downloads/{author_name}/sphere_plot.html")

fig.show()
"""},
{'role':'user','content':"""Plot sin(x) between -1 and 1. Fill the area under the curve."""},
{'role':'assistant','content':f"""

import numpy as np
import plotly.graph_objects as go

# Create an array of x values from -1 to 1
x = np.linspace(-1, 1, 1000)

# Define the function y = sin(x)
y = np.sin(x)

# Create the figure
fig = go.Figure()

# Add the line plot
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))

# Add the filled area
fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', mode='none', name='area'))

# Set the title and labels
fig.update_layout(title='sin(x) between -1 and 1', xaxis_title='x', yaxis_title='sin(x)')

# Save the figure
fig.write_html("app/downloads/{author_name}/sin_plot.html")

# Show the plot
fig.show()
"""},
{'role':'user','content':"""Save the titanic dataset to a csv file. Make sure to import seaborn as sns"""},
{'role':'assistant','content':f"""
import seaborn as sns
import pandas as pd

# Load the Titanic dataset from seaborn
titanic_data = sns.load_dataset('titanic')

# Save the Titanic dataset to a CSV file
filename = 'app/downloads/{author_name}/titanic_dataset.csv'
titanic_data.to_csv(filename, index=False)
"""},
]