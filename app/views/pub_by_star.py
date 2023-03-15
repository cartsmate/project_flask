from flask import render_template, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/star/<star_id>")
def pub_by_star(star_id):
    print('/pub/star/<star_id>')
    df_pubs_by_star = function.get_pubs_by_star(star_id)
    pubs_rev_star_json = function.df_to_dict(df_pubs_by_star)
    view = "star"
    return render_template('pub_list.html', pubs_reviews=pubs_rev_star_json, map_view=view, map_lat=51.5, map_lng=-0.1)
