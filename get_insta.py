import requests
import json
from bs4 import BeautifulSoup
links = ["https://www.instagram.com/p/BYq9uKNlPaM/?tagged=hashtag", "https://www.instagram.com/p/BYrKmNMget9/?tagged=hashtag", "https://www.instagram.com/p/BYrdpErnClr/?tagged=hashtag", "https://www.instagram.com/p/BYrODibh6Z3/?tagged=hashtag", "https://www.instagram.com/p/BYrRIN-DCDR/?tagged=hashtag", "https://www.instagram.com/p/BYrYJT_HpjA/?tagged=hashtag", "https://www.instagram.com/p/BYq29u1jbo6/?tagged=hashtag", "https://www.instagram.com/p/BYr175fn6IN/?tagged=hashtag", "https://www.instagram.com/p/BYrI84FlzQe/?tagged=hashtag", "https://www.instagram.com/p/BYscs8xADin/?tagged=hashtag", "https://www.instagram.com/p/BYscsYWg1_3/?tagged=hashtag", "https://www.instagram.com/p/BYscpW3FjKI/?tagged=hashtag", "https://www.instagram.com/p/BYscpMZhyeA/?tagged=hashtag", "https://www.instagram.com/p/BYscmDnBm9s/?tagged=hashtag", "https://www.instagram.com/p/BYsciwhlDdb/?tagged=hashtag", "https://www.instagram.com/p/BYsciOAgXuK/?tagged=hashtag", "https://www.instagram.com/p/BYscdDKnOzc/?tagged=hashtag", "https://www.instagram.com/p/BYscagbgVak/?tagged=hashtag", "https://www.instagram.com/p/BYscWs7jCyp/?tagged=hashtag", "https://www.instagram.com/p/BYscWitHYok/?tagged=hashtag", "https://www.instagram.com/p/BYscWCXAxqJ/?tagged=hashtag"]

users = []

for link in links:
    req = requests.get(link).text
    soup = BeautifulSoup(req, "html.parser")
    scripts = soup.find_all("script")
    for script in scripts:
        if script.text[:18] == "window._sharedData":
            break

    data = json.loads(script.contents[0][21:-1])
    print("user: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))
    print("comments: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    print("likes: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    print("url: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))

    users.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))

    print("################################################")

f = open('user.txt', 'w')
for user in users:
    f.write("https://www.instagram.com/" + user + "\n")
f.close()
