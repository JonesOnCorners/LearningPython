#take credit cardnumber as input
#pass it to a function which converts it to a list
#double every second digit starting from the right
#check for double digit sums, add them and replace corresponding double digits
#obtain final list and it's sum


def fun_to_double_input(num):
    num = num * 2
    if num > 9 :
        obtain_single_digit = list(map(int, str(num)))
        return(obtain_single_digit[0] + obtain_single_digit[1])
    else:
        return num
     

def card_validator(cc_number):
    cc_card_list = []
    cc_card_list = list(map(int, cc_number))
    cc_card_list_mod = cc_card_list[0::2]
    cc_card_list_rev = cc_card_list[-2::-2]   
    cc_card_list_doubled = list(map(fun_to_double_input,cc_card_list_rev))
    cc_card_final = cc_card_list_doubled + cc_card_list_mod
    
    print("original ",cc_card_list)
    print("remaining ",cc_card_list_mod)
    print("Reversed ",cc_card_list_rev)
    print("Doubled ",cc_card_list_doubled)
    print("Final ",cc_card_final)
    
    sum = 0
    for x in cc_card_final:        
        sum = sum + x

    if sum % 10 ==0:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    cc_number = input("Please enter the credit card number to be validated.\n")
    card_validator(cc_number)
   #if(len(str(cc_number))) != 10:
    #    print("Not Valid")
    #else:
     


