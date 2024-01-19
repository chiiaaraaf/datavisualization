import streamlit as st
import plotly.graph_objects as go

# Define the parties and their corresponding percentages
parties = ['PS', 'PSD', 'CHEGA', 'BE', 'CDU', 'CDS-PP', 'IL', 'PAN']
percentages = [39, 26, 7, 7, 6, 3, 3, 3]

# Less bright color palette
party_colors = ['#8B0000', '#000080', '#2E8B57', '#D2691E', '#483D8B', '#C71585', '#FFD700', '#20B2AA']

# Create a Plotly bar chart with thinner bars and minimal gap between them
fig = go.Figure(data=[
    go.Bar(
        x=parties,
        y=percentages,
        marker_color=party_colors,
        marker_line_color='rgba(0,0,0,0)',
        marker_line_width=1.5,
        hoverinfo='y',
        width=0.4  # Thinner bars
    )
])


fig.update_layout(
    title_text='Political support among parties in Portugal, 2020',
    xaxis=dict(
        title="",
        showgrid=False,
        showticklabels=True,
        tickangle=0,
        tickfont=dict(size=12, color='black'),  # Set tick label color to black
        title_font=dict(color='black'),  # Set axis title color to black
    ),
    yaxis=dict(
        title="Percentage of support (%)",
        showgrid=False,
        range=[0, max(percentages) * 1.2],
        showticklabels=True,
        tickangle=0,
        tickfont=dict(size=12, color='black'),  # Set tick label color to black
        title_font=dict(color='black'),  # Set axis title color to black
    ),
    plot_bgcolor='rgba(255,255,255,1)',  # Set background color to white
    bargap=0.05
)

st.plotly_chart(fig)
