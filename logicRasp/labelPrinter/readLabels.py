import csv
import queue

schema = ['ICC', 'ULTIMO', 'MIN', 'CAJA', 'BOX', 'LOTE']


class ReadLables:
    def __init__(self, filename):
        """Need file to read label data
        The file have:
        'ICC', 'ULTIMO', 'MIN', 'CAJA', 'BOX', 'LOTE'

        Args:
            filename (str): path file csv
        """
        self.filename = filename
        self.__readFile = queue.Queue()
        self.datas = None
        self.__readCSV()

    def __readCSV(self):
        """Read CSV file and create one Queue with dictionary
        """
        with open(self.filename, mode='r', newline='') as f:
            self.datas = list(csv.DictReader(f, fieldnames=schema))

            for contRow in range(1, len(self.datas)):
                self.__readFile.put(self.datas[contRow])

    def getlabel(self):
        """Read label and deleted of the queue

        Returns:
            [dict]: data of the label
        """
        return self.__readFile.get()

    def countLabels(self):
        return self.__readFile.qsize()

    def templateLabel(self, template, labelData, fieldsLabel):
        """Return label template in .npr format and delete
        the data label of the queue

        Args:
            template (str): template in .pnr fotmat
            labelData (dict): label data to replace in template
            fieldLabels (dict): dictionary of fields of teh template to replace
            (field Csv: field in template (ex:<icc>))

        Returns:
            str: template with data of the label of the queue, in format .prn
        """

        for key, value in fieldsLabel.items():
            template = template.replace(value, labelData[key])

        return template

    def searchLabel(self, ICC):
        """Search icc from csv file

        Args:
            ICC ([type]): [description]

        Returns:
            [dict]: dictionary with data of label
        """
        for data in self.datas:
            if ICC == data['ICC']:
                return data
        return 'None'


if __name__ == '__main__':
    from zebraPrinter import ZebraPrinter
    rcvs = ReadLables('sims.csv')
    template = (
        'CT~~CD,~CC^~CT~'
        '^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
        '^XA'
        '^MMT'
        '^PW240'
        '^LL0120'
        '^LS0'
        '^FT19,35^A0N,22,21^FH\^FD<icc>^FS'
        '^FT145,34^A0N,28,28^FH\^FD<ultimo>^FS'
        '^BY1,3,24^FT58,67^BCN,,Y,N'
        '^FD>:#CEL:>5<min>^FS'
        '^FT13,57^A0N,14,14^FH\^FDLOTE:^FS'
        '^FT15,73^A0N,15,14^FH\^FD<lote>^FS'
        '^FT31,108^A0N,17,16^FH\^FDCaja:^FS'
        '^FT66,108^A0N,17,16^FH\^FD<caja>^FS'
        '^FT150,108^A0N,17,16^FH\^FDBOX:^FS'
        '^FT185,108^A0N,17,16^FH\^FD<box>^FS'
        '^PQ1,0,1,Y^XZ'
    )

    fieldsLable = {
        'ICC': '<icc>',
        'ULTIMO': '<ultimo>',
        'MIN': '<min>',
        'CAJA': '<caja>',
        'BOX': '<box>',
        'LOTE': '<lote>',
    }

    zprint = ZebraPrinter()

    for i in range(rcvs.countLabels()):
        data = rcvs.getlabel()
        templatePrn = rcvs.templateLabel(
            template=template,
            labelData=data,
            fieldsLabel=fieldsLable
        )

        zprint.printLabel(str.encode(templatePrn))
