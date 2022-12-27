from functools import reduce
import requests
from bs4 import BeautifulSoup
from sklearn import datasets


#1 На базе данных введенных вручную
temp_list = [int(element) for element in "1 2 3 4 5 6 7 8 9 10".split()]

tempSquar = list(map(lambda temp: temp ** 2, temp_list)) # Вывод элементов, равных квадрату заданных
print(tempSquar,"\n")

tempMultiply = reduce((lambda x,y: x * y), tempSquar) # Произведение всех элементов, полученных при возведении в квадрат
print(tempMultiply,"\n")

#2 На базе данных полученных при парсинге

url = 'https://perm.kinoafisha.info/cinema/'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
cinema_rating = soup.find_all("div", class_='cinemaList_item favBtn favBtn-active inner-mobile')

cinemaName = []
cinemaAddress = []
for cinema in cinema_rating:
    cinema_name = cinema.find('div', class_='cinemaList_name')
    cinemaName.append(cinema_name.text)
    cinema_address = cinema.find('div', class_='cinemaList_addr')
    cinemaAddress.append(cinema_address.text)

print('==========================================================')
print('СПИСОК КИНОТЕАТРОВ')
for i in range(5):
    print(f"Название кинотеатра: {cinemaName[i]}\nАдрес кинотеатра: {cinemaAddress[i]}\n\n")


url = 'https://www.kinoafisha.info/rating/movies/'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
film_rating = soup.find_all("div", class_='movieList_item movieItem movieItem-rating movieItem-position')
films =[]
for film in film_rating:
    film_name = film.find('a', class_='movieItem_title').text.strip()
    films.append(film_name)
films_name_len = map(len, films)

print('==========================================================')
print('СПИСОК ФИЛЬМОВ')
for i in films:
    print(f'{i}\t')
print('СПИСОК БУКВ В НАЗВАНИИ ФИЛЬМА')
for i in films_name_len:
    print(f'{i}\t букв')



# url1 = 'https://perm.kinoafisha.info/movies/rating/'
# req1 = requests.get(url1)
# soup1 = BeautifulSoup(req1.text, "html.parser")
# film_mark = soup1.find_all("div", class_='movieList_item movieItem  movieItem-grid grid_cell4')
#
# filmName = []
# filmInfo = []
# filmGenre = []
# filmMark = []
# filmList = []
#
# for film in film_mark:
#     film_name = film.find('a', class_='movieItem_title')
#     filmName.append(film_name.text)
#     film_info = film.find('span', class_='movieItem_subtitle')
#     filmInfo.append(film_info.text)
#     film_genre = film.find('span', class_='movieItem_genres')
#     filmGenre.append(film_genre.text)
#     film_mark = film.find_all('span', class_='mark_num')[0].text
#     #print(film_mark + '1')
#     filmMark.append(film_mark)
#     filmList.append(list(map(lambda temp: temp, filmMark)))
#
# print(filmMark)
# #filmRating = reduce((lambda x,y: x + y), filmList)
#
# for j in range(5):
#     print(f" Название фильма: {filmName[j]}\nИнформация о фильме: {filmInfo[j]}\nЖанр фильма: {filmGenre[j]}\nОценка фильма: {filmMark[j]}\n\n")
# print('\n\n\n')
# #print(filmRating / len(filmList))

#3 На базе данных из датасета
iris = datasets.load_iris()
listic = list(iris.target_names)
print(listic)
x = map(len, listic)
print(list(x))