csv_path <- "C:\\Users\\Administrator\\Desktop\\anomaly detection\\csv files"
log_path <- "C:\\Users\\Administrator\\Desktop\\anomaly detection\\logs\\"

valid_csv <- function(csv_file){
  valid <- TRUE 
  if(length(csv_file[, "PTS"]) == 0){
    valid <- FALSE
  }
  ## Check if the latest log is on "today".
  ## Difference is 1 because of the time difference. 
  else{
    latest_date <- as.Date(rev(csv_file[, 1])[1])
    today_date <- Sys.Date()
    if(today_date - latest_date != 1){
      valid <- FALSE
    }
  }
  return(valid)
}

get_info <- function(file_name, csv_file, col, category){
  name <- strsplit(file_name, ".csv")[1]
  stat_type <- as.character(col(csv_file, T)[1, col])
  stat <- as.character(category[1])
  game <- as.character(rev(csv_file[, "GAME"])[1])
  return(c(name, stat_type, stat, game))
}

detect <- function(file_name){
  to_write <- paste(log_path,
               as.character(Sys.Date() - 1), ".txt", sep="")
  ## Detect statistical anamolies with a given csv file.
  csv_file <- read.csv(file_name)
  ## Columns that need to be inspected. 
  cols <- c(4:19)
  if(valid_csv(csv_file)){
    for(col in cols){
      category <- rev(csv_file[,col])
      ## We want the latest log to be on the first row.
      category_summary <- summary(category)
      q3 <- as.double(category_summary["3rd Qu."])
      q1 <- as.double(category_summary["1st Qu."])
      iqr <- q3 - q1
      if(category[1] < q1 - 1.5 * iqr){
        info <- get_info(file_name, csv_file, col, category)
        name <- info[1]
        stat_type <- info[2]
        stat <- info[3]
        game <- info[4]
        message <- sprintf("In %s, %s underperformed his average self by logging %s in %s.",
                           game, name, stat, stat_type)
        print(message)
        write(message, to_write, append=T)
        ## boxplot(category)
      }
      else if(category[1] > q3 + 1.5 * iqr){
        info <- get_info(file_name, csv_file, col, category)
        name <- info[1]
        stat_type <- info[2]
        stat <- info[3]
        game <- info[4]
        message <- sprintf("In %s, %s outperformed his average self by logging %s in %s.",
                           game, name, stat, stat_type)
        print(message)
        write(message, to_write, append=T)
        ## boxplot(category)
      }
    }
  }
}

detect_all <- function(){
  directory <- csv_path
  setwd(directory)
  file_lst <- list.files(path=directory)
  for(file_name in file_lst){
    detect(file_name)
  }
}
