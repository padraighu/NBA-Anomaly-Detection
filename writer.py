import csv 
from os import chdir

path = "C:\Users\Administrator\Desktop\\anomaly detection\csv files"
testpath = "C:\Users\Administrator\Desktop\\anomaly detection\\test"
chdir(path)

def register():
	csv.register_dialect("custom", "excel", lineterminator="\n")

def write_new_csv(logs):
	"""
	Write a csv file to store the stats of a player 
	after scraping. 
	"""
	register()
	# Start recording logs from the beginning of the season.
	logs.reverse()
	file_name = logs[0].name + ".csv"
	with open(file_name, "w") as csv_file:
		csv_writer = csv.writer(csv_file, dialect="custom")
		csv_writer.writerow(["DATE", "GAME", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA",
							"3P%", "FTM", "FTA", "FT%", "REB", "AST", "BLK", "STL", "PF", "TO"])
		for log in logs:
			# Prevent rows of stats that have MIN as 0, 
			# meaning the player is DNP or Inactive. 
			# They are irrelevant to our analysis.
			if log.minutes != "0":
				csv_writer.writerow([log.date, log.team + " " + log.opponent, log.minutes, log.pts,
									log.fgm, log.fga, log.fgp, log.tpm, log.tpa, log.tpp, log.ftm,
									log.fta, log.ftp, log.reb, log.ast, log.blk, log.stl, log.foul,
									log.turnover])
	csv_file.close()

def write_old_csv(log):
	"""
	Update a csv file by writing the latest game log. 
	"""
	register()
	file_name = log.name + ".csv"
	with open(file_name, "a") as csv_file:
		csv_writer = csv.writer(csv_file, dialect="custom")
		if log.minutes != "0":
			csv_writer.writerow([log.date, log.team + " " + log.opponent, log.minutes, log.pts,
									log.fgm, log.fga, log.fgp, log.tpm, log.tpa, log.tpp, log.ftm,
									log.fta, log.ftp, log.reb, log.ast, log.blk, log.stl, log.foul,
									log.turnover])
	csv_file.close()