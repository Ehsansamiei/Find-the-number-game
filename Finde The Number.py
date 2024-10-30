# Ehsan 

# Data 
sum = 6
#==================================================#

# Libraries 
import random 
#==================================================#

# Informaition 
answer = random.randint(1, 99)
print('-----------------------------------')
name = input('what is your name ? \t')
print('\n')
print('---------------> Hi',name,' <----------------') 
print('\n')
print('---> In this game you have 5 chances to finde the number !')
print('---> If the guess is wrong , One of your chances decreases')
print('---> This game is so easy :)')
print('---> Good luck',name,':)')
print('\n')
while True : 
    try : 
        guess =  int(input('what is your guess ? (1, 99) \t'))
        break
    except ValueError: 
        print('---------------->>  You have to enter number :/  <<----------------')
    except EOFError : 
        print("this game is for ever, there's no escape :)) ")

print('------------------------------------------')
#==================================================#

# Loop
while sum > 0 : 
    if guess == 'exit()':
        break

    if guess < answer :
        #print('\n')
        print('my number is larger ! \n')
        sum -= 1
        print ('You have',sum -1 ,'chances ! \n')
    if guess > answer : 
        print('my number is smaller ! \n')
        sum -= 1
        print ('You have',sum - 1,'chances ! \n')
    
    while True : 
        try : 
            guess =  int(input('Now what is your guess ? (1, 99) \t'))
            break
        except ValueError : 
            print('---------------->>  You have to enter number :/  <<----------------')
        except EOFError : 
            print("this game is for ever, there's no escape :)) ")

    print('------------------------------------------')

    if guess == answer : 
        print('---------------->> You Rock ! <<----------------')
        print('\n')
        break
    if sum == 0:
        print('You loooooose ooooooooooooooooooooooo')
#==================================================#

# End Of Game
print('---------------->> The number was',answer,'<<----------------')
print('\n')
print('---------------->> The End! <<----------------')        
print('\n')   