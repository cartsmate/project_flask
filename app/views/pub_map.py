from flask import render_template
from app import app


@app.route("/pub/map/stations")
def map_stations():
    print('/pub/map/stations')
    df_stations = get_stations()
    df_pubs_reviews = get_pubs_reviews()
    df_reviewed_only = df_pubs_reviews.loc[df_pubs_reviews['colour'] != constants.get("Colours", "NEW")]
    df_truncated = df_reviewed_only[['name', 'station_identity']]
    df_result = df_truncated.groupby(['station_identity'], as_index=False).count()
    df_result_latlng = pd.merge(df_result, df_stations, how='left', on='station_identity')
    df_sorted = df_result_latlng.rename(columns={'name': 'count'}).astype(str)
    df_sorted['colour'] = constants.get("Colours", "REVIEW")
    stations_json = df_to_dict(df_sorted)
    pubs_reviews_json = df_to_dict(df_pubs_reviews)
    view = "stations"
    return render_template('pub_map.html', google_key=config['google_key'], stations=stations_json,
                           pubs_reviews=pubs_reviews_json, icon_hole=False,
                           info_box=False, map_view=view, map_lat=51.5, map_lng=-0.1)
