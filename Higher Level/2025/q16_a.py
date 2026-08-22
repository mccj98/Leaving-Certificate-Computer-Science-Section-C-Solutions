# Question 16 (a)
#Examination Number:


def get_grade(result): #Value inputted into the function is referred to as result in the function
    grade = "Unsuccessful"


    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    #Simply just adding more conditions to the function
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    elif result < 40:
        grade ="Fail"

    return grade


#Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] #Initialise the list
N = len(results) #Initialise N to the number of results
total = 0 #Initialise the running total to 0


#Loop N times
for i in range(N):
    total = total + results[i] #running total


#Divide by the total number of results to give the mean
arithmetic_mean = total / N
arithmetic_mean = round(arithmetic_mean,2) #changes the reference within the variable
print("The mean percentage mark is: ", arithmetic_mean)

print("The grade for the average result is" ,get_grade(arithmetic_mean)) #function call and passing variable into function
print("The lowest score is", min(results))
print("The highest score is", max(results))

count1 = 0
for i in range(N):
    if results[i] < 40:
        count1+= 1
print("The number of scores below 40 is", count1)
count2 = 0 #need to assign value which also assigns data type to the variable
for i in range(N):
    if results[i] >= 50 and results[i] <= 79:
        count2+= 1
print("The number of scores between 50 and 79 inclusive is", count2)

current_len = 0
current_list =[results[0]]

num_of_lengths = 0
lists = []
lengths = []
for i in range(1, N):
    if results[i] > results[i-1]: #if increasing
        current_len += 1 #increas consec count
        current_list.append(results[i]) #add element to the sequence
    else: #not consec increasing
        lists.append(current_list) #record current sequence to history
        lengths.append(current_len) #record length of this sequence
        current_len = 0 #reset length for next run
        current_list = [results[i]] #add starting element as the first element of newly tracking sequence
        num_of_lengths += 1 #increase count of consec increasing lists by 1
lists.append(current_list) # add last list to the record 
lengths.append(current_len)
num_of_lengths += 1
#print(lists)
#print(lengths)

position = lengths.index(max(lengths))
#for f in range(1, num_of_lengths):
#    if lengths[f] > lengths[f-1]:
#        position = f
print("The longest run of result increases is", lists[position])

