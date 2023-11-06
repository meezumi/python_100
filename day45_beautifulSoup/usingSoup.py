from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

news = soup.find_all(class_="titleline")
# print(news)
article_texts = []
article_links = []
article_scores = []
for heading in news:
    article_links.append(heading.find(name="a").get("href"))
    # print(heading.find(name="a").get("href"))
    article_texts.append(heading.find(name="a").getText())
    # print(heading.find(name="a").getText())

sub_parts = soup.find_all(class_="subtext")
# print(sub_parts)

for score in sub_parts:
    # print(score.find(class_="score").getText())
    # article_scores.append(score.find(class_="score").getText())
    article_scores.append(int(score.find(class_="score").getText().split()[0]))

topScore = max(article_scores)
topIndex = article_scores.index(topScore)

print(article_links)
print(article_texts)
print(article_scores)

# for getting just the point str and converting it into int
# article_scores.append(int(score.find(class_="score").getText().split()[0]))













# import lxml
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # passing here the str=html(markup), parser= whether it's a xml or html file
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # we want to get all the same type of tags in the html
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
# # a tag that sits inside p tag
#
# myname = soup.select_one(selector="#name")
# print(myname)
#
# yooo = soup.select(".heading")
# print(yooo)
