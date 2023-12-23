# CSCI128 final project
# parse spotify music genre to see what affects popularity the most (ex, acousticness, danceability, energy, etc.)

# 0 = instance_id, 1 = artist_name, 2 = track_name, 3 = popularity, 4 = acousticness, 5 = danceability
# 6 = duration_ms 7 = energy, 8 = instrumentalness, 9 = key, 10 = liveness, 11 = loudness, 12 = mode
# 13 = speechiness, 14 = tempo, 15 = obtained_date, 16 = valence, 17 = music_genre


import handle_data as hd
import interpret_data as id

if __name__ == "__main__":
    # create an index with index values of different things to compare popularity against
    dataIndex = {
        'Popularity': 3,
        'Acousticness': 4,
        'Danceability': 5,
        'Duration': 6,
        'Energy': 7,
        'Instrumentalness': 8,
        'Liveness': 10,
        'Speechiness': 13,
        'Tempo': 14,
        'Valence': 16
    }

    print('Parsing data...')
    data = hd.parse_data('music_genre_data.csv', dataIndex)

    # plot various data and calcualte correlation
    print('Interpreting data...')
    correlation = {}
    for key, value in dataIndex.items():
        if key == 'Popularity':
            continue
        hd.plot_data(data[3], data[value], "Popularity", key)
        correlation[key] = id.calculate_correlation(data[3], data[value])

    # find max and min values in correlation and print
    keyList = list(correlation.keys())
    valList = list(correlation.values())
    maxPos = valList.index(max(correlation.values()))
    minPos = valList.index(min(correlation.values()))

    print(f'OUTPUT Greatest Positive Correlation: {keyList[maxPos]}')
    print(f'OUTPUT Correlation Coefficient: {valList[maxPos]:.3f} \n')

    print(f'OUTPUT Greatest Negative Correlation: {keyList[minPos]}')
    print(f'OUTPUT Correlation Coefficient: {valList[minPos]:.3f}')
