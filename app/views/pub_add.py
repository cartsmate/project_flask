from flask import render_template
from app import app


@app.route("/pub/add/")
def pub_add():
    print('/pub/add')
    stations_json = df_to_dict(get_records(constants.get("Aws_prefix", "STATION"),
                                           json.loads(constants.get("Columns", "STATION"))))

    new_pub_id = str(generate_uuid())
    date_now = date.today().strftime("%B %d, %Y")

    add_pub = Pub(pub_identity=new_pub_id, pub_deletion=False, place="", name="", address="", latitude=51.5,
                  longitude=-0.1, station_identity="", category="")

    add_review = Review(review_identity=str(generate_uuid()), pub_identity=new_pub_id, review_deletion=False,
                        visit=date_now,
                        star="", atmosphere=0, cleanliness=0, clientele=0, decor=0, entertainment=0, food=0,
                        friendliness=0, opening=0, price=0, selection=0, reviewer="")
    df_pub_review = pd.merge(pd.DataFrame([add_pub.__dict__]), pd.DataFrame([add_review.__dict__]), on='pub_identity')
    df_pub_review['station'] = ""
    df_pub_review['colour'] = constants.get("Colours", "REVIEW")
    df_pub_review['score'] = 0
    pub_review_json = df_to_dict(df_pub_review)
    pubs_reviews_json = df_to_dict(get_pubs_reviews())
    return render_template("pub_add.html", form='add', google_key=config['google_key'], pubs_reviews=pubs_reviews_json,
                           pub_review=pub_review_json, stations=stations_json,
                           pub_review_fields=json.loads(constants.get("Columns", "ALL_LIST")),
                           pub_fields=json.loads(constants.get("Columns", "PUB_LIST")),
                           review_fields=json.loads(constants.get("Columns", "REVIEW_LIST")),
                           pub_visible=json.loads(constants.get("Columns", "PUB_VISIBLE")),
                           review_visible=json.loads(constants.get("Columns", "REVIEW_VISIBLE")),
                           list_required=json.loads(constants.get("Columns", "REQUIRED")),
                           input_controls=json.loads(constants.get("Columns", "INPUT")),
                           dropdown_controls=json.loads(constants.get("Columns", "DROPDOWN")),
                           slider_controls=json.loads(constants.get("Columns", "SLIDER")),
                           score_list=json.loads(constants.get("Columns", "SCORE_REVIEW")))
