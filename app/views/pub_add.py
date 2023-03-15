import json
import pandas as pd
from datetime import date
from flask import render_template
from app import app
from ..models.pub import Pub
from ..models.review import Review
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/add/")
def pub_add():
    print('/pub/add')
    stations_json = function.df_to_dict(function.get_records(config['aws_prefix_station'],
                                                             json.loads(config['model_station'])))

    new_pub_id = str(function.generate_uuid())
    date_now = date.today().strftime("%B %d, %Y")

    add_pub = Pub(pub_identity=new_pub_id, pub_deletion=False, place="", name="", address="", latitude=51.5,
                  longitude=-0.1, station_identity="", category="")

    add_review = Review(review_identity=str(function.generate_uuid()), pub_identity=new_pub_id, review_deletion=False,
                        visit=date_now,
                        star="", atmosphere=0, cleanliness=0, clientele=0, decor=0, entertainment=0, food=0,
                        friendliness=0, opening=0, price=0, selection=0, reviewer="")
    df_pub_review = pd.merge(pd.DataFrame([add_pub.__dict__]), pd.DataFrame([add_review.__dict__]), on='pub_identity')
    df_pub_review['station'] = ""
    df_pub_review['colour'] = config['colour_review']
    df_pub_review['score'] = 0
    pub_review_json = function.df_to_dict(df_pub_review)
    pubs_reviews_json = function.df_to_dict(function.get_pubs_reviews())
    return render_template("pub_add.html", form='add', google_key=config['google_key'], pubs_reviews=pubs_reviews_json,
                           pub_review=pub_review_json, stations=stations_json,
                           pub_review_fields=json.loads(config['column_all']),
                           pub_fields=json.loads(config['column_pub']),
                           review_fields=json.loads(config['column_review']),
                           pub_visible=json.loads(config['visible_pub']),
                           review_visible=json.loads(config['visible_review']),
                           list_required=json.loads(config['column_required']),
                           input_controls=json.loads(config['control_input']),
                           dropdown_controls=json.loads(config['control_dropdown']),
                           slider_controls=json.loads(config['control_slider']),
                           score_list=json.loads(config['column_score']))
