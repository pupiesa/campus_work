target = input('Enter you target password : ')
found = False
num = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 1
for i in range(len(num)):
    if found: break
    for j in range(len(num)):
        if found: break
        for k in range(len(num)):
            if found: break
            for x in range(len(num)):
                result = num[i] + num[j] + num[k]+ num[x]
                print(result,f"iteration : {count}")
                count += 1
                if target == result:
                    print(f'you found target password')
                    found = True
                    break
