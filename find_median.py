# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def find_median(num):
    for x in num:
        if len(num)%2==1:
            result=(max(num)+1)/2
            return result
        elif len(num%2)==0:
            result=(((max(num)/2)+((max(num)/2)+1)))/2
            return result
#print(find_median([1,3,5,7,9]))



