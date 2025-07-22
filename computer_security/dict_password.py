input = input("Enter your pasword : ")
count = 1
with open('rockyou.txt','r',errors='ignore') as f:
    lines = f.readlines()
    clean_lines = [item.strip() for item in lines]
    
    for index,val in enumerate(clean_lines):
        count = count+1
        print(f'iteration {index+1}')
        if input == val:
            print(f"found target password '{val}' at line {index+1}")
            break