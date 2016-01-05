# NBA-Anomaly-Detection
Python and R scripts that automatically detect statistical anomalies within the latest game logs of individual players 

What it does:
1. Scrape all available past game logs of every NBA player in the current season from ESPN. 
2. Store them as individual csv files. 
3. Scrape latest game logs and update local csv files accordingly.
4. Detect any statistical anomalies in the latest finished games in the updated csv files. 

To run the scripts, you need to have Python 2.7 and R installed. I also recommend installing RStudio as IDE for R.
You need to install two additional Python packages: bs4 and urllib2. 

How to:
1. Download the zip file containing all scripts and unzip the directory to your computer.
2. Create two new directories, "csv files" and "logs" within the local directory to store csv files and daily anomaly logs respectively later.
3. Open helper.py, change PATH and TEST_PATH (an optional directory for you to test codes) according to your own settings; do the same with csv_path and log_path in detector.R.
4. Open the command line, change the working directory to the directory and enter "python main.py", which runs the Python codes in main.py (Or do the equivalent in Linux/OSX environments). 
5. Open RStudio, and call function source(), the single parameter being the path to detector.R with quotation marks, in the console, which allows you to call functions in detector.R.
6. Call function detect_all(), which will detect and print out any anomalies, and store the results in a txt file in "logs".
7. Take a look at the logs to discover the anomalies of the day! 