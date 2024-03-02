#Вариант 23.
#Восьмиричные числа не превышающие 409610. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К. 
#Список используемых цифр выводится отдельно прописью.


nums = {'0':"ноль",'1':'один','2':"два",
        '3':"три",'4':"четыре",'5':"пять",
        '6':"шесть",'7':"семь",'8':"восемь",'9':"девять",}
k = input("введите число k: ")
k = int(k)
max_num = 4096
buf_len = 1
max_num_oct = int(oct(max_num)[2:])
num_list = []
file_nums = []                                                             
work_buffer = ""
with open("text.txt","r") as file:
      buffer = file.read(buf_len)                                    
      while buffer:                                                       
           while buffer >= '0' and buffer <= '7':                                                            
              work_buffer += buffer
              buffer = file.read(buf_len)
           if len(work_buffer) > 0:
             if abs(int(work_buffer)) <= max_num_oct and abs(int(work_buffer)) % 2 == 1 and len(str(work_buffer)) % 2 == 0 and len(str(work_buffer)) > k:
                for x in str(work_buffer): 
                    num_list.append(int(x))
                for o in num_list:
                    print(nums[str(o)], end = " ")
                print(" ")
                num_list = []
           work_buffer = ''
           buffer = file.read(buf_len)
              
                
      
                                    

        

