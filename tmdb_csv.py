#cp -r /usr/local/lib/python3.11/site-packages/tmdbsimple* /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages

import tmdbsimple as tmdb
import csv
tmdb.API_KEY = ''

while True:
    print('\n')
    userInput = str(input('What titles do you want to search for: '))
    print('\n')
    search = tmdb.Search()
    response = search.movie(query=userInput)
    print('Name ID Popularity Release Date')
    for s in search.results:
        print(s['title'], s['id'],s['popularity'], s['release_date'])

    with open('movie_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title','id','popularity','release_date'])
        for s in search.results:
            writer.writerow([s['title'], s['id'],s['popularity'], s['release_date']])