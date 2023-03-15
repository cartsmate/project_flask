import json
import pandas as pd
from flask import render_template, request
from app import app
from ..models.pub import Pub
from ..models.review import Review
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/<pub_id>", methods=['GET', 'POST'])
def pub_read(pub_id):
    print('/pub/<pub_id>')
    # try:
    df_pub_review = function.get_pub_review(pub_id)
    if request.method == 'GET':
        print('/pub/<pub_id>/GET')
        pub_review_json = function.df_to_dict(df_pub_review)
        return render_template("pub_read.html", form='read', google_key=config['google_key'],
                               pub_review=pub_review_json,
                               pub_review_fields=json.loads(config['column_all']),
                               pub_fields=json.loads(config['column_pub']),
                               review_fields=json.loads(config['column_review']),
                               pub_visible=json.loads(config['visible_pub']),
                               review_visible=json.loads(config['visible_review']),
                               dropdown_controls=json.loads(config['control_dropdown']),
                               slider_controls=json.loads(config['control_slider']),
                               input_controls=json.loads(config['control_input']),
                               score_list=json.loads(config['column_score']))
    if request.method == 'POST':
        print('/pub/<id_code>/POST')
        new_pub = Pub(pub_identity=pub_id, pub_deletion=request.form['pub_deletion'], place=request.form['place'],
                      name=request.form['name'], address=request.form['address'],
                      latitude=request.form['latitude'], longitude=request.form['longitude'],
                      station_identity=request.form['station_identity'], category=request.form['category'].lower())
        df_new_pub = pd.DataFrame([new_pub.__dict__])
        new_review = Review(review_identity=request.form['pub_identity'], pub_identity=pub_id,
                            review_deletion=request.form['review_deletion'],
                            visit=request.form['visit'],
                            star=request.form.get('star').lower(), atmosphere=request.form['atmosphere'],
                            cleanliness=request.form['cleanliness'], clientele=request.form['clientele'],
                            decor=request.form['decor'], entertainment=request.form['entertainment'],
                            food=request.form['food'], friendliness=request.form['friendliness'],
                            opening=request.form['opening'], price=request.form['price'],
                            selection=request.form['selection'], reviewer=request.form['reviewer'])
        df_new_review = pd.DataFrame([new_review.__dict__])
        print(df_new_review)
        if df_pub_review.empty:
            print('NEW RECORD')
            # # # # # NEW RECORD # # # # #
            place = request.form['place']
            df_place = df_pub_review.loc[df_pub_review['place'] == str(place)]
            if df_place.empty:
                print('UNIQUE PLACE ID')
                df_pubs = function.get_pubs()
                # # # # # NEW and UNIQUE PLACE ID RECORD - save record # # # # #
                df_pubs_appended = pd.concat([df_pubs, df_new_pub], ignore_index=True)
                s3_resp = function.write_csv_to_s3(df_pubs_appended.to_csv(sep=',', encoding='utf-8', index=False),
                                                   config['aws_key_pub'])
                # print(s3_resp)
                df_reviews = function.get_reviews()
                df_reviews_appended = pd.concat([df_reviews, df_new_review], ignore_index=True)

                s3_resp = function.write_csv_to_s3(df_reviews_appended.to_csv(sep=',', encoding='utf-8', index=False),
                                                   config['aws_key_review'])
                df_pub_review = function.get_pub_review(pub_id)
                pub_review_json = function.df_to_dict(df_pub_review)
                return render_template('pub_read.html', form='read', google_key=config['google_key'],
                                       pub_review=pub_review_json,
                                       pub_review_fields=json.loads(config['column_all']),
                                       pub_fields=json.loads(config['column_pub']),
                                       review_fields=json.loads(config['column_review']),
                                       pub_visible=json.loads(config['visible_pub']),
                                       review_visible=json.loads(config['visible_review']),
                                       dropdown_controls=json.loads(config['control_dropdown']),
                                       slider_controls=json.loads(config['control_slider']),
                                       input_controls=json.loads(config['control_input']),
                                       score_list=json.loads(config['column_score']))
            else:
                print('DUPLCATE PLACE ID')
                df_pubs_reviews = function.get_pubs_reviews()
                df_pub_review = df_pubs_reviews.loc[df_pubs_reviews['place'] == str(place)]
                pub_review_json = df_to_dict(df_pub_review)
                dupe_id = df_pub_review['pub_identity']
                return render_template("pop_up_dupe.html", pub_review=pub_review_json, dupe_id=dupe_id)
        else:
            print('EDITED PUB')
            # # # # # EDITED OLD RECORD - return to edit screen without saving # # # # #
            df_pubs = function.get_pubs()
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = request.form['pub_deletion']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'place'] = request.form['place']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'name'] = request.form['name']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'address'] = request.form['address']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'latitude'] = request.form['latitude']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'longitude'] = request.form['longitude']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'station_identity'] = request.form['station_identity']
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'category'] = request.form['category'].lower()

            s3_resp = function.write_csv_to_s3(df_pubs.to_csv(sep=',', encoding='utf-8', index=False),
                                               config['aws_key_pub'])

            df_reviews = function.get_reviews()
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'visit'] = request.form['visit']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'star'] = request.form.get('star').lower()
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'atmosphere'] = request.form['atmosphere']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'cleanliness'] = request.form['cleanliness']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'clientele'] = request.form['clientele']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'decor'] = request.form['decor']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'entertainment'] = request.form['entertainment']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'food'] = request.form['food']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'friendliness'] = request.form['friendliness']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'opening'] = request.form['opening']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'price'] = request.form['price']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'selection'] = request.form['selection']
            df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'reviewer'] = request.form['reviewer']

            s3_resp = function.write_csv_to_s3(df_reviews.to_csv(sep=',', encoding='utf-8', index=False),
                                               config['aws_key_review'])
            # print(s3_resp)
            df_pub_review = function.get_pub_review(pub_id)
            pub_review_json = function.df_to_dict(df_pub_review)
            # print('NO REVIEW')
            return render_template('pub_read.html', form='read', google_key=config['google_key'],
                                   pub_review=pub_review_json,
                                   pub_review_fields=json.loads(config['column_all']),
                                   pub_fields=json.loads(config['column_pub']),
                                   review_fields=json.loads(config['column_review']),
                                   pub_visible=json.loads(config['visible_pub']),
                                   review_visible=json.loads(config['visible_review']),
                                   dropdown_controls=json.loads(config['control_dropdown']),
                                   slider_controls=json.loads(config['control_slider']),
                                   input_controls=json.loads(config['control_input']),
                                   score_list=json.loads(config['column_score']))
    # except Exception as e:
    #     print(e)
    #     return render_template('404.html', error=e, identity=id_code)
