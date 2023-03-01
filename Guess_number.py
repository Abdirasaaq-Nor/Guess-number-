d = {"ali": 19, "abdirsq": 17}
for i in d.keys():
    if i == 'ali':
        user_name = input("enter your name: ")
        secret = len(user_name)
        count = 0
        while True:
            user = input('take a number: ')
            if int(user) == secret:
                print('you correct the secret number', secret)
                break
               
            else:
                for i in range(0, 3):
                  
                    if count > 2:
                        print('secret number is ', secret)
                        break
                    
                       
                    else:
                        print('try again')
#                         print(f'this is i {count}')
                        count += 1
                        break
                
                
                
        break
    else:
        print('not working')
        break