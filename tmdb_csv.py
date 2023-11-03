###

import tmdbsimple as tmdb
import csv

#used to authenticate with TMDB 
tmdb.API_KEY = ''

#adding variable from the input from the user 
#using variable to search tmdb 
#requesting tmbd for title, id, popularity, and release date 
#formatted the display output and sending output into csv 
#put into a loop to continue search 
while True:
    print('\n')
    userInput = str(input('What titles do you want to search for: '))
    print('\n')
    search = tmdb.Search()
    response = search.movie(query=userInput)
    print('{:<80} {:<20} {:<20} {:<20}'.format('Name','ID','Popularity','Release Date'))
    for s in search.results:
        print('{:<80} {:<20} {:<20} {:<20}'.format(s['title'], s['id'],s['popularity'], s['release_date']))

    with open('movie_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title','id','popularity','release_date'])
        for s in search.results:
            writer.writerow([s['title'], s['id'],s['popularity'], s['release_date']])