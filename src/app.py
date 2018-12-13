from flask import Flask, render_template, jsonify, request
import pandas as pd
import datetime

from modules.scrape_nba import get_table
from modules.intelligent_machine import NBAChickenDinner


app = Flask(__name__)


@app.route('/')
def index():
    playoff_year = (datetime.datetime.now().year + 1)

    if 'playoff-year' in request.args:
        year = request.args.get('playoff-year')
        df = get_table(year)

        if int(year) == playoff_year:
            df.to_csv('static/data/regular_season.csv', index=False)

        nba = NBAChickenDinner(model='support_vector_machines.pkl', season_data=df)
        nba.prepare_data()
        df.W = [int(round(i)) for i in nba.run_model()]

    else:
        df = pd.read_csv('static/data/regular_season.csv')

    return render_template('index.html', table=df.to_html(index=False), current=playoff_year)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
