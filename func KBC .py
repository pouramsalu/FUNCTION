
# question_func=["how many countries are there?"," what is the capital of india?","what course did they teach in NG?"]

# option_func=[["Four","Nine","Seven","Eight"],
# ["Chandigard","Bhopal","Chennai","Delhi"],
# ["Software engineering","Counselling","Tourism","Agriculture"]]
# solution_func=[3,4,1]
# def function(index):
#     i=0
#     while i<len(option_func[index]):
#         print(i+1,option_func[index][i])
#         i+=1
#     user=int(input("enter the number:-"))
#     if user==solution_func[index]:
#         return(True)
#     else:
#         return(False)
# def num():
#     j=0
#     while j<len(question_func):
#         print("q",j+1,question_func[j])
#         result=function(j)
#         if result==True:
#             print("congratulation your answer is correct")
#         else:
#             print("better luck next time")
#             break
#         j+=1
# def main():
#     num()
# main()




question_list=["how many countries are there?","what is the capital of india?","what course did they teach in NG?"]
solution_list=["Four","nine","seven","eight"],
["chandigard","bhopal","chennai","delhi"],
["software engineering","counselling","tourism","agriculture"]

answer_list=[3,4,1]
fifty_list=[['1.Four','3.seven'],['2.Bhopal','4.Delhi'],['1.Software Engineering','2.Counseling']]
solution_list=[3,4,1]
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0):
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('enter the optin.....'))
        lifelinecount+=1
        if user_ans==solution_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"
        
def option(index):
    j=0
    while j<len(option[index]):
        print(j+1,option[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==answer_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    i=0
    while i<len(que):
        print("Q.",i+1,que[i],"?")
        result=option(i)
        if result=="no":
            i-=1
        elif result==True:
            print("congratulations")
        else:
            print("you loose")
            break   
        i+=1

def main():
    que()
main()

