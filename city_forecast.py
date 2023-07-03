import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",
                   page_title="Meterological forecasts",
                   page_icon="https://avatars.githubusercontent.com/u/138516174?s=400&u=8b1a12374e90f23f8e63f779d1d7cf23315dadbb&v=4")
# List of cities for which forecasts are available
cities = pd.read_csv('data/cities.csv')

# Create sidebar for cities
city = st.sidebar.selectbox("Select a City", cities.city.str.capitalize())
# Create sidebar for meterological parameters
parameter = st.sidebar.selectbox("Select a Meterological parameter", ['Precipitation', 'Temperature', 'Wind Speeds', 'Mixing Height'])

# Title
st.title("Air Quality Forecasts - {}".format(city))

# Header
st.header(str(parameter))

city = city.lower()
if parameter=='Precipitation':
    st.subheader("Daily Total Precipitation (maps)")
    st.image('https://urbanemissions.info/forecasts/{}/stitched_precip_daysum_1by4.png'.format(city), width=1000)

    st.subheader('Time series (variation within Airshed)')
    st.image('https://urbanemissions.info/forecasts/{}/timeseries_precip.png'.format(city), width=1000)
    
    st.subheader('Hourly Animation')
    #st.markdown("![Alt Text](https://urbanemissions.info/forecasts/{}/animation_precip.gif)".format(city))
    st.video('https://urbanemissions.info/forecasts/{}/animation_precip.mp4'.format(city))
elif parameter=='Temperature':
    st.subheader("Day time Average Temperature at 2m (maps)")
    st.image('https://urbanemissions.info/forecasts/{}/stitched_temp2m_dayavg_1by4.png'.format(city), width=1000)

    st.subheader("Night time Average Temperature at 2m (maps)")
    st.image('https://urbanemissions.info/forecasts/{}/stitched_temp2m_ngtavg_1by4.png'.format(city), width=1000)

    st.subheader('Time series (variation within Airshed)')
    st.image('https://urbanemissions.info/forecasts/{}/timeseries_temp2m.png'.format(city), width=1000)

    st.subheader('Hourly Animation')
    #st.markdown("![Alt Text](https://urbanemissions.info/forecasts/{}/animation_temp.gif)".format(city))
    st.video('https://urbanemissions.info/forecasts/{}/animation_temp.mp4'.format(city))
elif parameter=='Wind Speeds':
    st.subheader("Day time Average Wind Speeds (maps)")
    st.image('https://urbanemissions.info/forecasts/{}/stitched_winds_dayavg_1by4.png'.format(city), width=1000)

    st.subheader("Night time Average Wind Speeds (maps)")
    st.image('https://urbanemissions.info/forecasts/{}/stitched_winds_ngtavg_1by4.png'.format(city), width=1000)

    st.subheader('Time series (variation within Airshed)')
    st.image('https://urbanemissions.info/forecasts/{}/timeseries_winds.png'.format(city), width=1000)

    st.subheader('Hourly Animation')
    #st.markdown("![Alt Text](https://urbanemissions.info/forecasts/{}/animation_winds.gif)".format(city))
    st.video('https://urbanemissions.info/forecasts/{}/animation_winds.mp4'.format(city))
else:
    st.subheader('Time series (variation within Airshed)')
    st.image('https://urbanemissions.info/forecasts/{}/timeseries_pblht.png'.format(city), width=1000)

    st.subheader('Hourly Animation')
    #st.markdown("![Alt Text](https://urbanemissions.info/forecasts/{}/animation_hmix.gif)".format(city, city))
    st.video('https://urbanemissions.info/forecasts/{}/animation_hmix.mp4'.format(city))

