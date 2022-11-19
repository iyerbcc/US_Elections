For every national election since 1964, the US Census Bureau has collected data on the characteristics of American voters.
In particular, detailed data on Voting and Registration since 1990 by age, sex, race, and ethnicity for states are available on the US Census Bureau website. (https://www.census.gov/data.html)

Project Question: Predict the Population, Voting, Registration numbers for the years 2022 to 2030 elections by sex, race, and Hispanic origin for states and the United States.


Step 1: Collect, clean and transform data to a consistent form. 
Over the past 30 years formats and tabulations have changed. For instance, files from the 1990s are either in text, image, or pdf formats while more recent data are in excel formats of varying kinds. 

Raw data is kept in the folder: raw_elections_data
Several rounds of cleaning has been undertaken using Pandas and PySpark to obtain cleaner versions of data. They are available in order,  clean_election_data, clean2_election_data, clean3_election_data.
Final versions are saved in the folder elections and the sub-folders within. 


Step 2: Linear Regression has been used to predict Population, Voting, Registration numbers for each state, by race, sex, and Hispanic origin.  The final tables are kept in the folders: PopulationWithPredictions, VotingWithPredictions, and RegistrationWithPredictions. 

Step 3: We have built an interactive website in Flask which will incorporate the users’ selections in queries it sends to the RDS backend. The results are displayed in tabular form as well as visualizations such as Line plots and Bar graphs. 

Three Jupyter notebooks have been used for the following:
Scratch-work: This notebook has been used to test and build our main clean codes.
rawToclean2 : This notebook has been used to convert our raw data through various stages of cleaning until the folder clean2.
threeTables : This notebook has been used to build clean3 data folder, and then implement Linear Regression to finally obtain the database elections. 


Flask_Elections : This folder has the entire code to build the interactive website in Flask to display our data with predictions. 

YouTube Link: https://youtu.be/hd1m00OaO50
