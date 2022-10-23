# This program maps the transactions at different stores (Cities) and reduces the data into an
# aggregated report of total transaction amount for each Store(City).
#Input file - d.txt - contains date, time, store, item, cost, payment_amount of each transaction

#Step 1, we open the file and map the Store and amount for each transaction
i = open("data.txt","r")  # open input data file, read-only
m = open("map.txt", "w") # open file for mapping, write
for line in i:
    data = line.strip().split("    ") 
    print (data)
    print (len(data))
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print ("{0}\t{1}".format(store, cost))
        m.write("{0}\t{1}\n".format(store, cost)) # Writing Only needed data
i.close()
m.close()

#Step 2, we sort the data that contains Store and Amount
m = open("map.txt","r")  # open file, read-only
s = open("sort.txt", "w") # open file, write
lines = m.readlines()
lines.sort()
print(lines)
for line in lines:
	s.write(line)
m.close()
s.close()

#Step 3, we reduce the data through aggregation of amount based on the Store (City)
s = open("sort.txt","r")
r = open("reduce.txt", "w") #output file
thisKey = ""
thisValue = 0.0
for line in s:
  data = line.strip().split('\t')
  store, amount = data

  if store != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue) + '\n')
s.close()
r.close()