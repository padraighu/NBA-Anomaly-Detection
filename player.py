class Log:
	def __init__(self, name=None, date=None, team=None, opponent=None, minutes=0, fgm=0, fga=0, fgp=0,
				tpm=0, tpa=0, tpp=0, ftm=0, fta=0, ftp=0, reb=0, ast=0, blk=0, 
				stl=0, foul=0, turnover=0, pts=0):
		self.name = name 
		self.date = date
		self.team = team
		self.opponent = opponent
		self.minutes = minutes
		self.fgm = fgm
		self.fga = fga
		self.fgp = fgp
		self.tpm = tpm
		self.tpa = tpa 
		self.tpp = tpp
		self.ftm = ftm
		self.fta = fta
		self.ftp = ftp 
		self.reb = reb
		self.ast = ast
		self.blk = blk
		self.stl = stl 
		self.foul = foul
		self.turnover = turnover
		self.pts = pts

	def __str__(self):
		string = "Player: " + self.name + "\n" + "Game date: " + self.date + "\n"
		string += "Team: " + self.team + "\n" + "Opponent: " + self.opponent + "\n" + "Min: " + self.minutes + "\n" + "FGM: " + self.fgm + "\n" + "FGA: " + self.fga + "\n"
		string += "FG%: " + self.fgp + "\n" + "3PM: " + self.tpm + "\n" + "3PA: " + self.tpa + "\n" + "3P%: " + self.tpp + "\n" + "FTM: " + self.ftm + "\n" 
		string += "FTA: " + self.fta + "\n" + "FT%: " + self.ftp + "\n" + "REB: " + self.reb + "\n" + "AST: " + self.ast + "\n" + "BLK: " + self.blk + "\n"
		string += "STL: " + self.stl + "\n" + "PF: " + self.foul + "\n" + "TO: " + self.turnover + "\n" + "PTS: " + self.pts + "\n"
		return string 