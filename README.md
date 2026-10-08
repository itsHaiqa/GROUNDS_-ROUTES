# Smart Campus Route Planner

A Python/Streamlit demo that finds the lowest-cost route between UVA-inspired building nodes using **Dijkstra's shortest-path algorithm**. It includes an interactive network visualization and building closures.

## Run locally

1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python -m streamlit run app.py`.
5. Open the local URL printed by Streamlit.

## Tests

Run `python -m unittest discover -v`.

## Features

- Choose a starting point and destination
- Find a weighted shortest route
- Exclude buildings to simulate closures
- Visualize highlighted route segments
- Handle unavailable routes and invalid inputs

## Important limitation

**This is a demonstration, not a campus navigation service.** The network layout is schematic and edge weights are fictional examples, not real walking times, actual routes, or accessible-path information. To deploy responsibly, replace these with verified path data and accessibility attributes.

## How to extend it yourself

- Add verified geographic coordinates and walking paths
- Compare Dijkstra's algorithm with A* search
- Add wheelchair-accessible route filtering after validating path attributes
- Import a verified CSV of path segments
- Add unit tests for route closures and alternate-path choices

## Resume integrity

Describe this as an AI-assisted prototype unless you have personally run, tested, modified, and understood it. Do not claim independently authored code or real-world routing accuracy.
