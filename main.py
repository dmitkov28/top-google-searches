import json
import altair as alt
import pandas as pd
import streamlit as st

with open("data.json", 'r') as f:
    data = json.load(f)

processed_data = [{item.get("keyword"): item["keyword_info"]["search_volume"]} for item in
                  data.get("tasks")[0].get("result")[0].get("items")]

sorted_data = list(sorted(
    processed_data,
    key=lambda item: list(item.values())[0],
    reverse=True
))

chart_data = pd.DataFrame({
    'Category': [list(x.keys())[0] for x in sorted_data],
    'Value': [list(x.values())[0] for x in sorted_data]
})

st.title('Top Google Searches, US 2023')

chart = alt.Chart(chart_data).mark_bar().encode(
    x='Value',
    y=alt.Y('Category', sort='-x')
)

st.altair_chart(chart, use_container_width=True)
