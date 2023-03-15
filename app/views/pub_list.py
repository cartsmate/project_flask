from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/list")
def pub_list():
    print('/pub/list')
    pubs_reviews = function.get_pubs_reviews().sort_values(by=['score'], ascending=False)
    pubs_reviews_json = function.df_to_dict(pubs_reviews)
    view = "list"
    return render_template('pub_list.html', pubs_reviews=pubs_reviews_json, map_view=view, map_lat=51.5, map_lng=-0.1)
