#Вариант 23.
#Восьмиричные числа не превышающие 409610. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К. 
#Список используемых цифр выводится отдельно прописью.


nums = {'0':"ноль",'1':'один','2':"два",
        '3':"три",'4':"четыре",'5':"пять",
        '6':"шесть",'7':"семь",'8':"восемь",'9':"девять",}
k = input("введите число k: ")
k = int(k)
max_num = 4096
max_num_oct = int(oct(max_num)[2:])
num = []
num_list = []
file_nums = []
with open("text.txt","r") as file:
    file_nums.append(file.read().split())
    for i in range(len(file_nums[0])):
        num.append(file_nums[0][i])
    for n in range(len(num)):
        if abs(int(num[n])) <= max_num_oct and abs(int(num[n])) % 2 == 1 and len(str(num[n])) % 2 == 0 and len(str(num[n])) > k:
                for x in str(num[n]):
                    num_list.append(int(x))
                for o in num_list:
                    print(nums[str(o)], end = " ")
                print(" ")
                num_list = []
                                    

        

