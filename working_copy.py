from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle
 
app = QApplication([])
btn_OK = QPushButton('Answer') 
lb_Question = QLabel('The most difficult question in the world!')

#Radio group box
RadioGroupBox = QGroupBox("Answer options") 
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
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

#Answer group box
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('are you correct or not?')
lb_Correct = QLabel('the answer will be here!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

#Result Group Box
ResGroupBox = QGroupBox("Final Results")
lb_total = QLabel('Total correct answers')
lb_percent = QLabel('Percent correct')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_total)
layout_res.addWidget(lb_percent)
ResGroupBox.setLayout(layout_res)
ResGroupBox.hide()
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line2.addWidget(ResGroupBox) #NEWWWWWWW
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')
 
def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

"""
def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer) 
    show_question() 
"""
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        window.total_correct += 1
        show_correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

def next_question(q):
    shuffle(answers)
    answers[0].setText(q['c'])
    answers[1].setText(q['w1'])
    answers[2].setText(q['w2'])
    answers[3].setText(q['w3'])
    lb_Question.setText(q['q'])
    lb_Correct.setText(q['c']) 
    show_question() 

#Adding questions to 
questions = []
q1 = {'q': 'What is the smallest animal?', 'c':'ant', 'w1': 'dog', 'w2': 'cat', 'w3': 'whale'}
questions.append(q1)
q2 = {'q': 'What is the largest animal?', 'c':'kitten', 'w1': 'bee', 'w2': 'telephone', 'w3': 'dinosaur'}
questions.append(q2)

shuffle(questions) #NEW


def click_button():
    if btn_OK.text() == 'Answer':
        check_answer()
    elif window.current == len(questions) - 1:
        #set the text for lb_total and lb_percent
        lb_total.setText('Total correct: ' + str(window.total_correct))
        lb_percent.setText('Percent correct')
        #show ResGroupBox and hide answer_group_box and radio_group_box
        radio_group_box.hide()
        answer_group_box.hide()
        ResGroupBox.show()
    else:
        window.current += 1
        if window.current >= len(questions):
            window.current = 0
        next_question(questions[window.current])

window = QWidget()
window.current = 0
window.total_correct = 0
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_button)  #NEW
next_question(questions[window.current])  #NEW
window.show()
app.exec()
