while True:
    action = input('Enter tail or head or exit from program: \n')
    if action == 'tail' or action == 'head':
        with open('files/1_coin_flip.txt', 'r') as file:
            throw_list = file.readlines()
        throw_list.append(action + '\n')
        with open('files/1_coin_flip.txt', 'w') as file:
            file.writelines(throw_list)
        counter_head = throw_list.count('head\n')
        percentage = counter_head / len(throw_list) * 100
        percentage = round(percentage, 2)
        print(f'Head percentage: {percentage}')
    elif action == 'exit':
        print(f'You have made {len(throw_list)} throws')
        print(f'Percentage of getting a "head" = {percentage}%')
        break
    else:
        print('Unknown command')
