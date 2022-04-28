import os
import __init__ as pytchart


def demo1():
    pytchart.box(310, 5, 'yellow', (-160, -130))
    pytchart.bargraph('light green', startcoor=(-50, 0))
    pytchart.histogram('light pink', startcoor=(-150, -2))
    pytchart.linegraph(times=3, startcoor=(-50, 0))
    pytchart.texttag('Things I think about', 'light pink', ('Arial', 12, 'bold'), (0, -100))
    pytchart.texttag('Green - programming    Blue - Nintendo    Pink - Other', 'light green', ('Arial', 9, 'normal'), (0, 150))
    pytchart.savechart('thisisanexample')
    pytchart.screenloop()


def demo2():
    pytchart.box(450, 5, 'light green', (-80, -200))  
    pytchart.texttag('Line graph made by pytchart', 'light pink', ('Arial', 15, 'bold'), (150, 200))
    pytchart.texttag('$10000 ---', 'light blue', ('Arial', 15, 'normal'), (-30, 100))
    pytchart.texttag('$10 ---', 'light blue', ('Arial', 15, 'normal'), (-30, -100))
    pytchart.linegraph('light blue', 0.070, 10, 1000, 10, 10, (-80, -200))
    pytchart.linegraph('light green', 0.070, 10, 1000, 10, 10, (-80, -200))
    pytchart.linegraph('light pink', 0.070, 10, 1000, 10, 10, (-80, -200))
    pytchart.savechart('thisisanexample')
    pytchart.screenloop()


def demo3():
    pytchart.box(310, 5, 'light green', (-160, -130))
    pytchart.bubblegraph(linelength=435, times=6, startcoor=(-160, -130))
    pytchart.bubblegraph(color='light pink', linelength=435, times=6, startcoor=(-160, -130))
    pytchart.texttag('My life', 'light pink', ('Arial', 20, 'bold'), (0, -100))
    pytchart.texttag('Blue - Eat    Pink - Other', 'light green', ('Arial', 13, 'normal'), (0, 150))
    pytchart.savechart('thisisanexample')
    pytchart.screenloop()


def demo4():
    pytchart.box(400, 5, 'light green', (-200, -130))
    pytchart.sidebargraph(pxperstep=0.40, startcoor=(-195, 100))
    pytchart.texttag('Money made by a company in ten days', 'light pink',
    ('Arial', 15, 'bold'), (5, 200))
    pytchart.savechart('thisisanexample')
    pytchart.screenloop()


def demo5():
    while True:
        pytchart.delay(3)
        pytchart.randomgraph('light pink', 0.07, 5, 1000, 10, 10, 510, (0, 0))
        pytchart.delay(3)
        pytchart.clearall()
        os.system('clear')
