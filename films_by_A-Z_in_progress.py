from bs4 import BeautifulSoup

# Read HTML content from file
with open('curzon_html2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifuSoup library 
soup = BeautifulSoup(html_content, 'html.parser')

# Reads the Curzon HTML doc and gets all pieces of text from it
def get_films_text():
  """Extracts all text from the HTML and returns it as a string."""
  films_text = soup.get_text("\n", strip=True)
  print("Films HTML text processed")
  return films_text


films_text = get_films_text()
# print(films_text)


# List of texts to exclude
texts_to_exclude = ['Curzon HTML', '0-9', 'Watch 0-9 Collection of Films Online - Curzon Home Cinema',
                    'Cinemas', 'Home Cinema', 'Films', 'Seasons', 'Discover', 'Journal', 'Membership',
                    'Curzon Home Cinema Presents...', 'Get help', 'Help', 'Terms & Conditions', 
                    'Privacy Policy', 'My account', 'Manage account', 'Follow Us', 'Our newsletter', 
                    'Bafta winner 2017', 'Outstanding Contribution', 'to British Cinema', 'British Cinema', 
                    'Curzon ©', 'All Rights Reserved', 'Terms & Conditions', 'Privacy Policy', 'View All']


# Print some debug information
print("Debug Information:")
print("HTML Content Length:", len(html_content))
print("Films Text Length:", len(films_text))

"""

# Split the films_text and filter out excluded texts
# films_list = []
films_list = [line for line in films_text.split("\n") 
              if not any(exclude_text in line for exclude_text in texts_to_exclude)
              or ('to' == line.strip().lower() and len(line.split()) > 1)
              or '2021 Oscar Nominated Short Films' in line
              or 'Jean Vigo: Three Films' in line
              or 'The Short Films Of Claire Oakley' in line
              or 'The Seasons In Quincy' in line]


# Print debug information
print("Films List Length:", len(films_list))

# Print some films from the beginning and end
print("First 5 Films:", films_list[:5])
print("Last 5 Films:", films_list[-5:])

# Create a dictionary containing only film names and lengths
films_dict = {}


def create_film_dict():
  for i in range(0, len(films_list) - 1, 2):
    film_title = films_list[i]
    duration = films_list[i + 1]
    films_dict[film_title] = duration
  print("Film dictionary created")


def create_film_dict():
    # Creates a dictionary containing film names and lengths.
    for film_title, duration in zip(films_list[::2], films_list[1::2]):
        # Exclude single-letter film titles
        if len(film_title.strip()) > 1:
            films_dict[film_title] = duration
        else:
            print(f"Excluded (Dictionary Creation): {film_title}")


# Print some debug information
print("Before Create Film Dict - Films Dictionary Length:", len(films_dict))

# Create the film dictionary
create_film_dict()


# Print some debug information after creating the dictionary
print("After Create Film Dict - Films Dictionary Length:", len(films_dict))

# Print some films from the beginning and end of the dictionary
print("First 5 Films in Dictionary:", list(films_dict.items())[:5])
print("Last 5 Films in Dictionary:", list(films_dict.items())[-5:])


def print_summary():
  # Print header
  print(f"{'\nIndex':<6} {'Film title':<60} {'Length'}")
  print('-' * 80)

  # Print films and durations
  for index, (film_title, duration) in enumerate(films_dict.items(), start=1):
      print(f"{index:<6} {film_title:<60} {duration}")

  # Optional: Print a line to separate the output
  print('-' * 80)

 
# print_summary()
"""

films_list = [line for line in films_text.split("\n")
            if not any(exclude_text in line for exclude_text in texts_to_exclude)
            or ('to' == line.strip().lower() 
            and len(line.split()) > 1)
            or '2021 Oscar Nominated Short Films' in line
            or 'Jean Vigo: Three Films' in line
            or 'The Short Films Of Claire Oakley' in line
            or 'The Seasons In Quincy' in line]

films_dict = {}

def create_film_dict():
    """Creates a dictionary containing film names and lengths."""
    for i in range(0, len(films_list) - 1, 2):
        film_title = films_list[i]
        duration = films_list[i + 1]
        films_dict[i] = {'title': film_title, 'duration': duration}
    print("Film dictionary created")
    

def print_summary():
    """Prints a summary of films and their durations."""
    print(f"{'\nIndex':<10} {'\nFilm title':<60} {'Length'}")
    print('-' * 80)

    for index, item in enumerate(films_dict.items(), start=1):
        # print(f"{index:<10}", film)
        film = item[1]
        print(f"{index:<10} {item[0]:<10} {film["title"]:<60} {film["duration"]}")

    print('-' * 80)

create_film_dict()
# print(films_dict)
print_summary()
