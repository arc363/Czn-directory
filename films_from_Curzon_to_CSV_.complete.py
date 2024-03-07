from bs4 import BeautifulSoup
import csv

# Read HTML content from file
with open('curzon_by_A-Z.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifulSoup library to process HTML
soup = BeautifulSoup(html_content, 'html.parser')


def get_films_text():
    """Read the Curzon HTML doc and get all text strings from it"""
    string = soup.get_text("\n", strip=True)
    print(" ✅ Curzon HTML doc processed")
    return string


films_text = get_films_text()
# print("films_text", films_text)


films_list = []


def convert_str_to_list(p_films_text):
    """Split films_text and filter out excluded strings"""
    films_list = [line for line in p_films_text.split("\n")
                  if not ('View All' in line)]
    films_list = films_list[9:-21]
    return films_list

films_list = convert_str_to_list(films_text)


def create_film_dict(p_films_list):
    """Create dictionary from list of films, containing titles and durations"""
    films_dict = {}
  
    # Iterate through list in steps of two
    for i in range(0, len(p_films_list), 2):
      film_title = p_films_list[i]
      duration = p_films_list[i + 1]

      # Add the title and duration to the dictionary
      films_dict[film_title] = duration
    print(" ✅ Film dictionary created")

    return films_dict


# Create the dictionary
films_dict = create_film_dict(films_list)
# print(films_dict)

# Specify the CSV file name
csv_file = 'films4.csv'


def convert_dict_to_CSV(films_dict):
    """Write the dictionary to a CSV file so it can be opened in Excel"""
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
      # Create a CSV writer object
      csv_writer = csv.writer(file)
      
      # Write the header (keys of the dictionary)
      csv_writer.writerow(['Title', 'Duration'])

      # Write the data (values of the dictionary)
      for title, duration in films_dict.items():
        csv_writer.writerow([title, duration])

    print(f" ✅ Film dictionary written to {csv_file}")
    print()


convert_dict_to_CSV(films_dict)
