import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def main():
    st.title("Folium Map in Streamlit")

    # Create a Folium map centered on a specific location
    map_center = [37.7749, -122.4194]  # San Francisco coordinates
    folium_map = folium.Map(location=map_center, zoom_start=12)

    # Add a marker to the map
    marker_text = "Hello, Folium!"
    folium.Marker(
        location=[37.7749, -122.4194],
        popup=folium.Popup(marker_text, parse_html=True),
        icon=folium.Icon(color="blue")
    ).add_to(folium_map)

    # Render the Folium map in Streamlit
    folium_static(folium_map)

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

if __name__ == "__main__":
    main()
