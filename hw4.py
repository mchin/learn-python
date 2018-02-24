
# Wisconsin has eight congressional districts covering its land area of 169,790 square kilometers,
# while Alaska has just one district for its 1,717,856 square kilometers.
# Write a program which determines how many times bigger than the average Wisconsin district that Alaskan district is.

# declare vars
wisconsin_dist = 8
wisconsin_area = 169790
wisconsin_avg = float(wisconsin_area/wisconsin_dist)

alaska_dist = 1
alaska_area = 1717856
alaska_avg = float(alaska_area/alaska_dist)

# print district averages
print('First we need to calculate the Alaska district average: ', + round(alaska_avg,2))
print('Then we need to calculate the Wisconsin district average: ', + round(wisconsin_avg, 2))

# Alaska is how many times bigger than Wisconsin?
# alaska_avg = x * wisconsin_avg
# x =  alaska_avg / wisconsin_avg
times = float(alaska_avg / wisconsin_avg)
# Print the percentage
print('By my calculations, the Alaskan district is about', + round(times,2), 'times bigger than the Wisconsin district.')
