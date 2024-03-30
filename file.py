import os
import name as Name

print(Name.title())

para = "'Choose any of the following options you want to do something'\n"

options = "1.Read a File \n 2.Write a File \n 3.Create a File \n 4.Exit"
print(para.upper(),options)


while True:
     # Reading the content from the file
     def readFile():
          print("""
                    #####   ######    ##    #####           ######  #####   #       ######
                    #    #  #        #  #   #    #          #         #     #       #
                    #####   #####   #    #  #    #          #####     #     #       #####
                    #   #   #       ######  #    #          #         #     #       #
                    #    #  #       #    #  #    #          #         #     #       #
                    #    #  ######  #    #  #####           #       #####   ######  ######

          """)
          file_Name = input("Enter a File Name : ")
          file_Path = "{}.txt".format(file_Name)
          user_Path = os.getcwd()
          full_Path = user_Path+"\\"+file_Path
          if os.path.exists(full_Path):
               password = input("Enter your password : ")
               if password == "silambu":
                    with open(file_Path,'r') as file:
                         outText = file.read()
                         print(outText)
               else:
                    print("Password is wrong")
          else:
               print("There is no file is Exist ?????")
               print("So you create it !!!1")
     # Reading content is end---------------------------

     def writeFile():
          print("""
                    #    #  #####   #####   ######  ######          ######  #####   #       ######
                    #    #  #    #    #       #     #               #         #     #       #
                    #    #  #####     #       #     #####           #####     #     #       #####
                    # ## #  #   #     #       #     #               #         #     #       #
                    ##  ##  #    #    #       #     #               #         #     #       #
                    #    #  #    #  #####     #     ######          #       #####   ######  ######
    
          """)
          write_File = input("Writting file name : ")
          cur_Path = os.getcwd()
          full_Path = cur_Path + "\\"+write_File+".txt"
          print(full_Path)
          if os.path.exists(full_Path):
               new_Data = input("Add a file Content : ")
               with open(write_File+".txt",'a') as file:
                    file.write(new_Data)
                    print("Successfully ! Content is added in your File")
          else:
               print("???????????????File is not Found?????????????????")


     # File created is start------------------------------
     def createFile():
          print("""
                     #####  #####   ######    ##    ######  ######          ######  #####   #       ######  
                    #       #    #  #        #  #     #     #               #         #     #       #       
                    #       #####   #####   #    #    #     #####           #####     #     #       #####   
                    #       #   #   #       ######    #     #               #         #     #       #       
                     #####  #    #  ######  #    #    #     ######          #       #####   ######  ######  

                    """)
          new_File = input("New File Name : ")
          get_Path = os.getcwd()
          full_Path = get_Path+"\\"+new_File+".txt"
          if os.path.exists(full_Path):
               print("Already file is exist in {}".format(full_Path))
          else:
               with open(full_Path,'a') as file:
                    print("File is created successfully {}".format(full_Path))
     
     # File created is end------------------------------- 

     opt = int(input("Enter your options 1/2/3/4 : "))
     if opt <= 0 or opt > 4:
          print("Please enter a Valid ")     
     else:
          if opt == 1:
               readFile()
          elif opt == 2:
               writeFile()
          elif opt == 3:
               createFile()
          else:
               print(""""
                         #####         #    #  #####    #####   #####     #    #   #####  #    #
                           #           ##  ##    #     #       #           #  #   #    #  #    #
                           #           # ## #    #      #####   #####       ##    #    #  #    #
                           #           #    #    #          #       #       #     #    #  #    #
                           #           #    #    #     #    #  #    #       #     #    #  #    #
                         #####         #    #  #####    #####   #####       #      #####   #####
                                    """)
               exit()

     

