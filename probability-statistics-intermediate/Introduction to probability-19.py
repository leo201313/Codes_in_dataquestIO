## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country=flags[flags['bars']==flags['bars'].max()]['name']
highest_population_country=flags[flags['population']==flags['population'].max()]['name']


## 2. Calculating probability ##

total_countries = flags.shape[0]
orange_probability=flags[flags['orange']==1].shape[0]/total_countries
stripe_probability=flags[flags['stripes']>1].shape[0]/total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads=.5**10
hundred_heads=.5**100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total_count=flags.shape[0]
red_count=flags[flags['red']==1].shape[0]
three_red=1
for time in range(3):
    three_red=three_red*red_count/total_count
    red_count-=1
    total_count-=1

## 5. Disjunctive probability ##

start = 1
end = 18000
hundred_prob=180/end
seventy_prob=int(18000/70)/end

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
total_count=flags.shape[0]
red_and_orange=flags[(flags['red']==1) & (flags['orange']==1)].shape[0]
red=flags[flags['red']==1].shape[0]
orange=flags[flags['orange']==1].shape[0]
red_or_orange=(red+orange-red_and_orange)/total_count

stripes_and_bars=flags[(flags['stripes']>=1) & (flags['bars']>=1)].shape[0]
stripes=flags[flags['stripes']>=1].shape[0]
bars=flags[flags['bars']>=1].shape[0]
stripes_or_bars=(stripes+bars-stripes_and_bars)/total_count

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = 1-.5**3