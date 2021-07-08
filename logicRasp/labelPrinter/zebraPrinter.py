from zebra import Zebra

class ZebraPrinter:
    def __init__(self):
        self.zebraPrinter = Zebra(['etieueta'])

    def getPrinterList(self):
        return self.zebraPrinter.getqueues()

    def configPrinter(self, direct_thermal=None, label_height=None, label_width=None):
        self.zebraPrinter.setup(direct_thermal,label_height,label_width)

    def resetDefaultPrinter(self):
        self.zebraPrinter.reset_default()

    def resetPrinter(self):
        self.zebraPrinter.reset()

    def autoSense(self):
        self.zebraPrinter.autosense()

    def printLabel(self,command):
        self.zebraPrinter.output(command, encoding=None)

if __name__ == '__main__':
    z = ZebraPrinter()
    z.getPrinterList()
    lb2 = b'CT~~CD,~CC^~CT~^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ^XA^MMT^PW240^LL0104^LS0^BY1,3,21^FT39,59^BCN,,Y,N^FD>;123456789012^FS^PQ1,0,1,Y^XZ'
    lb3 = (b'CT~~CD,~CC^~CT~'
            b'              ^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
            b'^XA'
            b'^MMT'
            b'^PW240'
            b'^LL0104'
            b'^LS0'
            b'^BY1,3,21^FT13,36^BCN,,Y,N'
            b'^FD>;123456789012^FS'
            b'^FT17,82^A0N,28,28^FH\^FDTexto de  Prueba^FS'
            b'^PQ1,0,1,Y^XZ'
                    )
    lb4 = (b'CT~~CD,~CC^~CT~'
            b'^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
            b'^XA'
            b'^MMT'
            b'^PW240'
            b'^LL0104'
            b'^LS0'
            b'^FO0,0^GFA,02048,02048,00016,:Z64:'
            b'eJztlM1q20AUhe22xpBCWy9EXieLimw7xJdZDXmGLIxXoXkeCaq9Bb3dmL5ABm+iF5BAJgtvRjDTO79yXYdCu2xPyAzi+Jsz50bOZPK3uihGPdDzrBn1jZ7fm1H2eb4edXXG/x0/W1mBW1/kJcBPfFGUKZ+vOWTAOO2Rb41R1RGfi0bmR3wZfkP+MqN4Bilf2bM1Jl4KGw6Jd9mmSv2B2/I5j/0r53eJd3e3p3heofNVzAdffgkhX/nyXzHw0ueLyHfuAIUY+ufcdqcBhP57d4EO94GHnST8e7MNPA4D+YhdyM/4M6xgLRl4Ho2m+vSxwIvdLc3v0EjP02AoeuiCP19xfgmc33Dw+QSXncESteefxA4OQkDzJByvzLDRSg/RXwHPLuGOySVEHrHcJ5/yxbXcUgfP0+Wxa5F8dD4QD3dwAyHfjk9rk3jZPAopQErPzwc7YBx5BiQOjN6xq3C+Mfsx300fDnCUT9NX9ZhvdU/5kPLNUX8J9COvpXwEl+99aqA8v3Q8e85Sf13ZBpEnf2sDIPo40AuwQeIffD67J/9zBtFX9AJ0mmrG+91ugR/C/V7XdV2pDZa0e56+PCu2pjX8/SvTm1LvTXg/IKcDdjSd3PlvayJLY5fA5/YGlJ45/51udd+qvu+/aM8ziPL5m7reFLXdPO8HYDfHE9hbtX1/NN/Evzr9/wTgPzLz/kXbFq0VrXE+7vjsPD9l7NOC+cXxv55vGy5nL+RPF6Tpwm2TM/ybj6PO8ZMPo/6IP9Ep/1//kn4An1vUEw==:CBFF'
            b'^PQ1,0,1,Y^XZ'
            )

    javi = (
        b'CT~~CD,~CC^~CT~'
        b'^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
        b'^XA'
        b'^MMT'
        b'^PW240'
        b'^LL0104'
        b'^LS0'
        b'^FO0,0^GFA,02048,02048,00016,:Z64:'
        b'eJztlLFOwzAQhi+2IiIxhBeoYmVk6cqWPgIPgMQr9AEixWM3RtaoD5K2b5AHQCLq1DGjFVDhnGD7LJpUwAb8kh2dzt/9d5ETgF+hNE0n83IaF7jY9917lJ0tMNqE8B5ftx+cr20DvN+v7AHeOysbX2z1fmvteaMPKce3+lDr+FfcYmUHCHU8M3km+aYEVhH+EQ3ypQklf2iwPPHf1RDWxp8BX3cwb5R9AVzmkIDlMc5kJR0fytk2t3nky3jfsY7wQbv0eFCCzi/hzs2vechKkkclQHg9fYP5yMVBTfxxcN4xj4fc54H2Pxg4fy06f99j6/NM3XgxGjh/BFm1dvximMDqMExgm38CcwmGCm8lQNY4vlhAUNi0hPkBLo+kHl6AsLaRwALrzZ5+Qfe7Aqjil6MXB88O17Z9B/QDSsBX9LFOyXBiJG/urRzLC6/MZ0VkP9mARtmo/XlpdhKPVqvpAj/4e/3rD+sdf/ZbKw==:334D'
        b'^FT129,71^A0N,45,45^FH\^FDJavi^FS'
        b'^PQ1,0,1,Y^XZ')


    nico = (
        b'CT~~CD,~CC^~CT~'
        b'^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
        b'^XA'
        b'^MMT'
        b'^PW240'
        b'^LL0104'
        b'^LS0'
        b'^FO0,0^GFA,02048,02048,00016,:Z64:'
        b'eJztUzFOw0AQXMeyjIhE0tAR+QQlRXoKnI+gfIEPRPZTXNLxhJgf5AFBiagiqhQUluVk2bvdPfvoaRAn2+vReXZ29rwAf20ZfRlxmCqOOFwovuRwozjh8FgKnnPIdF9eJnvBZ/4wqyX9jmPecrxDoXUcU8ET4U3OjGenMOZYuepR+bhx6QvlY2NDjKq/27r026XwX8/GVn/ODe+/OWJ2LCRfiZaIB9WvV9bBql4Jv7IOYqxy+b7Ovlz1wp+UtnK6vf/knZ4bUP2KuGbdgOdDwZfyYd3EVIPXh1kXkXmvT7XHtNnzSfwZBnxivwT9X1oHXh9IgLyrf2cePD8rpfeib88/sb0X/QeIrQOvP4V0H1H5ynd/AB68vvNOl+obyBtyYJTv1O3h9/wDDPyTem3br/rU+4pO/6PnS45iiPv+80q3qs/rjs7PDDA5yIb75OAqwLNjEuB5Gwc4PUUBjrEMcLSr+WX0ST0w5hb3svHlHUjlpRvCvGGcnBYuPsmcjPETRreUX+YoQpcgxaNW7ozPeUxsYqe8fNdK7rE15J8ekqDohnT6OyhB7ukA1ydqftdbGWPr1SVBykOoCXAduE93PIN9Bb06J8B6uA/rH81LugBC3IYYFvC//tcvrG9gIM+I:CA70'
        b'^FT101,66^A0N,28,28^FH\^FDLos NENES^FS'
        b'^PQ1,0,1,Y^XZ'
    )

    for i in range(2):
        z.printLabel(javi)
    
    for i in range(2):
        z.printLabel(nico)

    

