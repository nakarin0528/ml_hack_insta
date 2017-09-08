import requests
import json
import csv
from bs4 import BeautifulSoup
links = ["https://www.instagram.com/p/BYwN2u4gqNb/?tagged=monochrome", "https://www.instagram.com/p/BYwvPm6nUFf/?tagged=monochrome", "https://www.instagram.com/p/BYwJLqFjTmb/?tagged=monochrome", "https://www.instagram.com/p/BYwBkBPnIOT/?tagged=monochrome", "https://www.instagram.com/p/BYwKMXugkJY/?tagged=monochrome", "https://www.instagram.com/p/BYwO6yfjpGM/?tagged=monochrome", "https://www.instagram.com/p/BYwvOiulx6p/?tagged=monochrome", "https://www.instagram.com/p/BYwJbUeH0on/?tagged=monochrome", "https://www.instagram.com/p/BYwyy0KnMRs/?tagged=monochrome", "https://www.instagram.com/p/BYw4lZYjCig/?tagged=monochrome", "https://www.instagram.com/p/BYw4kl4Day9/?tagged=monochrome", "https://www.instagram.com/p/BYw4kiOj-vZ/?tagged=monochrome", "https://www.instagram.com/p/BYw4kXkAcoD/?tagged=monochrome", "https://www.instagram.com/p/BYw4h3_HMYg/?tagged=monochrome", "https://www.instagram.com/p/BYw4glZDHI7/?tagged=monochrome", "https://www.instagram.com/p/BYw4gGtn4Qz/?tagged=monochrome", "https://www.instagram.com/p/BYw4f7tjVUl/?tagged=monochrome", "https://www.instagram.com/p/BYw4fnhA3Ty/?tagged=monochrome", "https://www.instagram.com/p/BYw4eU1BWuQ/?tagged=monochrome", "https://www.instagram.com/p/BYw4Zu6g9Dh/?tagged=monochrome", "https://www.instagram.com/p/BYw4Y5un02b/?tagged=monochrome", "https://www.instagram.com/p/BYw4YcvgMpK/?tagged=monochrome", "https://www.instagram.com/p/BYw4XVRgsRD/?tagged=monochrome", "https://www.instagram.com/p/BYw4WqrDlc0/?tagged=monochrome", "https://www.instagram.com/p/BYw4V5gj22g/?tagged=monochrome", "https://www.instagram.com/p/BYw4VLKn6vF/?tagged=monochrome", "https://www.instagram.com/p/BYw4U-WnS3z/?tagged=monochrome", "https://www.instagram.com/p/BYw4T4chWT7/?tagged=monochrome", "https://www.instagram.com/p/BYw4SnVgJx5/?tagged=monochrome", "https://www.instagram.com/p/BYw4ShgnsRH/?tagged=monochrome", "https://www.instagram.com/p/BYw4LF7jekc/?tagged=monochrome", "https://www.instagram.com/p/BYw4F9Ih82e/?tagged=monochrome", "https://www.instagram.com/p/BYw4EufDI24/?tagged=monochrome", "https://www.instagram.com/p/BYw4DpyFcOZ/?tagged=monochrome", "https://www.instagram.com/p/BYw3_tjjwdm/?tagged=monochrome", "https://www.instagram.com/p/BYw38MCAqch/?tagged=monochrome", "https://www.instagram.com/p/BYw37s3jXvg/?tagged=monochrome", "https://www.instagram.com/p/BYw37i6Fiuc/?tagged=monochrome", "https://www.instagram.com/p/BYw362YBU4O/?tagged=monochrome", "https://www.instagram.com/p/BYw36PwB_5N/?tagged=monochrome", "https://www.instagram.com/p/BYw35ttAR82/?tagged=monochrome", "https://www.instagram.com/p/BYw34wzH4-c/?tagged=monochrome", "https://www.instagram.com/p/BYw325uHfoG/?tagged=monochrome", "https://www.instagram.com/p/BYw32o9BZfk/?tagged=monochrome", "https://www.instagram.com/p/BYw32LlA6YB/?tagged=monochrome", "https://www.instagram.com/p/BYw3zzInG_I/?tagged=monochrome", "https://www.instagram.com/p/BYw3yYVg_7F/?tagged=monochrome", "https://www.instagram.com/p/BYw3xSXlnVR/?tagged=monochrome", "https://www.instagram.com/p/BYw3xLnB04n/?tagged=monochrome", "https://www.instagram.com/p/BYw3uphjWKg/?tagged=monochrome", "https://www.instagram.com/p/BYw3txMjHJ2/?tagged=monochrome", "https://www.instagram.com/p/BYw3tDiFlUr/?tagged=monochrome", "https://www.instagram.com/p/BYw3szDhuNN/?tagged=monochrome", "https://www.instagram.com/p/BYw3sWTBXOm/?tagged=monochrome", "https://www.instagram.com/p/BYw3rtQl14L/?tagged=monochrome", "https://www.instagram.com/p/BYw3qqvl0nW/?tagged=monochrome", "https://www.instagram.com/p/BYw3lQkBMIf/?tagged=monochrome", "https://www.instagram.com/p/BYw3iNSAdYU/?tagged=monochrome", "https://www.instagram.com/p/BYw3grDn2pH/?tagged=monochrome", "https://www.instagram.com/p/BYw3ghjgEag/?tagged=monochrome", "https://www.instagram.com/p/BYw3erDgpYO/?tagged=monochrome", "https://www.instagram.com/p/BYw3eG9hiDZ/?tagged=monochrome", "https://www.instagram.com/p/BYw3dmpDD7D/?tagged=monochrome", "https://www.instagram.com/p/BYw3cCBDm9u/?tagged=monochrome", "https://www.instagram.com/p/BYw3b1QHbrP/?tagged=monochrome", "https://www.instagram.com/p/BYw3ZMngLTY/?tagged=monochrome", "https://www.instagram.com/p/BYw3Y_jFvNk/?tagged=monochrome", "https://www.instagram.com/p/BYw3Y0glXgh/?tagged=monochrome", "https://www.instagram.com/p/BYw3YvNhR-b/?tagged=monochrome", "https://www.instagram.com/p/BYw3YpBAJ3x/?tagged=monochrome", "https://www.instagram.com/p/BYw3YKAgiGO/?tagged=monochrome", "https://www.instagram.com/p/BYw3YIvh-eg/?tagged=monochrome", "https://www.instagram.com/p/BYw3W_knge8/?tagged=monochrome", "https://www.instagram.com/p/BYw3WbRn8CF/?tagged=monochrome", "https://www.instagram.com/p/BYw3V29gl2m/?tagged=monochrome", "https://www.instagram.com/p/BYw3VmthZZI/?tagged=monochrome", "https://www.instagram.com/p/BYw3UNHlBQy/?tagged=monochrome", "https://www.instagram.com/p/BYw3TzQDF57/?tagged=monochrome", "https://www.instagram.com/p/BYw3R04nnKj/?tagged=monochrome", "https://www.instagram.com/p/BYw3RmnBA2x/?tagged=monochrome", "https://www.instagram.com/p/BYw3RkuDg5D/?tagged=monochrome", "https://www.instagram.com/p/BYw3RdpHHqo/?tagged=monochrome", "https://www.instagram.com/p/BYw3PxQlARQ/?tagged=monochrome", "https://www.instagram.com/p/BYw3OCrgyra/?tagged=monochrome", "https://www.instagram.com/p/BYw3N1DDvyX/?tagged=monochrome", "https://www.instagram.com/p/BYw3M1RnkAF/?tagged=monochrome", "https://www.instagram.com/p/BYw3L9hHcdU/?tagged=monochrome", "https://www.instagram.com/p/BYw3Lnzh0pj/?tagged=monochrome", "https://www.instagram.com/p/BYw3I1VHcoF/?tagged=monochrome", "https://www.instagram.com/p/BYw3FKnj1wZ/?tagged=monochrome", "https://www.instagram.com/p/BYw3E51nwaC/?tagged=monochrome", "https://www.instagram.com/p/BYw3DFWhT-T/?tagged=monochrome", "https://www.instagram.com/p/BYw293yhdX-/?tagged=monochrome", "https://www.instagram.com/p/BYw28WCnLh2/?tagged=monochrome", "https://www.instagram.com/p/BYw27gRBvwi/?tagged=monochrome", "https://www.instagram.com/p/BYw25PogmjI/?tagged=monochrome", "https://www.instagram.com/p/BYw25AfgUXC/?tagged=monochrome", "https://www.instagram.com/p/BYw24qwDQt9/?tagged=monochrome", "https://www.instagram.com/p/BYw24GCFNvK/?tagged=monochrome", "https://www.instagram.com/p/BYw23e0Aof8/?tagged=monochrome"]

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

    print("user: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))
    likes.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    print("comments: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    comments.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    print("likes: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    pictures.append(str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))

    print("url: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))

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

    listData.append("https://www.instagram.com/"+users[num]) #listにユーザー名、画像url、いいね数、コメント数を追加
    listData.append(pictures[num])
    listData.append(likes[num])
    listData.append(comments[num])
    list2.append(listData) #新たなリストにlistDataの1行を1つの要素として追加

    with open('instag.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(tag) #ファイルにtagとリストを追加
        writer.writerows(list2)
