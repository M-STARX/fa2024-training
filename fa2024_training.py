import numpy as np
import math

# Welcome to the M-STARX GitHub + Python training file! If you've made it here
# you already completed a few steps, so good job! You can complete this training
# by accomplishing every task marked with "TODO". When you complete a step,
# remove the "TODO" comment! Once you've cleared every "TODO" statement, push
# your final file to your GitHub branch :)

# Note: this tutorial is very basic, especially if you're more experienced coder.
# We often have people joining the team from a wide variety of skill levels, so this is just
# intended to get everyone's personal machines set up and give people a basic familiarity with
# GitHub and Python syntax. I promise you'll learn tons of more involved stuff as the year 
# progresses on your subteam!!


# This function fills a numpy array with values from data_list in order.
# If size is specified, the array is declared with shape (1, size). If size is 
# unspecified, the array is declared with the same number of rows and columns, which is math.sqrt(len(data_list))
def fillArray(data_list, size=None):
    arr = None
    if size == None:
        #  variable equal to the length of square array
        length = int(math.sqrt(len(data_list)))
        # sets arr to the size of the length by length
        arr = np.empty([length, length])
        # check your work:
        if (arr.shape == (math.sqrt(len(data_list)), math.sqrt(len(data_list)))): print("Array Initialized Correctly!")

     
    else:
        # arr is declared with shape (1, size)
        arr  = np.empty(1, size)
        if (arr.shape == (1, size)): print("Array Initialized Correctly!") # check your work: prints the shape of the array

   # Traverses the data_list for each entry
    for x in range(len(data_list)):
        # adds each entry to arr
        arr.flat[x] = data_list[x]
           
    # returns the array
    return arr

# Lists are a common Python container, similar to vectors in C++ and MATLAB
list = [1, 2, 3, 4] # this is a really simple list, with 5 elements

# fills arr with the list
arr = fillArray(list)

# prints out initial arr
print(f"initial Array: {arr}")

# 1. operation 1
ones = np.ones(2, dtype=int)
# adds one to each element
arr = arr + ones
# prints out the array after operation 1
print(f"1st mod Array: {arr}")

# 2. operation 2
# multiplies each element by itself
arr = arr * arr
# prints out the array after operation 2
print(f"2nd mod Array: {arr}")

# 3. operation 3
# divides each element by 3
arr = arr /3

# adds an aditional axis to the array
arr = np.expand_dims(arr, axis=2)

# prints final array
print(f"Final Array: {arr}")

# TODO: Push your final changes to your GitHub branch in 3 steps:
#   1. Stage your changes for commit using the "git add" command. You can type the filename,
#      or just use "git add --all" to stage all the files you've changed in the repository.
#   2. Commit your changes to the reppository with "git commit -m "{commit message}"". Your
#      commit message should be short but descriptive!
#   3. Push your changes using the command "git push".
#   4. Check that you changes pushed successfully by running "git status".