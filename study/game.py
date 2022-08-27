import numpy as np

number = np.random.randint(1,1001)
count = 0

while True:
    count+=1
    predict_number=int(input('Guess the number from 1 to 1000:'))
    
    if predict_number>number:
        print('Your number is too big!')
        
    if predict_number<number:
        print('Your number is too small!')
        
    if predict_number==number:
        print(f'Congratilations!! You are right!! You needed only {count} tries...')
        break