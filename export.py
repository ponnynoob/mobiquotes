import csv

def leavethefirstcolumn(filename):
  with open(filename) as file, open('quotes.txt', "w") as out:
    reader = csv.reader(file ,quotechar='|')
    for row in reader:
      out.write(row[0] + "\n")

# example of using the function
leavethefirstcolumn("quotes.csv")