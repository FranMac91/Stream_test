import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

# Colors
colors = {
    "background": "#F5F5F5",
    "text": "#111111"
}

df = new_hotels_df
best_hotels = df.sort_values(by="Average_Score", ascending=False).head(10)

# ---- Top 10 Bar Chart ----
fig = px.bar(
    best_hotels,
    x="Average_Score",
    y="Hotel_Name",
    orientation="h",
    color="Average_Score",
    color_continuous_scale="Blues",
    title="Top 10 Best Hotels by Average Score"
)
fig.update_layout(
    paper_bgcolor=colors["background"],
    plot_bgcolor=colors["background"],
    font=dict(family="Arial", size=18, color=colors["text"])
)

# ---- Global Map ----
fig_geo = px.scatter_geo(
    df,
    lat="lat",
    lon="lng",
    color="Average_Score",
    hover_name="Hotel_Name",
    projection="natural earth",
    title="Hotel Map By Location"
)
fig_geo.update_layout(
    geo=dict(
        showland=True,
        landcolor="rgb(230,230,230)",
        showcountries=True
    ),
    paper_bgcolor=colors["background"],
    plot_bgcolor=colors["background"],
    font=dict(family="Arial", size=18, color=colors["text"])
)

# ---- Streamlit Layout ----
st.title("Hotel Review Dashboard")

st.plotly_chart(fig, use_container_width=True)

# Slider and map together
st.subheader("Filter Hotels by Average Score")
selected_score = st.slider(
    "Hotels by Average Score",
    min_value=float(df["Average_Score"].min()),
    max_value=float(df["Average_Score"].max()),
    value=float(df["Average_Score"].min()),
    step=0.1
)

filtered_df = df[df["Average_Score"] == selected_score]

fig_slider = px.scatter_geo(
    filtered_df,
    lat="lat",
    lon="lng",
    color="Hotel_Name",
    hover_name="Hotel_Name",
    projection="natural earth",
    title=f"Hotels With Average Score = {selected_score}"
)

fig_slider.update_layout(
    paper_bgcolor=colors["background"],
    plot_bgcolor=colors["background"],
    font=dict(family="Arial", size=18, color=colors["text"])
)

st.plotly_chart(fig_slider, use_container_width=True)

# Main map
st.subheader("All Hotels on Global Map")
st.plotly_chart(fig_geo, use_container_width=True)



