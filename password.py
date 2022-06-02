# secret message

password = 'FIFA 22 FORTNITE ZAIN IS GENIUS777' 
guess = ''
secret_message = 'if you get the password right you can see this'
limit = 10

while(True) :
  print('Enter a Password')
  guess = input()
  if guess == password :
    print(f"{secret_message}")
    break
  else :
    limit = limit - 1
    if limit == 0 :
      print("You have no guesses left")
      break
    print(f"You have {limit} guesses left")
    print("try again")
    
