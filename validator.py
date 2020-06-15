from PyQt5 import QtGui as qtg
import string


class IPV4Validator(qtg.QValidator):
    def validate(self, a0: str, a1: int):
        octets = a0.split('.')
        if len(octets) > 4:
            state = qtg.QValidator.Invalid
        elif not all([x.isdigit() for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        elif not all([0<=int(x)<=255 for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        elif len(octets) < 4:
            state = qtg.QValidator.Intermediate
        elif any([x == '' for x in octets]):
            state = qtg.QValidator.Intermediate
        else:
            state = qtg.QValidator.Acceptable
        return (state, a0, a1)

