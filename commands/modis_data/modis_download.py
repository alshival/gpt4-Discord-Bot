from app.config import *
from commands.bot_functions import *
import aiohttp
import folium
async def download_modis_data(period,region,interaction):
    author_name = interaction.user.name
    embed1 = discord.Embed(
        description = '**Region**: '+region,
            color = discord.Color.dark_red()
        )
    embed1.set_author(name=f"{interaction.user.name} pulled the latest MODIS data",icon_url=interaction.user.avatar)
    # Create app/downloads/{author_name} and return the path

    url_dict = {
        'global-24hr':"https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv",
        # US
        'us-24hr':"https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_24h.csv",
        'us-48hr':"https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_48h.csv",
        'us-7d':"https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_7d.csv",
        # Central America
        'central-america-24hr':"https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Central_America_24h.csv",
        'central-america-48hr':"https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Central_America_48h.csv",
        'central-america-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Central_America_7d.csv',
        # South America
        'south-america-24hr':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_24h.csv',
        'south-america-48hr':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_48h.csv',
        'south-america-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_7d.csv',
        # Europe
        'europe-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Europe_24h.csv',
        'europe-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Europe_48h.csv',
        'europe-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Europe_7d.csv',
        # Africa (North & Central)
        'africa-north-central-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Northern_and_Central_Africa_24h.csv',
        'africa-north-central-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Northern_and_Central_Africa_48h.csv',
        'africa-north-central-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Northern_and_Central_Africa_7d.csv',
        # Africa (South)
        'africa-south-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Southern_Africa_24h.csv',
        'africa-south-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Southern_Africa_48h.csv',
        'africa-south-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Southern_Africa_7d.csv',
        # Russia & Asia
        'russia-asia-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Russia_Asia_24h.csv',
        'russia-asia-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Russia_Asia_48h.csv',
        'russia-asia-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Russia_Asia_7d.csv',
        # South Asia
        'south-asia-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_Asia_24h.csv',
        'south-asia-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_Asia_48h.csv',
        'south-asia-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_Asia_7d.csv',
        # South East Asia
        'south-east-asia-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_SouthEast_Asia_24h.csv',
        'south-east-asia-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_SouthEast_Asia_48h.csv',
        'south-east-asia-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_SouthEast_Asia_7d.csv',
        # Australia & New Zealand
        'australia-new-zealand-24hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Australia_NewZealand_24h.csv',
        'australia-new-zealand-48hr': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Australia_NewZealand_48h.csv',
        'australia-new-zealand-7d':'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Australia_NewZealand_7d.csv'
    }
    
    modis_url = url_dict[period]
        
    # Save modis_url data into user_dir
    async with aiohttp.ClientSession() as session:
        async with session.get(modis_url) as resp:
            if resp.status == 200:
                data = await resp.read()
                # Save in downloads for interpreter. This copy is kept until the next session.
                modis_file_path = os.path.join('app/downloads/', 'MODIS_C6_1_Global_48h.csv')
                with open(modis_file_path, 'wb') as f:
                    f.write(data)
                # import to pandas and remove nan latitude and longitude values
                data = pd.read_csv(modis_file_path)
                data = data.dropna(subset=['latitude', 'longitude'])
                data.to_csv(modis_file_path,index=False)
                # Copy in user directory. This copy is removed after sending.
                user_dir = await create_user_dir(interaction.user.name)
                modis_user_file_path = os.path.join(user_dir, period+'.csv')
                data.to_csv(modis_user_file_path,index=False)
                # Generate map to return to the user.
                # Create a leaflet map with a black background
                m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=2, tiles='CartoDB dark_matter')
                
                # Add circle markers to the map
                for index, row in data.iterrows():
                    # Set the color of the marker based on the confidence level
                    if row['confidence'] < 50:
                        color = 'lightred'
                    else:
                        color = 'darkred'
                    
                    folium.CircleMarker(
                        location=[row['latitude'], row['longitude']],
                        radius=6,
                        color=color,
                        fill=True,
                        fill_color=color,
                        fill_opacity=0.6
                    ).add_to(m)
                
                # Set variable filename (required)
                filename = f"app/downloads/{interaction.user.name}/fires_map.html"
                # Save the map as an HTML file
                m.save(filename)
                
                # Open the HTML file in a web browser to view the map
                import webbrowser
                webbrowser.open(filename)
                
                files_to_send = await gather_files_to_send(interaction.user.name)
                await send_followups(interaction,'[MODIS Fire Datasource](https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-txt)',files=files_to_send,embed=embed1)
                await delete_files(interaction.user.name)