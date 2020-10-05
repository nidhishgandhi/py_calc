from functools import partial
ERROR_MSG = 'ERROR'

class Controller:
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view 	   = view
        # Connect signals and slots
        self._connectSignals()

   
    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)