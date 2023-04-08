"""
Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt)
та повертає їх у вигляді списку рядків (назви повертати без крапки).
"""
def domainsToRows(filename):
    with open(filename, mode='r') as reader:
        domains = [line.strip() for line in reader]
        domains = [domain.replace('.', '') for domain in domains]
        return domains

domains = domainsToRows("domains.txt")
for domain in domains:
    print(domain)


"""
 Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
  Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і запистаи туди дані
"""

def get_surnames(filename2):
    surnames_list = []
    with open(filename2, mode='r') as reader:
        for line in reader:
            fields = line.strip().split(' ')
            surname = fields[1]
            surnames_list.append(surname)
        return surnames_list

surname_list = get_surnames("names.txt")
print(surname_list)

