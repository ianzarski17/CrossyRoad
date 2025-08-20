PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt") as names_data:
    names_list = names_data.readlines()
with open("./Input/Letters/starting_letter.txt") as draft_mail:
    draft = draft_mail.read()
    for name in names_list:
        stripped_name = name.strip()
        new_mail = draft.replace(PLACEHOLDER, stripped_name)
        print(new_mail)
        for _ in names_list:
            with open(f"./Output/ReadyToSend/{stripped_name}'s_mail.doc", mode='w') as folder:
                folder.write(new_mail)



