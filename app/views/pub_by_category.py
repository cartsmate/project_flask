from flask import render_template, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/category/<cat_id>")
def pub_by_category(cat_id):
    print('/pub/category/<cat_id>')
    df_pubs_by_category = function.get_pubs_by_category(cat_id)
    pubs_rev_cat_json = function.df_to_dict(df_pubs_by_category)
    view = "category"
    return render_template('pub_list.html', pubs_reviews=pubs_rev_cat_json, map_view=view, map_lat=51.5, map_lng=-0.1)
