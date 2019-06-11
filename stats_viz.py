import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral7
from bokeh.models.tools import HoverTool

df = pd.read_csv('alma_loans_by_date.csv')  # read data to dataframe

df['Loan Date'] = pd.to_datetime(df['Loan Date'])  # set column to datetime format
df.set_index('Loan Date', inplace=True)  #  set index to 'Loan Date' in order to group by month
g = df.groupby(pd.Grouper(freq="M"))  # group by month
new_df = g.sum()  # sum groupby object
new_df.reset_index(inplace=True)  # reset index 

source = ColumnDataSource(new_df)
# create the 'canvas' for the visualization
p = figure(plot_height=500, plot_width=950, x_axis_type='datetime')

# create line glyph
p.line(x='Loan Date', y='Loans (In House + Not In House)', line_width=2, source=source, color=Spectral7[0],
      legend='Total Loans')

# add metadata to the visualization
p.yaxis.axis_label = 'Total Loans'
p.xaxis.axis_label = 'Month'
p.title.text = 'Iliff Library Loans by Month'
p.legend.location = 'top_left'

# display visualization
show(p)