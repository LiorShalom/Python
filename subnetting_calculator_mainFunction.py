from colorama import Fore
from colorama import Style

address_color = Fore.CYAN            # ip color is   --> LIGHTBLUE.
note_color = Fore.YELLOW        # note color is --> YELLOW.
error_color = Fore.LIGHTRED_EX
reset_color = Style.RESET_ALL   # resets color.

rules = False
#   rules will be 'True' if:
#       it contains only numbers.
#       it contins 3 dots between each number.
#       each number will be in range of 0-255.

again = False
SB_Pref = '' # SubnetMask or Prefix argument.
IP = '' # IP argument.


# input of the rest of the IP address:
def restof_address(address):
    listof_address = []
    finish = False

    # print("{ getinto restof_address function }")
    address = str(address)
    listof_address.append(address)
    address = '.'.join(listof_address)

    # print current address.
    print("{}{}{}".format(address_color, address, reset_color))

    while True:
        print("Enter the next octate: {}".format(address_color), end = '')
        next_octate = input("")
        print("{}".format(reset_color), end = '')
        
        if next_octate.isnumeric() and int(next_octate) < 256:
            
            listof_address.append(next_octate)
            address = '.'.join(listof_address)
            
            # print current address.
            print("{}{}{}".format(address_color, address, reset_color))
            if len(listof_address) == 4:
                finish = True
                # break
        else:
            invalid_input()

        if finish == True:
            print()
            break
    return address




def yesor_no():
    # print("{ getinto yesor_no function }")
    while True:
        answer = input("Yes/No: {}".format(note_color))
        print('{}'.format(reset_color))
        answer = answer.lower()
        if not answer.isalpha():
            invalid_input()
            continue
        elif answer == 'yes' or answer == 'y':
            answer = 'y'
            return answer
        elif answer == 'no' or answer == 'n':
            answer = 'n'
            return answer
        else:
            invalid_input()




# prints out the IP address:
def output(address, Prefix = False):
    # print("{ getinto output function }")
    if Prefix == True:
        print("Your Prefix is {}{}{}".format(address_color, address, reset_color))
    else:
        print("Your IP is {}{}{}".format(address_color, address, reset_color))


# Error message about invalid input:
def invalid_input():
    print("{}Invalid input!\nPlease try again.{}".format(error_color, reset_color))




# IP or Subnet:
def collect_arguments(rules, address):
    while rules == False:
        Prefix = False
        octate = ''
        error = False
        answer = ''
        count_errors = 0
        invalid_indexNum = []
        invalidNum = []
        
        if IP == '': # for IP
            print("Enter an IP address:")
            print("{}>>>{}  {}".format(Fore.MAGENTA, reset_color, address_color), end = '')
            address = input("")
            print(reset_color)
        elif IP != '': # for SubnetMask or Prefix
            print("\nEnter a Prefix:")
            print("{}>>>{}  {}".format(Fore.MAGENTA, reset_color, address_color), end = '')
            address = input("")
            print(reset_color)
            Prefix = True
        else:
            print("{}An error occurred!{}".format(error_color, reset_color))
            break


        # checks if 'IP'contains only numbers and dots:
        if address.isnumeric() or "." in address:

            # checks 'IP' contain only 3 dots:
            if address.count(".") == 3 and Prefix == False:
                listof_address = address.split(".")
                for i in range(len(listof_address)):
                    if listof_address[i] == '':
                        listof_address[i] = '0'
                    elif listof_address[i].isnumeric():
                        octate = int(listof_address[i])
                        listof_address[i] = str(octate)
                        if Prefix == True:
                            if not (octate == 255 or octate == 0):
                                count_errors += 1
                                invalid_indexNum.append(i)
                                invalidNum.append(octate)
                            else:
                                print("checking if the subnet maks is valid.")
                                
                                break
                               
                        elif octate >= 256:
                            count_errors += 1
                            invalid_indexNum.append(i)
                            invalidNum.append(octate)
                    else:
                        invalid_input()
                        error = True
                if error == True:
                    continue
                

                # Errors check:
                if count_errors != 0:
                    print("{}ATTENTION!\n{} invalid values were found in your input:{}".format(error_color, count_errors, reset_color))

                    for error_num in range(len(invalid_indexNum)):
                        print("-- {}The number{} {}{}{} {}in octate{} {}{}{} {}is invalid.{}".format(error_color, reset_color, address_color, invalidNum[error_num], reset_color, error_color, reset_color, address_color, invalid_indexNum[error_num] + 1, reset_color, error_color,reset_color))
                    print("\nPlease try again.")
                    continue
                    

                # END of IP - output
                address = '.'.join(listof_address)
                output(address)

                return address
                # rules = True



            elif not '.' in address:
                address = int(address)
                
                if Prefix == True:
                    if address > 32:
                        invalid_input()
                        continue
                    else:
                        # print("{}Your input was only one number.{}\nDo you want it to be the value of the Prefix?".format(note_color, reset_color))
                        output(address, Prefix)
                        return address
                        # print("")
                        # answer = yesor_no()
                # checks if the number is in range 0 to 255.
                elif address < 256:
                    print("{}Your input was only one number.{}\nDo you want it to be the value of the first octate?".format(note_color, reset_color))
                    answer = yesor_no()

                if answer == 'y':
                    # print("ok!")
                    if Prefix == False:
                        address = restof_address(address)
                        output(address)
                        return address
                        # rules = True
                    elif Prefix == True:
                        output(address, Prefix)
                        return address
                        # rules = True
                elif answer == 'n':
                    print("Ok, so try again.")
                    continue
                elif Prefix == False:
                    invalid_input()
                    print("(your number is not it the range of 0 to 255.)")
                    
            else:
                invalid_input()

                
        else:
            invalid_input()
            if IP == '':
                print("{}NOTE: IP must contain only numbers and dots!{}\n".format(note_color, reset_color))







# welcome - enter your name:

print(Fore.MAGENTA + "\nWelcome to the subnetting calculator!\n" + reset_color)
print("At first I need to know you, {}what is your name?\n{}>{} If you want to skip type {}'skip'{} or {}'/0'{} and press {}'enter'{} to continue.".format(Fore.MAGENTA, note_color, reset_color, note_color, reset_color, note_color, reset_color, note_color, reset_color))

while True:
    
    if again == True:
        print('{}Enter your name: {}'.format(Fore.MAGENTA, reset_color), end = '')
        name = input()
        name = name.lower()
    else:
        print(Fore.MAGENTA + ">>> ", end = '')
        name = input("{}".format(reset_color))
        name = name.lower()
        print()


    if name == '/0' or name == 'skip':
        print("Ok!\n")
        break
    elif not name.isalpha() or ' ' in name:
        invalid_input()
        print("{}Your name must contain only letters!{}\n".format(error_color, reset_color))
        again = True
    else:
        name = name[0].upper() + name[1:].lower()
        print("{}Hi {} nice to meet you!{}\n".format(address_color, name, reset_color))
        break



IP = collect_arguments(rules, IP)
# print(IP)
Prefix = collect_arguments(rules, IP)
# print(Prefix)


def calculator(IP, Prefix):
    DONE = True
    print("{}\n\nSubnetting results:\n{}".format(Fore.MAGENTA, reset_color))
    ocatateNum = 0
    lastoctate = ''
    subnet_list = ['0','0','0','0']
    IP_list = IP.split('.')
    print("IP:\t{}{}{}\n".format(address_color, IP, reset_color) + "Prefix: {}{}{}".format(address_color, Prefix, reset_color))
    
    netbin = Prefix % 8
    hostbin = (8 - netbin)

    subnetnetpart = Prefix // 8 # calculating how much '255' we need in the SubnetMask. (if Perfix == 17: subnetnetpart = 2)
    for i in range(subnetnetpart):
        subnet_list[i] = '255' # according to the above example - '255.255.0.0'
    
    numof_hosts = 1
    for i in range(hostbin): # calculating the number of hosts in each subNetwork.
        numof_hosts *= 2

    for i in range(len(subnet_list)):
        if i == 3:
            IPlastoctate = int(IP_list[i])
            ocatateNum = i
        if subnet_list[i] == '255':
            continue
        else:
            subnet_list[i] = str(256 - numof_hosts) # last octate for the netPart
            SUBlastoctate = int(subnet_list[i])
            IPlastoctate = int(IP_list[i])
            ocatateNum = i
            break
        

    subnet_mask = '.'.join(subnet_list)
    

    print("Subnet Mask: \t{}{}{}".format(address_color, subnet_mask, reset_color))
    print("Hosts in each subnet: {}{}{}".format(address_color, numof_hosts, reset_color)) 

    if Prefix >= 0 and Prefix < 8:
        for jump in range(0, 255, numof_hosts):
            if IPlastoctate not in range(jump, jump + numof_hosts):
                continue
            else:           
                    
                # print("{}class A{}".format(error_color, reset_color))
                # NETWORK
                IP_list[ocatateNum] = str(jump)
                IP_list[ocatateNum + 1] = str(0)
                IP_list[ocatateNum + 2] = str(0)
                IP_list[ocatateNum + 3] = str(0)
                Network = '.'.join(IP_list)
                # FIRST HOST
                IP_list[ocatateNum] = str(jump)
                IP_list[ocatateNum + 1] = str(0)
                IP_list[ocatateNum + 2] = str(0)
                IP_list[ocatateNum + 3] = str(1)
                First_Host = '.'.join(IP_list)
                # LAST HOST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                IP_list[ocatateNum + 1] = str(256 - 1) # 255
                IP_list[ocatateNum + 2] = str(256 - 1) # 255
                IP_list[ocatateNum + 3] = str(256 - 2)  # 254
                Last_Host = '.'.join(IP_list)
                # BROADCAST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                IP_list[ocatateNum + 1] = str(256 - 1)  # 255
                IP_list[ocatateNum + 2] = str(256 - 1)  # 255
                IP_list[ocatateNum + 3] = str(256 - 1)  # 255
                Broadcast = '.'.join(IP_list)
                # NEXT SUBNET
                if jump + numof_hosts > 255:
                    IP_list[ocatateNum] = str(256 - 1) # 255
                    IP_list[ocatateNum + 1] = str(256 - 1) # 255
                    IP_list[ocatateNum + 2] = str(256 - 1) # 255
                    IP_list[ocatateNum + 3] = str(256 - 1) # 255
                else:
                    IP_list[ocatateNum] = str(jump + numof_hosts)
                    IP_list[ocatateNum + 1] = str(0)
                    IP_list[ocatateNum + 2] = str(0)
                    IP_list[ocatateNum + 3] = str(0)
                Next_Subnet = '.'.join(IP_list)
                break

    elif Prefix >= 8 and Prefix < 16:
        for jump in range(0, 255, numof_hosts):
            if IPlastoctate not in range(jump, jump + numof_hosts):
                continue
            else:           
                    
                # print("{}class A{}".format(error_color, reset_color))
                # NETWORK
                IP_list[ocatateNum] = str(jump)
                IP_list[ocatateNum + 1] = str(0)
                IP_list[ocatateNum + 2] = str(0)
                Network = '.'.join(IP_list)
                # FIRST HOST
                IP_list[ocatateNum] = str(jump)
                IP_list[ocatateNum + 1] = str(0)
                IP_list[ocatateNum + 2] = str(1)
                First_Host = '.'.join(IP_list)
                # LAST HOST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                IP_list[ocatateNum + 1] = str(256 - 1)  # 255
                IP_list[ocatateNum + 2] = str(256 - 2)  # 254
                Last_Host = '.'.join(IP_list)
                # BROADCAST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                IP_list[ocatateNum + 1] = str(256 - 1)  # 255
                IP_list[ocatateNum + 2] = str(256 - 1)  # 255
                Broadcast = '.'.join(IP_list)
                # NEXT SUBNET
                if jump + numof_hosts > 255:
                    IP_list[ocatateNum - 1] = str(int(IP_list[ocatateNum - 1]) + 1)
                    IP_list[ocatateNum] = str(0)
                    IP_list[ocatateNum + 1] = str(0)
                    IP_list[ocatateNum + 2] = str(0)
                else:
                    IP_list[ocatateNum] = str(jump + numof_hosts)
                    IP_list[ocatateNum + 1] = str(0)
                    IP_list[ocatateNum + 2] = str(0)
                Next_Subnet = '.'.join(IP_list)
                break

                # CLASS B - 255.255.0.0 ~ 255*255
    elif Prefix >= 16 and Prefix < 24:
        for jump in range(0, 255, numof_hosts):
            if IPlastoctate not in range(jump, jump + numof_hosts):
                continue
            else:           
                    
                # print("{}class B{}".format(error_color, reset_color))
                # NETWORK
                IP_list[ocatateNum] = str(jump)
                IP_list[ocatateNum + 1] = str(0)
                Network = '.'.join(IP_list)
                # FIRST HOST
                IP_list[ocatateNum] = str(jump)
                IP_list[ocatateNum + 1] = str(1)
                First_Host = '.'.join(IP_list)
                # LAST HOST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                IP_list[ocatateNum + 1] = str(256 - 2)  # 254
                Last_Host = '.'.join(IP_list)
                # BROADCAST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                IP_list[ocatateNum + 1] = str(256 - 1)  # 255
                Broadcast = '.'.join(IP_list)
                # NEXT SUBNET
                if jump + numof_hosts > 255:
                    IP_list[ocatateNum - 1] = str(int(IP_list[ocatateNum - 1]) + 1)
                    IP_list[ocatateNum] = str(0)
                    IP_list[ocatateNum + 1] = str(0)
                else:
                    IP_list[ocatateNum] = str(jump + numof_hosts)
                    IP_list[ocatateNum + 1] = str(0)
                Next_Subnet = '.'.join(IP_list)
                break

                # CLASS D - 255.255.255.0 ~ 255
    elif Prefix >= 24:
        for jump in range(0, 255, numof_hosts):
            # print(jump)
            if IPlastoctate not in range(jump, jump + numof_hosts):
                continue
            else:

                # print("{}class C{}".format(error_color, reset_color))
                # NETWORK
                IP_list[ocatateNum] = str(jump)
                Network = '.'.join(IP_list)
                # FIRST HOST
                IP_list[ocatateNum] = str(jump + 1)
                First_Host = '.'.join(IP_list)
                # LAST HOST
                IP_list[ocatateNum] = str(jump + numof_hosts - 2)
                Last_Host = '.'.join(IP_list)
                # BROADCAST
                IP_list[ocatateNum] = str(jump + numof_hosts - 1)
                Broadcast = '.'.join(IP_list)
                # NEXT SUBNET
                if jump + numof_hosts > 255:
                    IP_list[ocatateNum - 1] = str(int(IP_list[ocatateNum - 1]) + 1)
                    IP_list[ocatateNum] = str(0)
                else:
                    IP_list[ocatateNum] = str(jump + numof_hosts)
                Next_Subnet = '.'.join(IP_list)
                break

    print("Network:{}\t".format(address_color) + Network, reset_color)
    print("First Host:{}\t".format(address_color) + First_Host, reset_color)
    print("Last Host:{}\t".format(address_color) + Last_Host, reset_color)
    print("Broadcast:{}\t".format(address_color) + Broadcast, reset_color)
    print("Next Subnet:{}\t".format(address_color) + Next_Subnet, reset_color)


calculator(IP, Prefix)



