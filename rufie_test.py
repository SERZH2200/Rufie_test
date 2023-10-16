from PyQt5.QtCore import QTimerEvent, Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit
app = QApplication([])


class MainWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = 'Здоровье'
        self.txt_hello = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
        self.instruction = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        self.setWindowTitle(self.title)
        self.button = QPushButton('Начать')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_hello)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
        self.resize(1000, 800)
        self.show()
        self.button.clicked.connect(self.next)
    
    def next(self):
        self.hide()
        self.second_window = SecWin()
class SecWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.name_and_surname = QLineEdit()
        self.hintage = QLineEdit()
        self.hinttest1 = QLineEdit()
        self.hinttest2 = QLineEdit()
        self.hinttest3 = QLineEdit()
        
        self.flag1 = True
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.hinttest1.setEnabled(False)
        self.hinttest2.setEnabled(False)
        self.hinttest3.setEnabled(False)
        self.timer = QLabel('00:00:' + '00')
        self.timer.setFont(QFont('Times New Roman', 36, QFont.Bold))
        self.timer.setStyleSheet('color: rgb(0, 0, 0)')
        self.title = 'Здоровье'
        self.name_txt = QLabel('Введите Ф.И.О.:')
        self.ages = QLabel('Полных лет:')
        self.pre_exercise = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\n'
                               'Результат запишите в соответствующее поле.')
        self.first_test = QPushButton('Начать первый тест')
        self.start_exercise = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\n'
                                     'чтобы запустить счетчик приседаний.')
        self.squats = QPushButton('Начать делать приседания')
        self.result = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\n'
                             'Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.\n'
                             'Зелёным обозначены секунды, в течение которых необходимо \n'
                             'проводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.final_test = QPushButton('Начать финальный тест')
        self.send_results = QPushButton('Отправить результаты')
        self.main_layout = QHBoxLayout()
        self.v_line1 = QVBoxLayout()
        self.timer_line = QVBoxLayout()
        self.setWindowTitle(self.title)
        self.v_line1.addWidget(self.name_txt)
        self.v_line1.addWidget(self.name_and_surname)
        self.v_line1.addWidget(self.ages)
        self.v_line1.addWidget(self.hintage)
        self.v_line1.addWidget(self.pre_exercise)
        self.v_line1.addWidget(self.first_test)
        self.v_line1.addWidget(self.hinttest1)
        self.v_line1.addWidget(self.start_exercise)
        self.v_line1.addWidget(self.squats)
        self.v_line1.addWidget(self.hinttest2)
        self.v_line1.addWidget(self.result)
        self.v_line1.addWidget(self.final_test)
        self.v_line1.addWidget(self.hinttest3)
        self.v_line1.addWidget(self.send_results, alignment = Qt.AlignCenter)
        self.timer_line.addWidget(self.timer)
        self.main_layout.addLayout(self.v_line1)
        self.main_layout.addLayout(self.timer_line)
        self.setLayout(self.main_layout)
        self.resize(1000, 800)
        self.show()
        self.send_results.clicked.connect(self.next)
        self.first_test.clicked.connect(self.timer_test)
        self.squats.clicked.connect(self.second_timer_test)
        self.final_test.clicked.connect(self.third_timer_test)
        self.settings_btn()
    def next(self):
        try:
            self.username = self.name_and_surname.text()
            self.userage = self.hintage.text()
            self.p1 = self.hinttest1.text()
            self.p2 = self.hinttest2.text()
            self.p3 = self.hinttest3.text()
            self.index = round(((4 * (int(self.p1) + int(self.p2) + int(self.p3))) - 200) / 10, 1)
            self.hide()
            self.third_window = ThirdWin()
        except:
            self.name_txt.setText('Введите Ф.И.О.:                     ERROR! ПРОВЕРЬТЕ ПРАВИЛЬНОСТЬ ДАННЫХ')
            self.name_and_surname.setEnabled(True)
            self.hintage.setEnabled(True)
            self.hinttest1.setEnabled(True)
            self.hinttest2.setEnabled(True)
            self.hinttest3.setEnabled(True)
            self.final_test.setEnabled(False)
    def settings_btn(self):
        self.first_test.setEnabled(self.flag1)
        self.squats.setEnabled(self.flag2)
        self.final_test.setEnabled(self.flag3)
        self.send_results.setEnabled(self.flag4)
    def timer_test(self):
        global time
        self.name_and_surname.setEnabled(False)
        self.hintage.setEnabled(False)
        self.username = self.name_and_surname.text()
        self.userage = self.hintage.text()
        print(self.username, self.userage)
        time = QTime(0, 0, 3)
        self.q_timer = QTimer()
        self.q_timer.timeout.connect(self.timer1Event)
        self.q_timer.start(1000)
    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setStyleSheet('color: rgb(0, 0, 0)')
        if int(time.toString('hh:mm:ss')[6:8]) == 0:
            self.hinttest1.setEnabled(True)
            self.flag1 = False
            self.flag2 = True
            self.q_timer.stop()
            self.settings_btn()
    #Закончили таймер, сделали флаги кнопок почти до конца
    #Осталась формула Руфье
    def second_timer_test(self):
        global time
        time = QTime(0, 0, 3)
        self.q_timer = QTimer()
        self.hinttest1.setEnabled(False)
        self.p1 = self.hinttest1.text()
        self.q_timer.timeout.connect(self.timer2Event)
        self.q_timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss")[6:8])
        self.timer.setStyleSheet('color: rgb(0, 0, 0)')
        if int(time.toString('hh:mm:ss')[6:8]) == 0:
            self.flag2 = False
            self.flag3 = True
            self.q_timer.stop()
            self.hinttest2.setEnabled(True)
            self.settings_btn()
    def third_timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.hinttest2.setEnabled(False)
        self.p2 = self.hinttest2.text()
        self.q_timer = QTimer()
        self.q_timer.timeout.connect(self.timer3Event)
        self.q_timer.start(100)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString('hh:mm:ss')[6:8]) == 0:
            self.hinttest3.setEnabled(True)
            self.flag4 = True
            self.q_timer.stop()
            self.settings_btn()
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.timer.setStyleSheet('color: rgb(255, 0, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.timer.setStyleSheet('color: rgb(0, 0, 0)')
class ThirdWin(QWidget):
    def __init__(self):
        txt_res1 = "низкая. Срочно обратитесь к врачу!"
        txt_res2 = "удовлетворительная. Обратитесь к врачу!"
        txt_res3 = "средняя. Возможно, стоит дополнительно обследоваться у врача."
        txt_res4 = "выше среднего"
        txt_res5 = "высокая"
        QWidget.__init__(self)
        ind = window.second_window.index
        self.index = QLabel('Индекс Руфье: ' + str(window.second_window.index))
        if int(window.second_window.userage) >= 15:
            if ind >= 15:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res1)
            elif 11 <= ind <= 14.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res2)
            elif 6 <= ind <= 10.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res3)
            elif 0.5 <= ind <= 5.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res4)
            else:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res5)
        elif int(window.second_window.userage) in (13,14):
            if ind >= 16.5:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res1)
            elif 12.5 <= ind <= 16.4:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res2)
            elif 7.5 <= ind <= 12.4:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res3)
            elif 2 <= ind <= 7.4:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res4)
            else:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res5)
        elif int(window.second_window.userage) in (11,12):
            if ind >= 18:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res1)
            elif 14 <= ind <= 17.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res2)
            elif 9 <= ind <= 13.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res3)
            elif 3.5 <= ind <= 8.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res4)
            else:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res5)
        elif int(window.second_window.userage) in (9,10):
            if ind >= 19.5:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res1)
            elif 15.5 <= ind <= 19.4:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res2)
            elif 10.5 <= ind <= 15.4:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res3)
            elif 5 <= ind <= 10.4:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res4)
            else:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res5)
        elif int(window.second_window.userage) in (7,8):
            if ind >= 21:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res1)
            elif 17 <= ind <= 20.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res2)
            elif 12 <= ind <= 16.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res3)
            elif 6.5 <= ind <= 11.9:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res4)
            else:
                self.heart = QLabel('Работоспособность сердца: ' + txt_res5)
            #Доделали таймер, вычислили индекс, начали условие
            #Осталось дописать условия для оценки работоспособности сердца
        self.v_line = QVBoxLayout()
        self.setWindowTitle('Результаты')
        self.v_line.addWidget(self.index, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.heart, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
        self.resize(1000, 800)
        self.show()
window = MainWin()
app.exec_()