import numpy as np
from sklearn.cluster import KMeans
import csv
from colorfullcheck import aveLab2,aveLab
from LabDis import labdis

def final(number,imagename):
	if number == 0:
		filename = "instagCat2.csv"
	if number == 1:
		filename = "instagSea2.csv"
	if number == 2:
		filename = "instagFlo2.csv"
	if number == 3:
		filename = "instagStb2.csv"
	if number == 4:
		filename = "instagSky2.csv"
	if number == 5:
		filename = "instagOmu2.csv"
	
	csvdata = []

	with open(filename,'r') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		data = [v for v in csv_reader]
		for row in data:
			csvdata.append([row[2],row[3],row[4]])
			csvdata.append([row[5],row[6],row[7]])

	features = np.array(csvdata)
	kmeans_model = KMeans(n_clusters=2).fit(features)
	
	print(kmeans_model.cluster_centers_)
	
	lab = aveLab2(imagename,2)
	
	print(lab)

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

	if av <= 24.0:
		if howmany <= 30:
			return("bad!!:もっとカラフルにしよう")
		if ((howmany > 30) and (howmany <= 60 )):
			return("good!!:もっとカラフルになれば完璧！")
		if howmany > 60:
			return("very good!!:おめでとう！！")
	if ((av > 24.0) and (av <= 35)):
		if howmany <= 30:
			return("bad!!:もっとカラフルにしよう")
		if ((howmany > 30) and (howmany <= 60 )):
			return("soso!!:もっとカラフルに！")
		if howmany > 60:
			return("good!!:おめでとう！！もっとカテゴリにあった写真を撮ろう！！")
	if av > 35:
		if howmany <= 30:
			return("toobad!!:逆にすごい！！")
		if ((howmany > 30) and (howmany <= 60 )):
			return("bad!!:カテゴリにあった写真を撮ろう！")
		if howmany > 60:
			return("bad!!:カテゴリにあった写真を撮ろう！！")
if __name__ == '__main__':
	final("instagOmu2.csv","new.jpg")