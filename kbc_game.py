
question_list = ["How many continents are there?","What is the capital of India?","ap kyaa banna chate ho?"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.teacher", "3.criceter", "4.bussinessmen"]]
solution_list = [3, 4, 1] 
fifty_fifty = [
['1.Four','3.seven'],['2.Bhopal','4.Delhi'],['1.Software Engineering','2.teacher']]
i = 0
count=0
print("kya ap  5050 lifeline  lena chate ho , to  enter kare  '5050' ")
while i < len(question_list):
    print(question_list[i])
    j = 0
    while j < len(options_list[i]):
        print(options_list[i][j])
        j=j+1
    user=int(input("enter your number option: "))
    if user == solution_list[i]:
        print('badhai ho ap jit chuke ho ')
    elif user == 5050:
        if count == 0:
            print(fifty_fifty[i])
            count=count+1
            user1  = int(input("apka answer btye : "))
            if user1 == solution_list[i]:
                print("badhai ho ! , apka jabab shi hai" )
            else:
                print("ohh !, apka jabab glt hai")
        else:
            print("apne 5050 use kr liya ab ap 5050 nhi le skte ho ") 
    else:
        print(" apka jabab ! glt hai ")
        break
    i=i+1
        
# python kbc game 
        