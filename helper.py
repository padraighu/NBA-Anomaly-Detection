from os import listdir

def get_date(str_texts):
	"""
	Get the game date with the given string.
	"""
	begin_idx = 8
	for idx in range(len(str_texts)):
		if str_texts[idx] == "/":
			if str_texts[idx-1] == "<":
				end_idx = idx-1
			else: 
				div_idx = idx 
	month = str_texts[begin_idx:div_idx]
	day = str_texts[div_idx+1:end_idx]
	if int(month) <= 12 and int(month) >= 10:
		year = "2015"
	else:
		year = "2016"
	return year + "-" + month + "-" + day

def get_team(soup):
	"""
	Get the abbreviated name of the player's team 
	given a soup object.
	"""
	ABBREV = {"Boston Celtics": "BOS", "Brooklyn Nets": "BKN", "New York Knicks": "NY", "Philadelphia 76ers": "PHI", "Toronto Raptors": "TOR",
				"Chicago Bulls": "CHI", "Cleveland Cavaliers": "CLE", "Detroit Pistons": "DET", "Indiana Pacers": "IND", "Milwaukee Bucks": "MIL",
				"Atlanta Hawks": "ATL", "Charlotte Hornets": "CHA", "Miami Heat": "MIA", "Orlando Magic": "ORL", "Washington Wizards": "WSH",
				"Golden State Warriors": "GS", "Los Angeles Clippers": "LAC", "Los Angeles Lakers": "LAL", "Phoenix Suns": "PHX", "Sacramento Kings": "SAC",
				"Dallas Mavericks": "DAL", "Houston Rockets": "HOU", "Memphis Grizzlies": "MEM", "New Orleans Pelicans": "NO", "San Antonio Spurs": "SA",
				"Denver Nuggets": "DEN", "Minnesota Timberwolves": "MIN", "Oklahoma City Thunder": "OKC", "Portland Trail Blazers": "POR", "Utah Jazz": "UTAH"}
	team = soup.find("title").text
	first = True 
	for idx in range(len(team)):
		if team[idx] == "-":
			# Prevent errors when players' names have dash in it.
			if team[idx-12:idx-1] == "Performance" or team[idx+2:idx+6] == "ESPN":
				if first:
					begin_idx = idx + 2
					first = False 
				else:
					end_idx = idx - 1
	return ABBREV[team[begin_idx:end_idx]]

def validate_texts(str_texts):
	"""
	Validate given texts in order to clean the data based on dates.
	"""
	DAY_LIST = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	if str_texts[4:7] not in DAY_LIST:
		return False 
	for idx in range(len(str_texts)):
		if str_texts[idx] == "/" and str_texts[idx+1] != "t":
			div_idx = idx
	# We don't want preseason stats.
	if str_texts[div_idx-2:div_idx] == "10":
		# Dates that have single digits are definitely smaller than 27.
		if str_texts[div_idx+2] == "<":
			return False 
		elif int(str_texts[div_idx+1:div_idx+3]) < 27:
			return False
	return True 
 
def concatenate(str1, str2):
 	"""
 	Properly concatenate two strings.
 	"""
 	if str1[0] == "v":
 		return str1 + " " + str2
 	elif str1[0] == "@":
 		return str1 + str2

def format_data(raw_texts):
	result = []
	opponent = concatenate(raw_texts[1].find(class_="game-location").text,
							raw_texts[1].find(class_="team-name").text)
	result.append(opponent)
	for tag in raw_texts[3:]:
		text = str(tag.text)
		if "-" in text:
			for idx in range(len(text)):
				if text[idx] == "-":
					div_idx = idx
			result.append(text[:div_idx])
			result.append(text[div_idx+1:])
		else: 
			result.append(text)
	return result 

def check_existing_csv():
	"""
	Check csv files that already exist in the directory. 
	Return a list of players' names so that the scraper will
	skip those players because they're already scraped. 
	"""
	path = "C:\Users\Administrator\Desktop\\anomaly detection\csv files"
	testpath = "C:\Users\Administrator\Desktop\\anomaly detection\\test"
	names = listdir(path)
	#print len(names)
	result = []
	for name in names:
		result.append(name[:-4])
	return result