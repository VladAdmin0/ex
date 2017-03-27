from datetime import datetime, date, time

history = open('history.txt', 'a+')
incoming = open('incoming.txt', 'a+')
Mes = {}


class WriteInFile(object):

    def winf(self):
        id = 'id123456'
        history = open('history.txt', 'a+')
        incoming = open('incoming.txt', 'a+')
        word = input('Введите сообщение')
        Mes[id] = [word, datetime.now()]
        #         Mes[id] = [datetime.now(), word]
        # Mes[15][0] = 'yes'
        for id, words in Mes.items():

            h = str(id) + "\t" + words[0] + "\t" + datetime.strftime(words[1], "%Y.%m.%d %H:%M:%S") + "\n"
            history.write(h)
            i = words[0] + "\t" + datetime.strftime(words[1], "%Y.%m.%d %H:%M:%S") + "\n"
            incoming.write(i)
            incoming.close()
            history.close()


def print_message(message):
    print(str(message['id']), message['text'], str(message['date']))

def test():
    a = {}
    a['id'] = 12
    a['text'] = 'test'
    a['date'] = 'today'

    b = {'id':12, 'text':'test', 'date':'today'}
    list = [a,b]

    print_message(b)




class ReadFile(object):

    def rf_incom(self):
        incoming = open('incoming.txt')
        print(incoming.read())
        incoming = open('incoming.txt', 'w')


    def rf_hist(self):
        history = open('history.txt')
        print(history.read())



class IntractMenu(object):

    def menu(self):
        new_numb = None
        while new_numb != "0":
            print("""
            Меню выбора:

            0 - выход
            1 - Прочитать новые сообщения
            2 - Прочитать историю
            3 - Отправить сообщение
            """)

            # Выход
            new_numb = input("Выберите пункт: ")
            if new_numb == "0":
                print("выход")

            # Прочитать новые сообщения
            elif new_numb == "1":
                rf.rf_incom()

            # Прочитать историю
            elif new_numb == "2":
                rf.rf_hist()

            # Отправить сообщение
            elif new_numb == "3":
                wif.winf()

            # Не верный ввод меню
            else:
                print("\nИзвините, но", new_numb, "отсутсвует в меню выбора.")


wif = WriteInFile()
rf = ReadFile()
begin = IntractMenu()

begin.menu()

