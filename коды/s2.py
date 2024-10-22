def add_expense():
    description = input("Назначение расходов: ")
    amount = input("Сумма расходов: ")
    with open('s2.txt', 'a', encoding='utf-8') as file:
        file.write(f'{description}: {amount}\n')
def show_expenses():
    print("Записи расходов:")
    with open('s2.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
while True:
    action = input("Введите 'добавить' для добавления расхода или 'показать' для вывода всех расходов: ").strip()
    if action.lower() == 'добавить':
        add_expense()
    elif action.lower() == 'показать':
        show_expenses()
    else:
        print("Неверный ввод. Попробуйте снова.")