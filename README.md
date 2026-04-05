# Observatory

Interactive 3D star atlas with telescope control via API.

## Features

- Load star data from **Gaia Archive** (real astronomical data)
- Enrich stars with scientific names from **SIMBAD**
- Store data in **PostgreSQL** (DDD + CQRS architecture)
- Interactive **3D visualization** of the night sky (Plotly/Dash)
- Click on any star → automatically select a telescope → send coordinates via API
- Ready to integrate with **LCO** and **iTelescope** networks

## Tech Stack

- Python 3.11+
- PostgreSQL + psycopg2
- astroquery (Gaia, SIMBAD)
- Plotly + Dash (3D visualization)
- DDD + CQRS architecture

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/observatory.git

# Create virtual environment (Windows)
python -m venv venv
source venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
