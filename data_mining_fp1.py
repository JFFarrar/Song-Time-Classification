import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def main():

	parser = open("parodgers99.csv","r")
	songs = parser.readlines()
	parser.close()
	idfile = open("ids.csv","a")
	prev_artist = ""
	prev_song = ""
	original_songs = open("paro.csv","r")
	orig = original_songs.readlines()
	client_credentials_manager = SpotifyClientCredentials(client_id = "94de76eb590f4dd99204ed1fc4de106a", client_secret = "82567ef281a640bf8fc5421d85840a71")
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	features = []
	for num, line in enumerate(songs):
		temp = line.split(",")
		temp2 = orig[num].split(",")
		if(prev_artist == temp[0] and prev_song == temp[2]):
			idfile.write(str(features[0].get("energy"))+" ")
			idfile.write(str(features[0].get("liveness"))+" ")
			idfile.write(str(features[0].get("tempo"))+" ")
			idfile.write(str(features[0].get("speechiness"))+" ")
			idfile.write(str(features[0].get("acousticness"))+" ")
			idfile.write(str(features[0].get("instrumentalness"))+" ")
			idfile.write(str(features[0].get("time_signature"))+" ")
			idfile.write(str(features[0].get("danceability"))+" ")
			idfile.write(str(features[0].get("key"))+" ")
			idfile.write(str(features[0].get("loudness"))+" ")
			idfile.write(str(features[0].get("valence"))+" ")
			idfile.write(str(features[0].get("liveness"))+" ")
			idfile.write(str(num+1)+" ")
			for i in temp2:
				idfile.write(str(i)+" ")
			idfile.write("\n")
			idfile.flush()
			continue
		trackid = sp.search(q='artist:' + temp[0] + ' track:' + temp[2], limit=1, type='track')
		#If the search function fails us, just forget about it.
		try:
			id = trackid['tracks']['items'][0]['id']
		except:
			continue
		features = sp.audio_features([id])
		idfile.write(str(features[0].get("energy"))+" ")
		idfile.write(str(features[0].get("liveness"))+" ")
		idfile.write(str(features[0].get("tempo"))+" ")
		idfile.write(str(features[0].get("speechiness"))+" ")
		idfile.write(str(features[0].get("acousticness"))+" ")
		idfile.write(str(features[0].get("instrumentalness"))+" ")
		idfile.write(str(features[0].get("time_signature"))+" ")
		idfile.write(str(features[0].get("danceability"))+" ")
		idfile.write(str(features[0].get("key"))+" ")
		idfile.write(str(features[0].get("loudness"))+" ")
		idfile.write(str(features[0].get("valence"))+" ")
		idfile.write(str(features[0].get("liveness"))+" ")
		idfile.write(str(num+1)+" ")
		for i in temp2:
			idfile.write(str(i)+" ")
		idfile.write("\n")
		idfile.flush()
		prev_artist = temp[0]
		prev_song = temp[2]
		
main()