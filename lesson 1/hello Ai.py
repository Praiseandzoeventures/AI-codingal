print('hello! I am AI Bot, What is your name? :')
name = input()
print(f'Nice to meet you , {name}')
print("How how you feeling today?"("good/bad"))
mood=input().lower()
if mood == "good" :
    print('I am glad to hear that')
elif mood =='bad':
    print('i am sorry to hear that, hope things get better soon')
else:
    print('I see sometimes it is hard to express feeling in words')
    
print(f'IT was nice talking to you {name}. Goodbye')