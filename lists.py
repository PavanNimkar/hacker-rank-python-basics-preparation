if __name__ == '__main__':
    N = int(input())
    
    my_list = list()
    
    for _ in range(N):
        command = input().split()
        
        if "insert" in command:
            index = int(command[1])
            value = int(command[2])
            my_list.insert(index, value)
            
            
        elif "print" in command:
            print(my_list)
            
        elif "remove" in command:
            value = int(command[1])
            my_list.remove(value)
            
            
        elif "append" in command:
            value = int(command[1])
            my_list.append(value)
            
            
        elif "sort" in command:
            my_list.sort()
            
            
        elif "pop" in command:
            my_list.pop()
            
            
        elif "reverse" in command:
            my_list.reverse()
            
        
        command = list()