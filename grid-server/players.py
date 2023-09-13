from rounddata import datum
def player_names(data):
    name=set()

    for df in data:
        if 'name' in df.columns:
            name.update(df['name'].unique())
    return list(name)

players=player_names(datum)