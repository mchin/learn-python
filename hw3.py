# Every state in the U.S. has two senators, but Florida has 20 million people to Idaho's 1.6 million.
# Write a program that shows how many Floridians it takes to equal the Senatorial power of one Idahoan.

florida_population = 20000000
idaho_population = 1600000

print('One Idahoan equals', float( florida_population / idaho_population), 'Floridians or rounded up, 13 Floridians since half a person is not countable')
print('Idaho is', float(100 * idaho_population / florida_population), '% of the population of Florida')
