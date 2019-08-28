person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
def stupid_array_tricks(array):
        print(array[1:3])
        print(array[2:4])
        array.insert(2,"Chuck")
        print(array)
        array.pop(1)
        print(array)
(stupid_array_tricks(person_array))

#Problem 2
user=input("Enter a word ")
while(user!="q"):
    user=input("Try again ")

#Problem 3
data=['GOOD_DATA','DECENT_DATA','BAD_DATA','DECENT_DATA','GOOD_DATA','BAD_DATA','GOOD_DATA','DECENT_DATA','BAD_DATA',
      'GOOD_DATA']
print(data.__len__())
data.pop(2) # !! : you should be able to do this without knowing the index position!
data.pop(4) # !! : you should be able to do this without knowing the index position!
data.pop(6) # !! : you should be able to do this without knowing the index position!
print(data)
print(data.__len__())

#Problem 4
score_list = [21,14,6,8,28,42,21]
print(f"The sum of the numbers is {sum(score_list)}")
print(f"The max of the numbers is {max(score_list)}")
print(f"The min of the numbers is {min(score_list)}")