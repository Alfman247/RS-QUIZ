import time
again = 1
print("Welcome to Alfred's Quiz about Hinduism")
time.sleep(3)
while again == 1:
  score = 0
  variable = input("Are you ready to start (Just press enter on your keyboard!)")
  print("Question 1:")
  time.sleep(1)
  print("According to Hinduism, who is the cosmic giant?")
  q1 = input("")
  if q1 == "Purshma":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was 'Purshma'")
  
  print("Question 2:")
  time.sleep(1)
  print("According to a myth, who created the Earth (the other story)?")
  q2 = input("")
  if q2 == "Brahma":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was 'Brahma'")
  
  
  print("Question 3:")
  time.sleep(1)
  print("According to Hinduism, does god maintain the Earth?")
  q3 = input("")
  if q3 == "Yes":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was 'Yes'")

  print("Question 4:")
  time.sleep(1)
  print("According to Hinduism, how many gods are there (write a digit)?")
  q4 = input("")
  if q4 == "1":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was '1'")

  print("Question 5:")
  time.sleep(1)
  print("When did Hindusim start (answer with a digit please)?")
  q5 = input("")
  time.sleep(1)
  print("The answer was between 4000-5000 years ago")
  print("Unfortunately, I can't easily tell weather you are right, so type '1' if you got it right")
  q55 = input("")
  if q55 == 1:
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print (score)
    
  print("Question 6:")
  time.sleep(1)
  print("According to Hinduism, what head does Ganesh have?")
  q6 = input("")
  if q6 == "Elephant":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was 'Elephant'")
  
    print("Question 7:")
  time.sleep(1)
  print("According to Hinduism, what did Sita see?")
  q7 = input("")
  if q7 == "Deer":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was 'Deer'")
  
    print("Question 8:")
  time.sleep(1)
  print("According to Hinduism, what is another name for Divali (apart from Diwali)?")
  q8 = input("")
  if q8 == "The Festival of Lights":
    print("Well done!")
    time.sleep(1)
    print("I'll add 1 point to your score! Your score is now:")
    score = score + 1
    time.sleep(2)
    print(score)
  else:
    time.sleep(2)
    print("You were close! The answer was 'The Festival of Lights'")
  
  print("Thank you for playing!")
  time.sleep(1)
  print("Your score was...")
  time.sleep(1)
  print(score)
  time.sleep(3)
  
  hmmm = input("Do you want to play again? ")
  if hmmm == ("Yes"):
    again = 1
  else:
    again = 0
  
  
