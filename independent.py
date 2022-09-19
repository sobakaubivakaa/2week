# independent work week 2
# task1
# numbers = [0,0,1,1,2,2,3,4,5]
# numbers.reverse()
# print(numbers)

# task2
# numbers = [0,0,1,1,2,2,3,4,5]
# def change():
#     temp = numbers[0]
#     numbers[0] = numbers[len(numbers)-1]
#     numbers[len(numbers)-1] = temp
# change()
# print(numbers)

# task3
# def lists(*args):
#    return list(args)
# print(lists(1, 2 , 5, 6,))

# # task4
# def useless(*args):
#     max = args[0]
#     for i in args:
#         if i > max:
#             max = i
#             temp = max / (len(args))
#     return temp,max,sum
#
#
# print(useless(7,7,7))


# task5
# def list_sort(list):
#     for i in range (0, len(list)):
#         list[i] = abs(list[i])
#     list.sort(reverse=True)
#     return list
# print(list_sort([-7,5,0,3,-9]))

# task6
# def work(list):
#     max = 0
#     n=0
#     char = "_"
#     for word in list:
#         if max < len(word):
#             max = len(word)
#     for word in list:
#         n = len(word) - max
#         n = abs(n)
#         word = f'{char * n}{word}'
#         print(word)
# words = ["Sad","INFP","IhateMath","IhateMuslim","IhateRussianLanguage"]
# work(words)
