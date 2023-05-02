note_base = []
while True:


    user_input = input("\n\tadd - додати нотатку\n\t"
                       "earliest - вивeсти збережені нотатки у хронологічному порядку - від найстарішої до найновішої\n\t"
                       "latest - вивecти збережені нотатки у хронологічному порядку - від найновішої до найстарішої\n\t"
                       "longest - вивeсти збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої\n\t"
                       "shortest - вивести збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої\n\t"
                       "Exit - вихід\n"
                       )

    if user_input == 'add':
        new_note = input('Введіть нотатку: ')
        note_base.insert(0, new_note)

    elif user_input == 'earliest':
                print(sorted(note_base, reverse=False))

    elif user_input == 'latest':
                print(sorted(note_base, reverse=True))

    elif user_input == 'longest':
        note_base.sort(key=len, reverse=True)
        print(note_base)

    elif user_input == 'shortest':
        note_base.sort(key=len, reverse=False)
        print(note_base)

    elif user_input == 'Exit':
        break

    else:
        print('Доступні тільки такі команди як:')