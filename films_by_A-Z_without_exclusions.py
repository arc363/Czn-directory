from bs4 import BeautifulSoup
import csv

# Read HTML content from file
with open('curzon_by_A-Z.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifuSoup library to 
soup = BeautifulSoup(html_content, 'html.parser')

# Reads the Curzon HTML doc and gets all pieces of text from it
def get_films_text():
  string = soup.get_text("\n", strip=True)
  print("Films HTML text processed")
  return string


films_text = get_films_text()
# print(films_text)




# Split the films_text and filter out excluded texts
films_list = []
films_list = [line for line in films_text.split("\n")
              if not 'View All' in line]

films_list = films_list[9:-21]

# Debug check
print(films_list)
# print(films_list[0:9])
# print(films_list[-21:-1])

# Create a dictionary containing only film names and lengths
films_dict = {}

def create_film_dict():
  for i in range(0, len(films_list) - 1, 2):
    film_title = films_list[i]
    duration = films_list[i + 1]
    films_dict[film_title] = duration
  print("Film dictionary created")


# create_film_dict()

"""
def print_summary():
  # Print header
  print(f"{'\nIndex':<6} {'Film title':<60} {'Length'}")
  print('-' * 80)

  # Print films and durations
  for index, (film_title, duration) in enumerate(films_dict.items(), start=1):
      print(f"{index:<6} {film_title:<60} {duration}")

  # Optional: Print a line to separate the output
  print('-' * 80)

 

print_summary()


# Create csv file from dictionary
with open('curzon_films.csv', 'w') as f:
  w = csv.DictWriter(f, films_dict.keys())
  w.writeheader()
  w.writerow(films_dict)


# Create txt file from dictionary
with open('curzon_films.txt', 'w') as f:
  
  
"""