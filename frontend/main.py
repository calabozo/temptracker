from flask import Flask
import pandas as pd
import sqlite3
from flask import render_template, request
from frontend.thermal import get_last_temp, get_last_entries
import plotly.graph_objs as plt
import plotly
import json
import plotly.express as px

app = Flask(__name__)

db_path='thermal.db'

@app.route("/")
def main():
    conn = sqlite3.connect(db_path)
    dict_temps = get_last_temp(conn)

    df = get_last_entries(conn, 60/5*24)
    fig = px.line(df, x="datetime", y="temp", line_group="id", color="id", title='Temperatura')
    hourly_ticks = pd.date_range(start=df['datetime'].min(), end=df['datetime'].max(), freq='H')
    fig.update_xaxes(tickvals=hourly_ticks, ticktext=[x.strftime('%H:%M') for x in hourly_ticks])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    conn.close()
    return render_template('index.html', temps=dict_temps, data=graphJSON)

if __name__ == "__main__":
    app.run()