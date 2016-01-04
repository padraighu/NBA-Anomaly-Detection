from urllib2 import urlopen 
from bs4 import BeautifulSoup
from player import Log
from datetime import date, timedelta
import helper 

def get_teams_url():
	"""
	Get the urls to all the current teams in the NBA 
	so that we can scrape the stats of the players. 
	"""
	team_urls = []
	# To concatenate with the result urls later. 
	first_half_url = "http://espn.go.com"
	begin_url = "http://espn.go.com/nba/players"
	html_file = urlopen(begin_url)
	soup = BeautifulSoup(html_file)
	raw_texts = soup.find_all("a", style="padding-top:5px;padding-left:0px;")
	for text in raw_texts:
		team_urls.append(first_half_url + str(text.get("href")))
	return team_urls

def get_players_url():
	"""
	Get the urls to all the current players in the NBA 
	so that we can scrape the stats. 
	"""
	team_urls = get_teams_url()
	gamelog_urls = []
	for team_url in team_urls:
		begin_url = team_url
		#print begin_url
		html_file = urlopen(begin_url)
		soup = BeautifulSoup(html_file)
		# Players' urls are a little tricky because 
		# they don't have any attributes other than a.
		for candidate in soup.find_all("a"):
			candidate_url = str(candidate.get("href"))
			if candidate_url[:30] == "http://espn.go.com/nba/player/":
				gamelog_url = candidate_url[:30] + "gamelog/" + candidate_url[30:]
				gamelog_urls.append(gamelog_url)
	return gamelog_urls
	
def get_previous_game_logs(url):
	"""
	Get previous game logs of a certain player. 
	"""
	existing_names = helper.check_existing_csv()
	try:
		html_file = urlopen(url)
	except: 
		print "Game log url does not exist. Skipping this player."
		return None
	soup = BeautifulSoup(html_file)
	player_name = soup.find_all("h1")[0].text
	if player_name in existing_names:
		print "Skipping players that were scraped."
		return None
	games = soup.find_all("tr")
	team = helper.get_team(soup)
	logs = []
	for game in games:
		raw_texts = game.find_all("td")
		if helper.validate_texts(str(raw_texts[0])):
			game_date = helper.get_date(str(raw_texts[0])) 
			opponent, minutes, fgm, fga, fgp, tpm, tpa, tpp, ftm, fta, ftp, reb, ast, blk, stl, foul, turnover, pts = helper.format_data(raw_texts)
			log = Log(player_name, game_date, team, opponent, minutes, fgm, fga, fgp, tpm, tpa, tpp, 
							ftm, fta, ftp, reb, ast, blk, stl, foul, turnover, pts)
			print game_date, player_name, team
			logs.append(log)
	return logs

def update_game_logs(url):
	"""
	Update game logs of a certain player. 
	For prototype let's use Isaiah Thomas as an example. 
	"""
	# Check date to make sure because we're only getting 
	# the lateest game. 
	today_date = date.today()
	try:
		html_file = urlopen(url)
	except: 
		print "Game log url does not exist. Skipping this player.", url
		return None
	soup = BeautifulSoup(html_file)
	player_name = soup.find_all("h1")[0].text
	team = helper.get_team(soup)
	# The 6th (counting from 1) tr element in the html texts 
	# is the latest_game.
	latest_game = soup.find_all("tr")[5]
	raw_texts = latest_game.find_all("td")
	game_date_str = helper.get_date(str(raw_texts[0]))
	year, month, day = game_date_str.split("-")
	ONE_DAY = timedelta(1)
	# Transforming the scraped date into an date object. 
	game_date = date(int(year), int(month), int(day))
	# On account of me being in China which is a day ahead of US time.
	if today_date - game_date == ONE_DAY:
		opponent, minutes, fgm, fga, fgp, tpm, tpa, tpp, ftm, fta, ftp, reb, ast, blk, stl, foul, turnover, pts = helper.format_data(raw_texts)
		log = Log(player_name, game_date, team, opponent, minutes, fgm, fga, fgp, tpm, tpa, tpp, 
						ftm, fta, ftp, reb, ast, blk, stl, foul, turnover, pts)
		print game_date, player_name, team
		return log 

if __name__ == "__main__":
	#get_previous_game_logs("http://espn.go.com/nba/player/gamelog/_/id/4240/avery-bradley")
	pass 