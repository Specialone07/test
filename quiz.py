
questions=[
  ["which is the best soccer player?",
  "Hari","Ram","Messi","Cristiano", 3],
  ["which is the best cricket player?",
  "ram","shyam","sachin","ponting",2],
  ["when was python first appeared?",
  int(1990),(2000),(2005),(1991),3],
  ["which the place where we can find the white elephant?", "nepal","india","china","thailand",3],
  ["which is the best boxing player?", "ram","shyam","sachin","ponting",1],
  ["which is the best ludo player?",   "ram","shyam","sachin","ponting",3],
  ["which is the best chess player?", "ram","shyam","sachin","ponting",2],
  ["which is the best hockey player?","ram","shyam","sachin","ponting",1],
]

levels=[1000,5000,10000,50000,60000,70000,80000,90000,100000]
money=10000
for i in range (0, len(questions)):
  question= questions[i]
  print(f"Question for Rs.{levels [i]}")
  print(question[0])
  print(f"a. {question[1]}       b. {question[2]}")
  print(f"c. {question[3]}       d. {question[4]}")
#   print(f"e. {questions[4]}       f. {questions[5]}")
#   print(f"g. {questions[6]}       h. {questions[7]}")
#   print(f"i. {questions[8]}       j. {questions[9]}")
#   print(f"k. {questions[10]}       l. {questions[11]}")
  reply=int(input("Enter answer(0-4)"))
  if (reply == question[-1]):
    if(i==3):
        money=10000
    # elif(i ==6):
    #     money=50000

    print(f"Correct answer You have won RS. {levels[i]}")
  else:
    print("Wrong answer")
    break