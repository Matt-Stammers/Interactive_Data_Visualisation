# Getting started with Bokeh

# Boken is an interactive visualisation library in the style of D3.js, but it runs on very large datasets. Basically it's awesome

# To start with we can plot a basic figure of our admissions vs. deaths data:

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label= 'admissions (admissions per year)', y_axis_label='deaths (% of admissions who died)')

# Add a circle glyph to the figure p - this contains the x-axis and y-axis data respectively
p.circle(admissions, deaths)

# Call the output_file() function and specify the name of the file
output_file('admissions_vs_deaths.html')

# Display the plot
show(p)

# Now you have a basic visualisation plot displayed in the browser - Exciting. you can pan around it, zoom in and interact with the plot

# So that was square one. What if we wanted to display two sets of data? It is really easy in Bokeh.

# Create the figure: p
p = figure(x_axis_label= 'admissions (admissions per year)', y_axis_label='deaths (% of admissions who died)')

# Add a circle glyph to the figure p
p.circle(admissions_Portsmouth, death_rate_Portsmouth)

# Add an x glyph to the figure p
p.x(admissions_Southampton, death_rate_Southampton)

# Specify the name of the file
output_file('adm_death_Southampton_Portsmouth.html')

# Display the plot
show(p)

# and Voila, you have an interactive plot with two 'glyphs' on it. One is circular (Portmouth), the other X (Southampton).

# You can also specify colours, size and alpha values:

p.circle(admissions_Portsmouth, death_rate_Portsmouth, color='blue', size=10, alpha=0.8) # this will colour it blue
p.x(admissions_Southampton, death_rate_Southampton, color='blue', size=10, alpha=0.8)) # this will colour it red

# You can also plot python 'datetime' line graphs.

from bokeh.plotting import figure

p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='deaths')

# Plot date along the x axis and deaths along the y axis
p.line(date, deaths)

# Specify the name of the output file and then show
output_file('deaths.html')
show(p)

# You can then obviously change the colour as well:

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date, price, fill_color='white', size=4) # this one will leave white circles on the line which looks very nice.

# You can also use patches to build colour 'patches' on a plot:

# you do this by creating a list, say
x = [a_longitude, b_longitude, c_longitude]
y = [a_latitude, b_latitude, c_latitude]

# you then pass this to p.patches and specify the line color argument

# you can easily use numpy or pandas with bokeh 

# ok so first numpy arrays:

# Import numpy as np
import numpy as np

# Create array using np.linspace: x - this will generate a series of 100 values between 0 and 5
x = np.linspace(0,5,100)

# Create array using np.cos: y
y = np.cos(x) # this will make y the cosign of x.

# Add circles at x and y
p.circle(x, y, color='red') # This will add red circle glyphs

# Specify the name of the output file and show the result - sweet, that was easy. Arrays can obviously be passed in easily as well
output_file('numpy_example.html')
show(p)

# ok so now pandas:

# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('admissions_deaths.csv')

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='admissions', y_axis_label='deaths')

# Plot admissions vs deaths by color from the original dataframe!
p.circle(df['admissions'], df['deaths'], color=df['color'], size = 10)

# Specify the name of the output file and show the result
output_file('adm_vs_deaths.html')
show(p)

# Loving it. Ok so how is this all working? The answer my friend is the ColumnDataSource! The developers of Bokeh (currently over 230 contributors on github) have thought of everything.

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle(x='Admissions', y ='Year', source= source, size = 8, color='color')

# Specify the name of the output file and show the result
output_file('source_adms.html')
show(p)

# Ok now lets move on to some even cooler stuff. With bokeh you can create selection tools and hover tools for your data.

# to create a box selection tool you do the following: to use lasso change the tool

from bokeh.plotting import figure

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label = 'Admissions', y_axis_label = 'Death', tools = 'box_select') # or lasso_select which is freeform

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle(x = 'Admissions', y = 'Death', source = source, selection_color = 'red', nonselection_color = 'gray', nonselection_alpha = 0.2)

# Specify the name of the output file and show the result
output_file('Adm_selection_glyph.html')
show(p)

# to use the hover tools - this creates a graph that will highlight when hovered over. The tool has to be imported and used as below.

# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=8,
         fill_color='grey', alpha=0.2, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.6,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)

# Tadaa, you now have a hovergraph. This is amazing and looks beautiful.

# Finally one can build interactive colormaps - again this requires an import

from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper - ]american english] object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Portsmouth', 'Southampton', 'Chichester'],
                                      palette=['red', 'green', 'blue'])

p.circle('admissions', 'deaths', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

output_file('hosp_colormap.html')
show(p)

# And there we go. We have a lovely colour map!
