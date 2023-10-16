#main.py
import functions

result1, sorted_list1 = functions.add_and_sort_numbers(2, 1)
result2, sorted_list2 = functions.add_and_sort_numbers(5)
result3, sorted_list3 = functions.add_and_sort_numbers(3, 4, verbose=True)
result4, sorted_list4 = functions.add_and_sort_numbers(7, verbose=True)

print("Result 1: Sum =", result1, "Sorted List =", sorted_list1)
print("Result 2: Sum =", result2, "Sorted List =", sorted_list2)
print("Result 3: Sum =", result3, "Sorted List =", sorted_list3)
print("Result 4: Sum =", result4, "Sorted List =", sorted_list4)
