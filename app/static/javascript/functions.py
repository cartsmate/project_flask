
def df_to_dict(df):
    df_dict = df.to_dict(orient='records')
    return df_dict


def get_records(aws_prefix, list_of_columns):
    df = read_s3_csv_to_df(aws_prefix, list_of_columns)
    del_consol = aws_prefix + "_deletion"
    df_false = df.loc[df[del_consol] != True]
    return df_false


def get_pubs():
    df_pubs = get_records(constants.get("Aws_prefix", "PUB"), json.loads(constants.get("Columns", "PUB")))
    return df_pubs


def get_pubs_station():
    df_pubs = get_pubs()
    df_stations = get_stations()
    df_stations = df_stations[['station_identity', 'station']]
    df_pubs_station = pd.merge(df_pubs, df_stations, how='left', on='station_identity')
    return df_pubs_station


def get_pubs_by_star(star_id):
    # print(star)
    df_pubs_reviews = get_pubs_reviews()
    # print(df_pubs_reviews)
    df_pubs_by_star = df_pubs_reviews.loc[df_pubs_reviews['star'] == star_id]
    # print(df_pubs_by_star)
    return df_pubs_by_star


def get_pubs_by_category(cat_id):
    df_pubs_reviews = get_pubs_reviews()
    df_pubs_by_category = df_pubs_reviews.loc[df_pubs_reviews['category'] == cat_id]
    return df_pubs_by_category


def get_pubs_by_station(loc_id):
    df_pubs_reviews = get_pubs_reviews()
    df_pubs_by_station = df_pubs_reviews.loc[df_pubs_reviews['station'] == loc_id]
    return df_pubs_by_station


def get_reviews():
    df_reviews = get_records(constants.get("Aws_prefix", "REVIEW"), json.loads(constants.get("Columns", "REVIEW")))
    return df_reviews


def get_stations():
    df_stations = get_records(constants.get("Aws_prefix", "STATION"), json.loads(constants.get("Columns", "STATION")))
    return df_stations


def get_pubs_reviews():
    # print('get_pubs_reviews')
    df_pubs_reviews = pd.merge(get_pubs_station(), get_reviews(), how='left', on='pub_identity')
    df_pubs_reviews['score'] = df_pubs_reviews.loc[:,
                           ['atmosphere', 'cleanliness', 'clientele', 'decor', 'entertainment', 'food', 'friendliness',
                            'opening', 'price', 'selection']].sum(axis=1)
    df_pubs_reviews['colour'] = np.where(df_pubs_reviews['reviewer'] == 'BOTH', constants.get("Colours", "RED"),
                                np.where(df_pubs_reviews['reviewer'] == 'ANDY', constants.get("Colours", "RED"),
                                np.where(df_pubs_reviews['reviewer'] == 'AVNI', constants.get("Colours", "RED"),
                                constants.get("Colours", "NEW"))))
    # df_pubs_reviews['colour'] = constants.get("Colours", "RED")
    df_pubs_reviews.fillna(0, inplace=True)
    # print(df_pubs_reviews)
    #     .drop(columns=['deletion_x', 'identity_y', 'deletion_y']) \
    #     .rename(columns={'identity_x': 'identity'})
    return df_pubs_reviews


def get_record(dfs, id_code):
    df = dfs.loc[dfs['pub_identity'] == id_code]
    return df


def get_pub_station(id_code):
    df_pub = get_pub(id_code)
    df_stations = get_stations()
    df_stations = df_stations[['station_identity', 'station']]
    df_pub_station = pd.merge(df_pub, df_stations, how='left', on='station_identity')
    return df_pub_station


def get_pub(id_code):
    df_pub = get_record(get_records(constants.get("Aws_prefix", "PUB"),
                                    json.loads(constants.get("Columns", "PUB"))), id_code)
    return df_pub


def get_review(pub_id):
    df_reviews = get_records(constants.get("Aws_prefix", "REVIEW"), json.loads(constants.get("Columns", "REVIEW")))
    df_review = df_reviews.loc[df_reviews['pub_identity'] == pub_id]
    return df_review


def get_pub_review(id_code):
    df_pub_review = pd.merge(get_pub_station(id_code), get_review(id_code), how='left', on='pub_identity')

    df_pub_review['score'] = df_pub_review.loc[:,
                               ['atmosphere', 'cleanliness', 'clientele', 'decor', 'entertainment', 'food',
                                'friendliness',
                                'opening', 'price', 'selection']].sum(axis=1)
    df_pub_review['colour'] = np.where(df_pub_review['reviewer'] == 'BOTH', constants.get("Colours", "RED"),
                                       np.where(df_pub_review['reviewer'] == 'ANDY', constants.get("Colours", "RED"),
                                                np.where(df_pub_review['reviewer'] == 'AVNI',
                                                         constants.get("Colours", "RED"),
                                                         constants.get("Colours", "NEW"))))
    return df_pub_review
