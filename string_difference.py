list_list = [[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]

set_list = []

card_dict_list = []
for card in list_list:
    card_dict = {}
    for c in card:
        if c not in card_dict.keys():
            card_dict[c] = 1
        else:
            card_dict[c] = card_dict[c] + 1
            
    card_dict_list.append(card_dict)


card = 0  
for card_dict in card_dict_list:
    for k,v in card_dict.items():
        if v <= 1:
            if k > card:
                card = k


print(card)