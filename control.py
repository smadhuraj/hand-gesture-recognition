class ControlInput:

    def controlSignal(inp, arr):
        
        bit = inp
        number = 0
        for x in range(5):
            number = number + int(bit[x])*pow(2,4-x)
        print('number is : ', arr[number])

        if(arr[number] == 'off'):
            print("true")
            arr[number] = 'on'
        else:
            arr[number] = 'off'

        for y in range(32):
            print(y ," - ",arr[y])

    # controlSignal(userInput)