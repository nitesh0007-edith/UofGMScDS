# IV Group Project — Multiview Weather Visualisation

Interactive multiview visualisation system built with Python, Altair, and Pandas for the Information Visualisation course at the University of Glasgow.

## Setup

```bash
pip install -r requirements.txt
```

## Generate All Pages

```bash
python src/index_page.py       # → output/index.html
python src/system_a.py         # → output/System_A.html
python src/system_b.py         # → output/System_B.html
python src/system_c.py         # → output/System_C.html
```

Or generate everything at once:

```bash
python src/index_page.py && python src/system_a.py && python src/system_b.py && python src/system_c.py
```

## View

Open `output/index.html` in any modern browser and click the system buttons to navigate to each dashboard.

## Project Structure

- `data/` — Source dataset (`clean_weather_data.csv`)
- `src/` — Python source files for generating HTML dashboards
- `output/` — Generated HTML files (landing page + 3 system dashboards)
- `evaluation/` — User evaluation templates and results
- `report/` — Report draft sections

## Systems

- **System A** — Category + Attribute Overview with metric dropdown and threshold sliders
- **System B** — Temporal Decomposition + Heatmap with generalised selection
- **System C** — Full Exploration with clickable legend filtering
