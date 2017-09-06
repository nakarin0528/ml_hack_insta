import requests
import json
import csv
from bs4 import BeautifulSoup
links = ["https://www.instagram.com/p/BYq9uKNlPaM/?tagged=hashtag", "https://www.instagram.com/p/BYrKmNMget9/?tagged=hashtag", "https://www.instagram.com/p/BYrdpErnClr/?tagged=hashtag", "https://www.instagram.com/p/BYrODibh6Z3/?tagged=hashtag", "https://www.instagram.com/p/BYrRIN-DCDR/?tagged=hashtag", "https://www.instagram.com/p/BYrYJT_HpjA/?tagged=hashtag", "https://www.instagram.com/p/BYq29u1jbo6/?tagged=hashtag"]

likes = []
comments = []
pictures = []
users = []

for link in links:
    req = requests.get(link).text
    soup = BeautifulSoup(req, "html.parser")
    scripts = soup.find_all("script")
    for script in scripts:
        if script.text[:18] == "window._sharedData":
            break

    data = json.loads(script.contents[0][21:-1])
    
    #print("user: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))
    likes.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    #print("comments: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    comments.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    #print("likes: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    pictures.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))
    
    #print("url: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))

    # ユーザー名の配列に要素を追加
    users.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))

    print("################################################")

# ファイルに出力 user
#f = open('user.txt', 'w')
#for user in users:
#    f.write("https://www.instagram.com/" + user + "\n")
#f.close()

# ファイルに出力 likes
#f2 = open('likes.txt','w')
#for like in likes:
#    f2.write(like+"\n")
#f2.close()
# ファイルに出力 comments
#f3 = open('comments.txt','w')
#for comment in comments:
#    f3.write(comment+"\n")
#f3.close()
# ファイルに出力 pictures
#f4 = open('pictures.txt','w')
#for picture in pictures:
#    f4.write(picture+"\n")
#f4.close()

with open('instag.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    list2=[]
    tag=["user","url","likes","comments"] #各項目のタグ付け
for num in range(0, len(users)):
    listData = []   #listの初期化
    
    listData.append(users[num]) #listにユーザー名、画像url、いいね数、コメント数を追加
    listData.append(pictures[num])
    listData.append(likes[num])
    listData.append(comments[num])
    list2.append(listData) #新たなリストにlistDataの1行を1つの要素として追加
    
    with open('instag.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(tag) #ファイルにtagとリストを追加
        writer.writerows(list2)