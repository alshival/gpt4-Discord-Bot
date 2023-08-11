finetune = [
{'role':'user','content':"""

filename:
```
app/downloads/sample_database_2.csv
```

columns:
```
Age              int64
Home State      object
Education       object
Eye Color       object
Attribute 1      int64
Attribute 2      int64
Attribute 3      int64
Attribute 4      int64
Attribute 5      int64
Attribute 6      int64
Attribute 7      int64
Attribute 8      int64
Attribute 9      int64
Attribute 10     int64
dtype: object
```

First 3 rows:
```
   Age   Home State    Education Eye Color  Attribute 1  Attribute 2  Attribute 3  Attribute 4  Attribute 5  Attribute 6  Attribute 7  Attribute 8  Attribute 9  Attribute 10
0   56     Delaware  High School      Blue            0            0            1            1            1            1            0            0            0             0
1   46  Mississippi          PhD     Hazel            1            1            0            0            0            1            0            0            1             0
2   32       Hawaii  High School     Hazel            0            0            1            0            1            1            1            0            0             1
```

request:
```
create a state choropleth leaflet containing the number of people who reside in each state.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import geopandas as gpd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/geojsons/us-states.json')

# Group by state and count the number of people
state_data = data.groupby('Home State').size().reset_index(name='Count')

# Merge data with gdf on state column
merged_data = gdf.merge(state_data, left_on='name', right_on='Home State')

# Create a choropleth map to show the count in each state
m = folium.Map(location=[37, -102], zoom_start=4)

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['Home State', 'Count'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of People'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/state_choropleth.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/iris_dataset.csv
```

columns:
```
sepal_length    float64
sepal_width     float64
petal_length    float64
petal_width     float64
species          object
dtype: object
```

First 3 rows:
```
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
```

request:
```
Create a pair plot using this data.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Assuming your data is in a DataFrame called `data`
# Load the iris dataset
data = pd.read_csv('app/downloads/iris_dataset.csv')

# Create a pair plot
sns.pairplot(data, hue='species')

# Set variable filename (required)
filename = "app/downloads/pair_plot.png"
# Save the pair plot as an image file
plt.savefig(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
Who are the youngest passengers who died?
```

"""},
{'role':'assistant','content':"""
import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Filter the dataset to get the youngest passengers who died
youngest_passengers_died = data[data['survived'] == 0].sort_values('age').head()

# Print the results
print(youngest_passengers_died.to_string())
"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
Who are the oldest passengers who died?
```

"""},
{'role':'assistant','content':"""
import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Filter the dataset to get the youngest passengers who died
youngest_passengers_died = data[data['survived'] == 0].sort_values('age', ascending=False).head()

# Print the results
print(youngest_passengers_died.to_string())

"""},
{'role':'user','content':"""

filename:
```
app/downloads/sample_database_2.csv
```

columns:
```
Age              int64
Home State      object
Education       object
Eye Color       object
Attribute 1      int64
Attribute 2      int64
Attribute 3      int64
Attribute 4      int64
Attribute 5      int64
Attribute 6      int64
Attribute 7      int64
Attribute 8      int64
Attribute 9      int64
Attribute 10     int64
dtype: object
```

First 3 rows:
```
   Age   Home State    Education Eye Color  Attribute 1  Attribute 2  Attribute 3  Attribute 4  Attribute 5  Attribute 6  Attribute 7  Attribute 8  Attribute 9  Attribute 10
0   56     Delaware  High School      Blue            0            0            1            1            1            1            0            0            0             0
1   46  Mississippi          PhD     Hazel            1            1            0            0            0            1            0            0            1             0
2   32       Hawaii  High School     Hazel            0            0            1            0            1            1            1            0            0             1
```

request:
```
Who has blue eyes?
```

"""},
{'role':'assistant','content':"""

import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the sample database
data = pd.read_csv('app/downloads/sample_database_2.csv')

# Filter the dataset to get the people with blue eyes
people_with_blue_eyes = data[data['Eye Color'] == 'Blue']

# Print the results
print(people_with_blue_eyes.to_string())
"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
create a plotly histogram for age of survivors and dead.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import plotly.express as px

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Set the dark theme using plotly
px.defaults.template = "plotly_dark"

# Create a histogram for age of survivors and dead
fig = px.histogram(data, x="age", color="survived", nbins=30)

# Save the figure
# Set save filename
save_filename = "app/downloads/titanic_plotly.html"
fig.write_html(save_filename)

# Show the plot
fig.show()
"""},
{'role':'user','content':"""

filename:
```
app/downloads/sample_database_2.csv
```

columns:
```
Age              int64
Home State      object
Education       object
Eye Color       object
Attribute 1      int64
Attribute 2      int64
Attribute 3      int64
Attribute 4      int64
Attribute 5      int64
Attribute 6      int64
Attribute 7      int64
Attribute 8      int64
Attribute 9      int64
Attribute 10     int64
dtype: object
```

request:
```
Create a state choropleth leaflet.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import geopandas as gpd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/geojsons/us-states.json')

# Group by state and count the number of cases
state_data = data.groupby('Home State').size().reset_index(name='Count')

# Merge data with gdf on state column
merged_data = gdf.merge(state_data, left_on='name', right_on='Home State')

# Create a choropleth map to show the count in each state
m = folium.Map(location=[37, -102], zoom_start=4)

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['Home State', 'Count'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Count'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/state_choropleth.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
Create an interactive histogram showing survivors and dead for males and females. Save the `.html` file and then `.show()` the figure.
```

"""},
{'role':'assistant','content':"""

import pandas as pd
import plotly.express as px

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Set the dark theme using matplotlib
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# Create an interactive histogram showing survivors and dead for males and females
fig = px.histogram(data, x="sex", color="survived", barmode="group")

# Save the figure as an HTML file
filename = "app/downloads/titanic_histogram.html"
fig.write_html(filename)

# Show the figure
fig.show()
"""},
{'role':'user','content':"""

filename:
```
app/downloads/sample_dataset.csv
```

columns:
```
Latitude         float64
Longitude        float64
Business Type     object
dtype: object
```

First 3 rows:
```
    Latitude   Longitude Business Type
0  26.178626  -86.813786    Restaurant
1  32.382985  -97.108596  Retail Store
2  33.379966 -107.710758           Gym
```

request:
```
create a folium map using latitude and longitude. Use red circle markers of radius 6.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the sample dataset
data = pd.read_csv('app/downloads/sample_dataset.csv')

# Create a folium map centered on the first latitude and longitude
m = folium.Map(location=[data['Latitude'].iloc[0], data['Longitude'].iloc[0]], zoom_start=10)

# Add red circle markers for each latitude and longitude
for index, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=6,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(m)

# Set variable filename (required)
filename = "app/downloads/folium_map.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/sample_dataset.csv
```

columns:
```
Latitude         float64
Longitude        float64
Business Type     object
dtype: object
```

First 3 rows:
```
    Latitude   Longitude Business Type
0  26.178626  -86.813786    Restaurant
1  32.382985  -97.108596  Retail Store
2  33.379966 -107.710758           Gym
```

request:
```
create a folium map using latitude and longitude. Use red circle markers of radius 6. Add the type of business to the tooltip.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the sample dataset
data = pd.read_csv('app/downloads/sample_dataset.csv')

# Create a folium map centered at the mean latitude and longitude
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=4)

# Add red circle markers to the map
for index, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=6,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        tooltip=row['Business Type']
    ).add_to(m)

# Set variable filename (required)
filename = "app/downloads/folium_map.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/state_population_counts.csv
```

columns:
```
State         object
Population     int64
dtype: object
```

First 3 rows:
```
     State  Population
0  Alabama     7423388
1   Alaska     7550634
2  Arizona     5304572
```

request:
```
Create a state choropleth, colored by the population count.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import geopandas as gpd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/geojsons/us-states.json')

# Load the state population counts
state_population = pd.read_csv('app/downloads/state_population_counts.csv')

# Merge data with gdf on state column
merged_data = gdf.merge(state_population, left_on='name', right_on='State')

# Create a choropleth map to show the population count in each state
m = folium.Map(location=[37, -102], zoom_start=4)

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['State', 'Population'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population Count'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/state_population_choropleth.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/state_population_counts.csv
```

columns:
```
State         object
Population     int64
dtype: object
```

First 3 rows:
```
     State  Population
0  Alabama     7423388
1   Alaska     7550634
2  Arizona     5304572
```

request:
```
Can you sector off the United States into `North, North East, East, South Easth`, etc, and calculate the total population?
```

"""},
{'role':'assistant','content':"""
import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the state population counts
data = pd.read_csv('app/downloads/state_population_counts.csv')

# Create a dictionary to map states to regions
region_mapping = {
    'North': ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont'],
    'North East': ['Delaware', 'Maryland', 'New Jersey', 'New York', 'Pennsylvania'],
    'East': ['District of Columbia', 'Florida', 'Georgia', 'North Carolina', 'South Carolina', 'Virginia', 'West Virginia'],
    'South East': ['Alabama', 'Arkansas', 'Kentucky', 'Louisiana', 'Mississippi', 'Tennessee'],
    'South': ['Oklahoma', 'Texas'],
    'Mid West': ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin'],
    'West': ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming'],
    'Pacific': ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']
}

# Create a new column for regions
data['Region'] = data['State'].map({state: region for region, states in region_mapping.items() for state in states})

# Calculate the total population by region
total_population_by_region = data.groupby('Region')['Population'].sum().reset_index()

# Save the total population by region as a CSV file
filename = "app/downloads/total_population_by_region.csv"
total_population_by_region.to_csv(filename, index=False)

# Show the total population by region
total_population_by_region
"""},
{'role':'user','content':"""

filename:
```
app/downloads/business_listings.csv
```

columns:
```
Business Name        object
Type of Business     object
Latitude            float64
Longitude           float64
Open                   bool
dtype: object
```

First 3 rows:
```
  Business Name Type of Business   Latitude  Longitude   Open
0    Business 0            Salon  40.712091 -73.785713   True
1    Business 1            Salon  40.439328 -73.573209  False
2    Business 2            Salon  40.423729 -73.551146   True
```

request:
```
Mark the location of each business on a leaflet using circle markers colored by whether they are currently open or not.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the business listings dataset
data = pd.read_csv('app/downloads/business_listings.csv')

# Create a folium map centered at the mean latitude and longitude
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

# Add circle markers to the map
for index, row in data.iterrows():
    color = 'green' if row['Open'] else 'red'
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=6,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        tooltip=row['Business Name']
    ).add_to(m)

# Set variable filename (required)
filename = "app/downloads/business_map.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/chicago_homicide_data_1.csv
```

columns:
```
id                        int64
case_number              object
date                     object
block                    object
iucr                      int64
primary_type             object
description              object
location_description     object
arrest                     bool
domestic                   bool
beat                      int64
district                  int64
ward                      int64
community_area            int64
fbi_code                 object
x_coordinate            float64
y_coordinate            float64
year                      int64
updated_on               object
latitude                float64
longitude               float64
location                 object
dtype: object
```

First 3 rows:
```
      id case_number                     date                 block  iucr primary_type          description location_description  arrest  domestic  beat  district  ward  community_area fbi_code  x_coordinate  y_coordinate  year               updated_on   latitude  longitude                                                                                                                            location
0  27595    JG320179  2023-06-28T23:04:00.000    036XX N KEDZIE AVE   110     HOMICIDE  FIRST DEGREE MURDER                ALLEY    True     False  1733        17    33              16      01A     1154405.0     1924119.0  2023  2023-07-06T16:46:09.000  41.947608 -87.707847  {'latitude': '41.947607802', 'longitude': '-87.707846683', 'human_address': '{"address": "", "city": "", "state": "", "zip": ""}'}
1  27600    JG321314  2023-06-29T19:40:00.000   066XX S STEWART AVE   110     HOMICIDE  FIRST DEGREE MURDER               STREET   False     False   722         7     6              68      01A     1174775.0     1860707.0  2023  2023-07-06T16:48:39.000  41.773168 -87.634868  {'latitude': '41.773168477', 'longitude': '-87.634868256', 'human_address': '{"address": "", "city": "", "state": "", "zip": ""}'}
2  27597    JG313398  2023-06-29T07:00:00.000  049XX S KILBOURN AVE   110     HOMICIDE  FIRST DEGREE MURDER               STREET   False     False   815         8    14              57      01A     1147193.0     1871572.0  2023  2023-07-06T16:48:39.000  41.803554 -87.735701  {'latitude': '41.803553993', 'longitude': '-87.735701327', 'human_address': '{"address": "", "city": "", "state": "", "zip": ""}'}
```

request:
```
plot the cities homicides on a map using red circle markers. Can you add the description to the text I see when I hover over a marker?
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the Chicago homicide dataset
data = pd.read_csv('app/downloads/chicago_homicide_data_1.csv')

# Create a folium map centered at the mean latitude and longitude
m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=10)

# Add red circle markers to the map
for index, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=6,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        tooltip=row['description']
    ).add_to(m)

# Set variable filename (required)
filename = "app/downloads/homicide_map.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/state_population_counts.csv
```

columns:
```
State         object
Population     int64
dtype: object
```

First 3 rows:
```
     State  Population
0  Alabama     7423388
1   Alaska     7550634
2  Arizona     5304572
```

request:
```
create a map and color in the states by the population size. Add the name of the state and population size to the hover tooltip.
```

"""},
{'role':'assistant','content':"""

import pandas as pd
import geopandas as gpd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/geojsons/us-states.json')

# Merge data with gdf on state column
merged_data = gdf.merge(data, left_on='name', right_on='State')

# Create a choropleth map to show the population in each state
m = folium.Map(location=[37, -102], zoom_start=4)

choropleth = folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['State', 'Population'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population'
).add_to(m)

# Add hover functionality
style_function = lambda x: {'fillColor': '#ffffff', 'color':'#000000', 'fillOpacity': 0.1, 'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 'color':'#000000', 'fillOpacity': 0.50, 'weight': 0.1}
NIL = folium.features.GeoJson(
    merged_data,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['State','Population'],
        aliases=['State: ','Population: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
)
m.add_child(NIL)
m.keep_in_front(NIL)
folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/state_population_choropleth.html"
# Save the map as an HTML file
m.save(filename)

# Open the HTML file in a web browser to view the map
import webbrowser
webbrowser.open(filename)
"""},
{'role':'user','content':"""

take `app/downloads/customer_statement-10_24_2021.txt` and save to `filename=app/downloads/customer_statement.txt`, but wrap the text to text width 65.

filename:
```
app/downloads/customer_statement-10_24_2021.txt
```

filetype:
```
.txt
```
            
"""},
{'role':'assistant','content':"""

import textwrap

# Read the content of the file
with open('app/downloads/customer_statement-10_24_2021.txt', 'r') as file:
    content = file.read()

# Wrap the text to text width 65
wrapped_content = textwrap.fill(content, width=65)

# Write the wrapped text to a new file
filename = "app/downloads/customer_statement.txt"
with open(filename, 'w') as file:
    file.write(wrapped_content)
"""}
]