from csv import writer

import bs4
import requests

response = requests.get('https://movizland.icu/')


list = bs4.BeautifulSoup(response.text, "html.parser")
film = list.findAll(class_='BlockItem FeaturedBLock')

with open('FilmName.csv', 'w')as csv_file:
    csv_writer = writer(csv_file)
    header = ['FilmName', 'image Link','rating']

    for film in film:
        title = film.find(class_='BlockTitle').get_text().replace('\n', ' ')
        image_link = film.find(class_='BlockImageItem').find('img')['src']
        Rating = film.find(class_='StarsIMDB').find('strong').get_text()('\n', ' ')
        csv_writer.writerow(['title','image_link','Rating'])




