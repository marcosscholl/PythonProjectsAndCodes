.QWidget {
   background-color: blue;
background-image: url(:/backgroundImage/CockpitBackground.png);

}

/* Nice Windows-XP-style password character. */
QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}

/* We provide a min-width and min-height for push buttons
   so that they look elegant regardless of the width of the text. */
QPushButton {
    background-color: palegoldenrod;
    border-width: 2px;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 5;
    padding: 3px;
    min-width: 9ex;
    min-height: 2.5ex;
}

QPushButton:hover {
   background-color: khaki;
}

/* Increase the padding, so the text is shifted when the button is
   pressed. */
QPushButton:pressed {
    padding-left: 5px;
    padding-top: 5px;
    background-color: #d0d67c;
}

QLabel, QAbstractButton {
    font: bold;
}

/* Mark mandatory fields with a brownish color. */
.mandatory {
    color: brown;
}

/* Bold text on status bar looks awful. */
QStatusBar QLabel {
   font: normal;
}

QStatusBar::item {
    border-width: 1;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 2;
}

QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {
    background-color: cornsilk;
    selection-color: #0a214c; 
    selection-background-color: #C19A6B;
}

QListView {
    show-decoration-selected: 1;
}

QListView::item:hover {
    background-color: wheat;
}

/* We reserve 1 pixel space in padding. When we get the focus,
   we kill the padding and enlarge the border. This makes the items
   glow. */
QLineEdit, QFrame {
    border-width: 2px;
    padding: 1px;
    border-style: solid;
    border-color: darkkhaki;
    border-radius: 5px;
}

/* As mentioned above, eliminate the padding and increase the border. */
QLineEdit:focus, QFrame:focus {
    border-width: 3px;
    padding: 0px;
}

/* A QLabel is a QFrame ... */
QLabel {
    border: none;
    padding: 0;
    background: none;
}

/* A QToolTip is a QLabel ... */
QToolTip {
    border: 2px solid darkkhaki;
    padding: 5px;
    border-radius: 3px;
    opacity: 200;
}

/* Nice to have the background color change when hovered. */
QRadioButton:hover, QCheckBox:hover {
    background-color: wheat;
}

/* Force the dialog's buttons to follow the Windows guidelines. */
QDialogButtonBox {
    button-layout: 0;
}


