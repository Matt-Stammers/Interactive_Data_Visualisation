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

