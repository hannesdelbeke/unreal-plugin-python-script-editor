"""
This is a debug script that can be run outside of unreal to test the UI.
"""

import sys
from PySide2 import QtWidgets



# mocking unreal allows us to run the UI outside of unreal,
# preventing an exception on `import unreal` in unrealScriptEditor
# run this before importing unrealScriptEditor
from unittest.mock import MagicMock
mock_unreal = MagicMock()
sys.modules["unreal"] = mock_unreal

import pprint
from unrealScriptEditor import startup
from unrealScriptEditor import main
pprint.pp(sys.path)

# handle QApplication correctly, PythonScriptEditor attempts this but doesn't do _exec()
APP = QtWidgets.QApplication.instance()
ex = False
if not APP:
    APP = QtWidgets.QApplication(sys.argv)
    ex = True

# show the script editor
global editor
editor = main.show()

# exec the app if we created it
if ex:
    APP.exec_()
