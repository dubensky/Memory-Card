from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
    QPushButton, QHBoxLayout,
    QVBoxLayout, QLabel,
    QMessageBox, QRadioButton,
    QGroupBox, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, correct_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии?','Португальский','Бразильский','Английский','Испанский'))
questions_list.append(Question('Какого цвета нет ни на одном флаге?','Фиолетового','Чёрного','Голубого','Все есть'))
questions_list.append(Question('Каспийское море это озеро?','Да','Точно не известно','Учёные спорят','Это море'))
questions_list.append(Question('Самая большая страна на данный момент?','Российская Федерация','Китай','США','Канада'))
questions_list.append(Question('Государственный язык Великобритании?','Английский','Британский','Шведский','Мнения расходятся'))
questions_list.append(Question('Сколько существует океанов?','4','5','6','3'))
questions_list.append(Question('Граница между Азией и Европой?','Уральские горы','Каспийское море','Азербайджан','Казахстан'))
questions_list.append(Question('Самое солёное море?','Чёрное','Нет','Скучно','Затрудняюсь ответить'))
questions_list.append(Question('Тебе нравится мой опрос?','Он лучший','Нет','Скучно','Затрудняюсь ответить'))
questions_list.append(Question('Тебе нравится мой опрос?','Он лучший','Нет','Скучно','Затрудняюсь ответить'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400,300)
lb_Question = QLabel('Здесь будет вопрос:')
btn_OK = QPushButton('Ответить')
window.score = 0
window.total = 0

RadioGroupBox = QGroupBox('Варианты ответов:')
buttons = QButtonGroup()
rbtn_1 = QRadioButton('Вариант ответа')
rbtn_2 = QRadioButton('Вариант ответа')
rbtn_3 = QRadioButton('Вариант ответа')
rbtn_4 = QRadioButton('Вариант ответа')
buttons.addButton(rbtn_1)
buttons.addButton(rbtn_2)
buttons.addButton(rbtn_3)
buttons.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox()
lb_Result = QLabel('Верно\неверно')
lb_Correct = QLabel('Верный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 3)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
window.setLayout(layout_card)

def click_ok():
    if btn_OK.text() == 'Следующий вопрос':
        show_question()
    else:
        check_answer()

def show_correct():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    AnsGroupBox.setTitle('Результат теста')

def check_answer():
    if answers[0].isChecked():
        lb_Result.setText('Правильно!')
        show_correct()
        window.score += 1
        print('Статистика\n-Всего вопросов: ' + str(window.total) + '\n-Правильных ответов: ' + str(window.score))
        print('Рейтинг: ' + str(window.score/window.total*100) + '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            lb_Result.setText('Неверно!')
            show_correct()
            print('Рейтинг: ' + str(window.score/window.total*100) + '%')

def show_question():
    buttons.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    buttons.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    next_question()

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ' + str(window.total) + '\n-Правильных ответов: ' + str(window.score))
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def ask(q: Question):
    shuffle(answers)
    lb_Question.setText(q.question)
    answers[0].setText(q.correct_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.correct_answer)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
AnsGroupBox.hide()
btn_OK.clicked.connect(click_ok)
next_question()
window.show()
app.exec_()