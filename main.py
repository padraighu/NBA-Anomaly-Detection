import scraper 
import writer 

def update_old(player_urls):
	for player_url in player_urls:
		log = scraper.update_game_logs(player_url)
		if log != None:
			writer.write_old_csv(log)

def create_new(player_urls):
	for player_url in player_urls:
		logs = scraper.get_previous_game_logs(player_url)
		if logs != None:
			writer.write_new_csv(logs)

if __name__ == "__main__":
	print "getting urls..."
	player_urls = scraper.get_players_url()
	#create_new(player_urls)
	update_old(player_urls)