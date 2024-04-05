## widgets

- QPushButton
- QLineEdit
- QComboBox
- QRadioButton

## layout managers

- QHBoxLayout
  - arranges widgets horizontall left to right
- QVBoxLayout
  - arranges vertically top to bottom
- QGridLayout
  - arranges widgets in a grid of row and columns
- QFormLayout
  - arranges widgets in a two-column layout

## dialogs

- provide additonal functionality settings for user

## main windows

- have a menu bar, some toolbars, and status bar, with centrla widget
- core functionality of an application

## applications

- manages applications control flow as well as main settings
- event handling mechanisms
- brains QApplication

event lopps

- GUI apps are event-driven

signals and slots

- event catchers
- signals need to be connected to slots to do stuff
- gives life to the applciation
- turns user evens into concrete actions

## key functionalities

1. user performs action on the view
2. view notifies the controller
3. controller queries the model for response
4. model processes the controller query and performs computations
5. controller recieve and update view user sees new view result

inside main(), the program does the following

1. creates a QApplicaion object named pycalcApp
2. create instance of app windows pycalWindow
3. show the GUI by calling show() on window object
4. run the application even loop with exec()
