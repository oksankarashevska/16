from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from modules.app import app 

# Створюємо головне вікно
main_window = QMainWindow()
main_window.setWindowTitle("Counter")
main_window.setFixedSize(400, 500)

WIDTH_WINDOW = 400
HEIGHT_WINDOW = 500

# розміри 
primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()

main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

# Головний віджет
central_widget = QWidget()
main_window.setCentralWidget(central_widget)
main_window.setStyleSheet("background-color: #b04bd1;")

layout = QVBoxLayout(central_widget)
layout.setContentsMargins(20, 20, 20, 20)
layout.setSpacing(15)

# штучка для лічильника
counter = [0]

# треба зробити числа
label1 = QLabel(str(counter[0]))
label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
label1.setStyleSheet("color: white; font-size: 64px; font-weight: bold;")
layout.addWidget(label1)

# Стиль кнопок
button_style = """
    QPushButton {
        background-color: #d168d9;
        color: white;
        font-size: 18px;
        border-radius: 5px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #d14b81;
    }
"""

# кнопки + та -
def plus_click():
    counter[0] += 1  # (+1)
    label1.setText(str(counter[0]))

def minus_click():
    counter[0] -= 1  # (-1)
    label1.setText(str(counter[0]))

def reset_click():
    counter[0] = 0   # 0
    label1.setText(str(counter[0]))

# Кнопка "+"
plus = QPushButton("+")
plus.setStyleSheet(button_style)
plus.clicked.connect(plus_click)
layout.addWidget(plus)

# Кнопка "-"
minus = QPushButton("-")
minus.setStyleSheet(button_style)
minus.clicked.connect(minus_click)
layout.addWidget(minus)

# скидання до 0
reset = QPushButton("reset")
reset.setStyleSheet(button_style)
reset.clicked.connect(reset_click)
layout.addWidget(reset)

main_window.show()
    
    
    
    