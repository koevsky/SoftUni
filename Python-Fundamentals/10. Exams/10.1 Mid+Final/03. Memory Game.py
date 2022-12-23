elements_list = input().strip().split(" ")
moves_counter = 0
while True:
    line = input().strip()
    if line == "end" or not elements_list:
        if line == "end" and elements_list:
            print("Sorry you lose :(")
            print(" ".join(elements_list))
        elif not elements_list:
            print(f"You have won in {moves_counter} turns!")
        break
    integers_list = [int(x) for x in line.split(" ")]
    moves_counter += 1
    first_index, second_index = integers_list[0] , integers_list[1]
    #                       Cheating conditions                   #
    condition_1 = first_index == second_index
    condition_2 = first_index < 0 or first_index > len(elements_list) - 1
    condition_3 = second_index < 0 or second_index > len(elements_list) - 1
    #                       Cheating                               #
    if condition_1 or condition_2 or condition_3:
        first_half = elements_list[:int(len(elements_list)/2)]
        second_half = elements_list[int(len(elements_list)/2):]
        penalty_list = [f"-{moves_counter}a", f"-{moves_counter}a"]
        elements_list = first_half + penalty_list + second_half
        print("Invalid input! Adding additional elements to the board")
    #                       Not cheating                            #
    else:
        if elements_list[first_index] == elements_list[second_index]:
            print(f"Congrats! You have found matching elements - {elements_list[first_index]}!")
            elements_list[first_index] = ""
            elements_list[second_index] = ""
            while "" in elements_list:
                elements_list.remove("")

        else:
            print("Try again!")
