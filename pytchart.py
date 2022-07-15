"""
  An easy and customizable chart-maker.
  Supposedly used to encourage people to code with no experience and to
  make a chart very customizable.
  No modules to manually install or complex function names to make the person 
  have fun.
  v0.1.2
"""


import turtle as __root
from random import randint as __rint
from time import sleep as delay
screen = __root.Screen()
screen.title('Pytchart')


def linegraph(datalist: list, color='light blue', pxperstep=0.070, linesize=5, startcoordinates=(0, 0)):
  """
  Generates a line graph (obviously).
  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line size of the chart's line. Defaults to 5.
      startcoordinates (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).
  """
  y = __root.Turtle('circle')
  y.hideturtle()
  y.pensize(linesize)
  y.penup()
  y.color(color)
  screen.tracer(25)
  y.goto(startcoordinates)
  y.lt(45)
  y.pendown()
  for data in datalist:
    y.fd(pxperstep * data)
    y.rt(45)
    y.fd(10)
    y.lt(45)
  
  
def bargraph(datalist: list, color='light blue', pxperstep=0.070, linesize=5, startcoordinates=(0, 0)):
  """
  Generates a bar graph (obviously).
  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line size of the graph's line. Defaults to 5.
      startcoordinates (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).
  """
  y = __root.Turtle('circle')
  y.pensize(linesize)
  y.color(color)
  screen.tracer(25)
  y.hideturtle()
  y.penup()
  y.goto(startcoordinates)
  y.lt(90)
  y.pendown()
  for data in datalist:
    y.fd(pxperstep * data)
    y.bk(pxperstep * data)
    y.penup()
    y.rt(90)
    y.fd(10)
    y.lt(90)
    y.pendown()
  
  
def histogram(datalist: list, color='light blue', pxperstep=0.070, linesize=5, startcoordinates=(0, 0)):
  """
  Generates a histogram (obviously).
  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line linesize of the graph's line. Defaults to 5.
      startcoordinates (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).
  """
  y = __root.Turtle('circle')
  y.pensize(linesize)
  y.color(color)
  screen.tracer(100)
  y.hideturtle()
  y.penup()
  y.goto(startcoordinates)
  y.lt(90)
  y.pendown()
  for data in datalist:
    y.fd(pxperstep * data)
    y.bk(pxperstep * data)
    y.rt(90)
    y.fd(2.5)
    y.lt(90)
  
  
def bubblegraph(datalist: list, color='light blue', pxperstep=0.070, linesize=5, linelength=510, startcoordinates=(0, 0)):
  """
  Generates a bubble graph (obviously).
  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line size of the graph's line. Defaults to 5.
      linelength (int, optional): The length of the line. Defaults to 510.
      startcoordinates (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).
  """
  y = __root.Turtle('circle')
  y.shape('circle')
  y.color(color)
  screen.tracer(25)
  y.penup()
  y.goto(startcoordinates)
  y.setheading(sum(datalist) / len(datalist) - 30)
  y.pendown()
  y.pensize(linesize)
  y.fd(linelength)
  y.bk(linelength)
  y.setheading(sum(datalist) / len(datalist))
  y.penup()
  for data in datalist:
    y.fd(pxperstep * data)
    y.stamp()
    y.rt(45)
    y.fd(10)
    y.lt(45)
  
  
def sidebargraph(datalist: list, color='light blue', pxperstep=0.70, linesize=8, startcoordinates=(0, 0)):
  """
  Generates a side bar graph (obviously) from the left to the right.
  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line linesize of the graph's line. Defaults to 5.
      high (int, optional): The highest number the chart's random generator goes. Defaults to 1000.
      low (int, optional): The lowest number the chart's random generator goes. Defaults to 10.
      times (int, optional): How many times it will draw lines in a chart. Defaults to 10.
      startcoordinates (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).
  """
  y = __root.Turtle('circle')
  y.hideturtle()
  y.pensize(linesize)
  y.color(color)
  screen.tracer(25)
  y.penup()
  y.goto(startcoordinates)
  y.pendown()
  for data in datalist:
    y.fd(pxperstep * data)
    y.bk(pxperstep * data)
    y.rt(90)
    y.penup()
    y.fd(20)
    y.lt(90)
    y.pendown()


def randomgraph(datalist: list, color: str, pxperstep: int or float, linesize: int or float, linelength: int or float, startcoordinates: tuple or list):
  """
  Generates a random kind of graph (obviously).
  Args:
      color (str): The color of the graph.
      pxperstep (int or float): How far the drawer moves per 1 step.
      linesize (int or float): The line linesize of the graph's line.
      high (int or float): The highest number the chart's random generator goes.
      low (int or float): The lowest number the chart's random generator goes.
      times (int): How many times the it will draw lines in a chart.
      linelength (int or float): The length of the line.
      startcoordinates (tuple or list): Where the line graph's origin coordinates are.
  """
  c = __rint(1, 5)
  if c == 1:
    linegraph(datalist, color, pxperstep, linesize, startcoordinates)
  elif c == 2:
    bargraph(datalist, color, pxperstep, linesize, startcoordinates)
  elif c == 3:
    histogram(datalist, color, pxperstep, linesize, startcoordinates)
  elif c == 4:
    sidebargraph(datalist, color, pxperstep, linesize, startcoordinates)
  elif c == 5:
    bubblegraph(datalist, color, pxperstep, linesize, linelength, startcoordinates)
  
  
def examplesofchartsfrompytchart(print_or_return='print'):
  """
  Gives example of charts from this module.
  Args:
      p__rint_or_return (str, optional): Either p__rints the results or returns it. Defaults to 'p__rint'.
  returns:
      str: Examples of charts from module.
  """
  if print_or_return == 'p__rint':
    print('''Instructions:
1 - linegraph(): see https://www.howtogeek.com/wp-content/uploads/2021/11/GoogleSheetsLineChart.png?width=1198&trim=1,1&bg-color=000&pad=1,1 for example
2 - bargraph(): see https://www.math-only-math.com/images/representation-bar-graph.png for example
3 - histogram(): see https://www150.statcan.gc.ca/n1/edu/power-pouvoir/c-g/c-g05-7-1-eng.png for example
4 - bubblegraph(): see https://www.myexcelonline.com/wp-content/uploads/2020/06/Screenshot-2020-06-25-at-3.14.16-PM.png for example
5 - sidebargraph(): see https://depictdatastudio.com/wp-content/uploads/2017/01/Depict-Data-Studio_Bar-Charts_Vertical-or-Horizontal_Horizontal-1.jpg for example
6 - mover(): mover.obj() returns a turtle object; rootobj() returns the turtle module''')
    return "<class 'instructions'>"
  elif print_or_return == 'return':
    return '''Instructions:
1 - linegraph(): see https://www.howtogeek.com/wp-content/uploads/2021/11/GoogleSheetsLineChart.png?width=1198&trim=1,1&bg-color=000&pad=1,1 for example
2 - bargraph(): see https://www.math-only-math.com/images/representation-bar-graph.png for example
3 - histogram(): see https://www150.statcan.gc.ca/n1/edu/power-pouvoir/c-g/c-g05-7-1-eng.png for example
4 - bubblegraph(): see https://www.myexcelonline.com/wp-content/uploads/2020/06/Screenshot-2020-06-25-at-3.14.16-PM.png for example
5 - sidebargraph(): see https://depictdatastudio.com/wp-content/uploads/2017/01/Depict-Data-Studio_Bar-Charts_Vertical-or-Horizontal_Horizontal-1.jpg for example
6 - mover(): mover.obj() returns a turtle object; rootobj() returns the turtle module'''


def texttag(text: str or int or float or list or tuple or bool, color: str, font: tuple or list, coordinates: tuple or list):
  """
  Function to show text.
  Args:
      text (str or int or float or list or tuple or bool): Text to be displayed on screen.
      color (str): Color of message.
      font (tuple or list): Font of message.
      coor (tuple or list): Coordinates of text.
  """
  t = __root.Turtle()
  t.hideturtle()
  t.color(color)
  t.penup()
  t.goto(coordinates)
  t.pendown()
  t.write(text, False, 'center', font)
  screen.update()
  
  
def box(squarelength: int or float, linesize: int or float, color: str, startcoordinates: tuple or list):
  """
  Function to create a box.
  Args:
      squarelength (int or float): Length of square
      linesize (int or float): linesize of border
      color (str): Color of border
      startcoordinates (tuple or list): 
  """
  sl = squarelength
  t = __root.Turtle()
  screen.tracer(0)
  t.color(color)
  t.pensize(linesize)
  t.hideturtle()
  t.penup()
  t.goto(startcoordinates)
  t.pendown()
  t.lt(90)
  for i in range(4):
    t.fd(sl)
    t.rt(90)
  screen.update()


def clearall():
  """
  Clears everything in the screen.
  """
  screen.clear()


def start():
  """
  Starts the screen.
  """
  screen.mainloop()


def windowname(thename: str):
  """
  Adds the parameter's argument to the window's name.
  
  Args:
      thename (str): Window name
  """
  screen.title(thename)


def savechart(thefilename: str, width='defult', height='defult'):
  """
  Saves the graph from the screen.
  Args:
      thefilename (str): File name to save image as
      width (int or float, optional): Width of saved graph
      height (int or float, optional): Height of saved graph
  """
  _ex = thefilename.split('.')
  try:
    ex = _ex[1]
  except IndexError:
    pass
  if thefilename.find('.') != -1:
    if ex != 'ps' and ex is not None:
          raise Exception('No ps extension. Cannot use any other extension')
    elif ex is None:
          pass
  else:
      pass
  if width == 'defult' and height == 'defult' or width == 'defult' and height != 'defult' or width != 'defult' and height == 'defult':
    screen.getcanvas().postscript(file=thefilename)
  elif width != 0 and height != 0:
        screen.getcanvas().postscript(file=thefilename, width=width, height=height)
  book = open(thefilename, 'r').read()
  with open(thefilename, 'w') as savedfile:
    savedfile.write(book.replace('%%Creator: Tk Canvas Widget', '%%Creator: pytchart'))
