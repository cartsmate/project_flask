from flask import render_template, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/location/<loc_id>")
def pub_by_location(loc_id):
    print('/pub/location/<loc_id>')
    df_pubs_by_station = function.get_pubs_by_station(loc_id)
    pubs_rev_loc_json = function.df_to_dict(df_pubs_by_station)
    view = "station"
    return render_template('pub_list.html', pubs_reviews=pubs_rev_loc_json, map_view=view, map_lat=51.5, map_lng=-0.1)
