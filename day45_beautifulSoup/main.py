import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_page = response.text
# print(response.text)

soup = BeautifulSoup(movie_page, "html.parser")
# article = soup.find(class_="article-title-description__text")

articles = soup.find_all(class_="article-title-description__text")
# print(article)
# movie_title = article.find(class_="title").getText()

movie_list = []

for title in articles:
    # with open("./movies.txt", mode="w") as file:
    #     file.write(title.find(class_="title").getText())
    # print(title.find(class_="title").getText())
    movie_list.append(title.find(class_="title").getText())


# print(movie_list[::-1])
movies = movie_list[::-1]
# [::-1] this will reverse the order of the movie_list

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


