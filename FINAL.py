import numpy as np
from sklearn.cluster import KMeans
import csv
from colorfullcheck import aveLab2,aveLab
from LabDis import labdis

filename = "instagSea2.csv"
imagename = "new.jpg"
k = 2
def final(filename,imagename):
	csvdata = []

	with open(filename,'r') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		data = [v for v in csv_reader]
		for row in data:
			csvdata.append([row[2],row[3],row[4]])
			csvdata.append([row[5],row[6],row[7]])

	features = np.array(csvdata)
	kmeans_model = KMeans(n_clusters=2).fit(features)
	lab = aveLab2(imagename,k)

	disa =  labdis(kmeans_model.cluster_centers_[0],lab[0])
	disb =  labdis(kmeans_model.cluster_centers_[0],lab[1])
	disc =  labdis(kmeans_model.cluster_centers_[1],lab[0])
	disd = labdis(kmeans_model.cluster_centers_[1],lab[1])

	dis1 = disa
	dis2 = disc

	if disb < disa:
		dis1 = disb
	if disd < disc:
		dis2 = disd

	av = (dis1+dis2)/2.0
	howmany = aveLab(imagename,7)

	if av <= 33.0:
		if howmany <= 40:
			print("bad!!:もっとカラフルにしよう")
		if ((howmany > 40) and (howmany <= 70 )):
			print("good!!:もっとカラフルになれば完璧！")
		if howmany > 70:
			print("very good!!:おめでとう！！")
	if ((av > 33) and (av <= 66)):
		if howmany <= 40:
			print("bad!!:もっとカラフルにしよう")
		if ((howmany > 40) and (howmany <= 70 )):
			print("soso!!:もっとカラフルに！")
		if howmany > 70:
			print("good!!:おめでとう！！もっとカテゴリにあった写真を撮ろう！！")
	if av > 66:
		if howmany <= 40:
			print("toobad!!:逆にすごい！！")
		if ((howmany > 40) and (howmany <= 70 )):
			print("bad!!:カテゴリにあった写真を撮ろう！")
		if howmany > 70:
			print("bad!!:カテゴリにあった写真を撮ろう！！")