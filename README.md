# shell_csv_manipulation

The csv_cuts.py is a Python 3 script that is used to 
1) look at .CSV data files with columns of numbers
2) eliminate certains rows in those data based on certain criteria in the data
3) output new .CSV files without the eliminated rows

There are endless possibilities as to how this could be modified. In the example I have provided, I include name#.csv files, and I have 3 columns: AGE, DIST, and CertID. I say that I only want rows where the age is greater than a certain number, and the distance is greater than a certain number. 

The bash script "cut_it_up.sh" is a while loop to run the Python script through the series of name#.csv files.
