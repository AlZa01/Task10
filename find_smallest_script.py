import two_smallest
import lists
with open('results.txt', 'w') as file:
    for number in [lists.list1, lists.list2, lists.list3, lists.list4]:
        small1, small2 = two_smallest.find_two_smallest(number)
        file.write("For "+str(number)+": "+str(small1)+", "+str(small2)+"\n")
print("Results are saved to results.txt")