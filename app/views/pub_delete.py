from flask import render_template, request, redirect, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/delete/<pub_id>")
def pub_delete(pub_id):
    print('/pub/delete/<pub_id>')
    df_pubs = function.get_pubs()
    df_reviews = function.get_reviews()
    df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = True
    s3_resp = function.write_csv_to_s3(df_pubs.to_csv(sep=',', encoding='utf-8', index=False), config['aws_key_pub'])
    # print(s3_resp)
    df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'review_deletion'] = True
    s3_resp = function.write_csv_to_s3(df_reviews.to_csv(sep=',', encoding='utf-8', index=False),
                                       config['aws_key_review'])
    # print(s3_resp)
    return redirect(url_for('map_stations'))

        # except Exception as e:
        #     print(e)
        #     return render_template('404.html', error=e)
