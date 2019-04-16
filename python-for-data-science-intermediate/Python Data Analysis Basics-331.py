## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != '':
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##

ages = []
for row in moma:
    data = row[6]
    birth = row[3]
    if type(birth) == int:
        age = data - birth
    else:
        age = 0
    ages.append(age)

final_ages = []
for element in ages:
    if element > 20:
        final_age = element
    else:
        final_age = 'Unknown'
    final_ages.append(final_age)
    
 

## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen
decades = []
for element in ages:
    if element == 'Unknown':
        decade = element
    else:
        decade = str(element)
        decade = decade[:-1]
        decade = decade + '0s'
    decades.append(decade)
    
    

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for ele in decades:
    if ele in decade_frequency:
        decade_frequency[ele] += 1
    else:
        decade_frequency[ele] = 1
        

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
template = "{name}'s birth year is {num}"
print(template.format(name = artist, num = birth_year))


## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist in artist_freq:
        artist_freq[artist] += 1
    else:
        artist_freq[artist] = 1
        

## 7. Creating an Artist Summary Function ##

def artist_summary(artist_name):
    num_artworks = artist_freq[artist_name]
    template = "There are {num} artworks by {name} in the data set"
    print(template.format(num = num_artworks, name = artist_name))
artist_summary("Henri Matisse")
    

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
template = "The population of {name} is {num:,.2f} million"
for row in pop_millions:
    country = row[0]
    population = row[1]
    output = template.format(name = country,num = population)
    print(output)

## 9. Challenge: Summarizing Artwork Gender Data ##

dic_gender = {}

for row in moma:
    gender = row[5]
    if gender in dic_gender:
        dic_gender[gender] += 1
    else:
        dic_gender[gender] = 1

for gender,fre in dic_gender.items():
    template = "There are {num:,} artworks by {sex} artists"
    print(template.format(num = fre,sex = gender))