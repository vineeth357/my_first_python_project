# Write your code here
import sqlite3
import random

conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
command = """CREATE TABLE IF NOT EXISTS card(
                    id INTEGER,
                    number TEXT,
                    pin TEXT,
                    balance INTEGER DEFAULT 0
                    ); """
cur.execute(command)
conn.commit()


class Account:
    num_accs = 0

    def create():
        connection = sqlite3.connect("card.s3db")
        crsr = connection.cursor()
        while 1:

            acc_num = random.randint(0, 999999999)
            acc_num = '400000' + '0' * (9 - len(str(acc_num))) + str(acc_num)
            acc_num_lst = list(acc_num)
            count = 0
            sum_ = 0
            for i in range(len(acc_num)):
                count += 1
                if count % 2 == 1:
                    acc_num_lst[i] = int(acc_num_lst[i]) * 2
                    if acc_num_lst[i] > 9:
                        acc_num_lst[i] = acc_num_lst[i] - 9
                sum_ += int(acc_num_lst[i])
            acc_num = acc_num + str(10 - sum_ % 10)[-1]
            command = """SELECT number FROM card WHERE number = ?;"""
            crsr.execute(command, (acc_num,))
            ans = crsr.fetchall()
            if len(ans) == 0:
                password = str(random.randint(0, 9999))
                if len(password) < 4:
                    password = '0' * (4 - len(password)) + password
                command = """INSERT INTO card (id,number,pin,balance) VALUES(?,?,?,0)"""
                crsr.execute(command, (Account.num_accs + 1, acc_num, password))
                Account.num_accs += 1
                print('Your card has been created')
                print('Your card number:\n{}'.format(acc_num))
                print('Your card PIN:\n{}'.format(password))

                break
        connection.commit()
        connection.close()

    def login():
        conn = sqlite3.connect("card.s3db")
        cur = conn.cursor()
        card_num = input('Enter your card number:')
        pin = input('Enter your PIN:')
        command = """SELECT number,pin FROM card WHERE number = ? AND pin = ?;"""
        cur.execute(command, (card_num, pin))
        ans = cur.fetchall()
        if (card_num, pin) in ans:
            print('You have successfully logged in!\n')
            while (1):

                option = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')

                if option == '1':
                    command = """SELECT balance FROM card WHERE number = ? ;"""
                    cur.execute(command, (card_num,))
                    ans = cur.fetchall()
                    print('Balance: {}'.format(ans[0][0]))

                elif option == '2':
                    add_income = int(input('Enter income:'))

                    sql_command = """UPDATE card SET balance = balance + ? WHERE number = ? ;"""
                    cur.execute(sql_command, (add_income, card_num))
                    conn.commit()
                    print('Income was added!')

                elif option == '3':
                    transfer_acc = input('Transfer\nEnter card number:')
                    if card_num == transfer_acc:
                        print("You can't transfer money to the same account!")

                    else:
                        acc_num_lst = list(transfer_acc)
                        count = 0
                        sum_ = 0
                        for i in range(len(transfer_acc)):
                            count += 1
                            if count % 2 == 1:
                                acc_num_lst[i] = int(acc_num_lst[i]) * 2
                                if acc_num_lst[i] > 9:
                                    acc_num_lst[i] = acc_num_lst[i] - 9
                            sum_ += int(acc_num_lst[i])
                        if (sum_ % 10) != 0:
                            print('Probably you made mistake in the card number. Please try again!')
                        else:
                            command = """SELECT number FROM card WHERE number = ? ;"""
                            cur.execute(command, (transfer_acc,))
                            ans = cur.fetchall()

                            if len(ans) == 1:
                                transfer_income = int(input('Enter how much money you want to transfer:'))
                                command = """SELECT balance FROM card  WHERE number = ? ;"""
                                cur.execute(command, (card_num,))
                                balance_acc_num = cur.fetchall()
                                if transfer_income < balance_acc_num[0][0]:
                                    command = """UPDATE card SET balance = balance + ? WHERE number = ? ;"""
                                    cur.execute(command, (transfer_income, transfer_acc))
                                    command = """UPDATE card SET balance = balance - ? WHERE number = ? ;"""
                                    cur.execute(command, (transfer_income, card_num))
                                    conn.commit()
                                    print('Success!')

                                else:
                                    print('Not enough money!')

                            else:
                                print('Such a card does not exist.')

                elif option == '4':
                    command = """DELETE FROM card WHERE number = ?"""
                    cur.execute(command, (card_num,))
                    conn.commit()
                    print('The account has been closed!')
                    break

                elif option == '5':
                    print('You have successfully logged out!')
                    break


                elif option == '0':
                    print('Bye!')
                    exit()


        else:
            print('Wrong card number or PIN!')
        conn.commit()
        conn.close()


while 1:
    option = input('1. Create an account\n2. Log into account\n0. Exit')
    if option == '1':
        Account.create()
    elif option == '2':
        Account.login()
    elif option == '0':
        exit()
    else:
        print('Error Occured!!')
