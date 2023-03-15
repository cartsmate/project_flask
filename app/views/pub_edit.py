import json
from flask import render_template, request
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/edit/<pub_id>")
def pub_edit(pub_id):
    print('/pub/edit/<pub_id>')
    # try:
    stations_json = function.df_to_dict(function.get_records(config['aws_prefix_station'], json.loads(config['model_station'])))
    df_pub_review = function.get_pub_review(pub_id)
    pub_review_json = function.df_to_dict(df_pub_review)
    return render_template('pub_edit.html', form='edit', google_key=config['google_key'],
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

    # except Exception as e:
    #     print(e)
    #     return render_template('404.html', error=e)
