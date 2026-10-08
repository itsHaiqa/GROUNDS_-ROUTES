"""Interactive campus route planning demo. Run: streamlit run app.py"""
import plotly.graph_objects as go
import streamlit as st
from routing import BUILDINGS, EDGES, build_graph, dijkstra

st.set_page_config(page_title='Campus Route Planner', page_icon='🗺️', layout='wide')
st.title('🗺️ Smart Campus Route Planner')
st.caption('A UVA-inspired algorithm demo using illustrative connections and fictional walking times — not real navigation or accessibility guidance.')

graph = build_graph()
left, right = st.columns([1, 2])
with left:
    st.subheader('Plan your route')
    start = st.selectbox('Starting building', sorted(BUILDINGS), index=sorted(BUILDINGS).index('Rice Hall'))
    end = st.selectbox('Destination', sorted(BUILDINGS), index=sorted(BUILDINGS).index('Clemons Library'))
    blocked = st.multiselect('Avoid buildings / temporary closures', sorted(BUILDINGS), help='The route will not pass through these buildings.')
    path, minutes = dijkstra(graph, start, end, blocked)
    if path:
        st.metric('Illustrative travel time', f'{minutes} min')
        st.success(' → '.join(path))
        st.caption(f'{len(path)-1} connection(s) · Dijkstra’s shortest-path algorithm')
    else:
        st.warning('No route available. Try removing a closure or changing endpoints.')
    st.info('To make this real-world ready, replace the sample graph with surveyed paths and accurate weights; validate accessibility and closures.')

with right:
    fig = go.Figure()
    for a, b, weight in EDGES:
        x1,y1 = BUILDINGS[a]
        x2,y2 = BUILDINGS[b]
        active = bool(path) and any({a,b} == {path[i],path[i+1]} for i in range(len(path)-1))
        fig.add_trace(go.Scatter(x=[x1,x2], y=[y1,y2], mode='lines', line=dict(color='#2563eb' if active else '#cbd5e1', width=6 if active else 2), hoverinfo='text', text=[f'{a} ↔ {b}: {weight} demo minutes']*2, showlegend=False))
    for name,(x,y) in BUILDINGS.items():
        fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers+text', text=[name], textposition='top center', marker=dict(size=17, color='#ef4444' if name in blocked else '#16a34a' if name in path else '#334155'), hovertemplate=name+'<extra></extra>', showlegend=False))
    fig.update_layout(height=620, margin=dict(l=20,r=20,t=20,b=20), xaxis=dict(visible=False,range=[0.05,0.98]), yaxis=dict(visible=False,range=[0.18,0.90],scaleanchor='x',scaleratio=1), plot_bgcolor='#f8fafc', paper_bgcolor='#f8fafc')
    st.plotly_chart(fig, use_container_width=True)
    st.caption('Schematic network, not a geographic map. Blue = selected route; red = closed building.')

with st.expander('How the algorithm works'):
    st.markdown('Each building is a **node**; each path is a weighted **edge**. Dijkstra’s algorithm explores the cheapest known path using a priority queue until it reaches the destination. Avoided buildings are excluded from consideration. With a binary heap, runtime is approximately **O((V + E) log V)**.')
