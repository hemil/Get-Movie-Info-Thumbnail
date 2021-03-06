'''

Download info about all the movies in the folder and save it in the info.txt
Download the thumbnail and name it as folder.jpg if it doesnt exist. 

'''
import imdb
import os
import urllib

#Get the subdirectories
def GetSubdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

#Download the thumbnail if it doesn't already exist
def GetThumbnail(movie,name):
	FileName = name+"/folder.jpg"
	if not os.path.isfile(FileName):
		urllib.urlretrieve(movie['cover url'], FileName)
		print name.split("/")[-1] + "'s thumbnail downloaded"

print "Start..."

#Enter the folder
root = "/media/mithrandir/Entertainment/Theatre/MKOM"
movies = GetSubdirectories(root)

# Create the object that will be used to access the IMDb's database.
portal = imdb.IMDb()

for name in movies:
	print name
	f = open(os.path.join(root,name)+"/info.txt",'w')
	
	# Search for a movie (get a list of Movie objects).
	result = portal.search_movie(name)
	'''
	# Print the long imdb canonical title and movieID of the results.
	for item in result:
	   print item['long imdb canonical title'], item.movieID
	'''
	
	# Retrieves default information for the first result (a Movie object).
	movie = result[0]
	portal.update(movie)

	GetThumbnail(movie,os.path.join(root,name))

	# Print some information.
	genres = ""
	for each in movie['genres']:
		genres = genres + each + " , " 
	directors = ""
	for each in movie['director']:
		directors = directors + str(each) + " , " 
	writers = ""
	for each in movie['writer']:
		writers = writers+ str(each) + " , " 
	cast = "\n"
	for each in movie['cast']:
		cast = cast + str(each) + "\n"

	f.write(movie['long imdb title'] + "\n" + portal.get_imdbURL(movie)) 
	f.write("\n\nLength : " + movie['runtime'][0] + " mins") 
	f.write("\n\nRating : " + str(movie['rating'])) 
	f.write("\n\nGenres : " + genres)
	f.write("\n\nDirector : " + directors) 
	f.write("\n\nWriter : " + writers)
	f.write("\nPlot : " + movie['plot'][0])
	f.write("\n\nCast : " + cast + "")
