import os
import json
from configparser import ConfigParser
from flask import render_template
from app import app
from config import Configurations

config = Configurations()


@app.route("/")
@app.route("/index")
def index():
    print('/index')
    photo_array = json.loads(config.get_config().get("Columns", "SCORE"))
    return render_template('index.html', photo_array=photo_array, map_view="stations", map_lat=51.5, map_lng=-0.1,
                           row_loop=range(3), col_loop=range(4))
