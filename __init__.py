"""
  Makes automatic random data-based charts.
  Supposedly used to encourage people to code with no experience and to
  make a chart very customizable.
  No modules to manually install or complex function names to make the person 
  have fun.
  v0.1.0
"""


import turtle as _root
from turtle import title
from random import randint as rint
from time import sleep as delay
screen = _root.Screen()
s = screen
s.title('Pytchart')


def linegraph(color='light blue', pxperstep=0.070, linesize=5, high=1000, low=10, times=10, startcoor=(0, 0)):
  """
  Generates a line graph (obviously).

  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line size of the chart's line. Defaults to 5.
      high (int, optional): The highest number the chart's random generator goes. Defaults to 1000.
      low (int, optional): The lowest number the chart's random generator goes. Defaults to 10.
      times (int, optional): How many times the it will draw lines in a chart. Defaults to 10.
      startcoor (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).

  returns:
      str, int: The id of the graph (this one is 22)
  """
  y = _root.Turtle('circle')
  y.hideturtle()
  ra = rint(low, high)
  y.pensize(linesize)
  y.penup()
  y.color(color)
  s.tracer(25)
  y.goto(startcoor)
  y.lt(45)
  y.pendown()
  for i in range(times):
    y.fd(pxperstep * ra)
    y.rt(45)
    y.fd(10)
    y.lt(45)
    ra = rint(low, high)
  return ["<class 'pytchart'>", 0.11 * 2]
  
  
def bargraph(color='light blue', pxperstep=0.070, linesize=5, high=1000, low=10, times=20, startcoor=(0, 0)):
  """
  Generates a bar graph (obviously).

  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line size of the graph's line. Defaults to 5.
      high (int, optional): The highest number the chart's random generator goes. Defaults to 1000.
      low (int, optional): The lowest number the chart's random generator goes. Defaults to 10.
      times (int, optional): How many times the it will draw lines in a chart. Defaults to 10.
      startcoor (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).

  returns:
      str, int: The id of the graph (this one is 44)
  """
  y = _root.Turtle('circle')
  ra = rint(low, high)
  y.pensize(linesize)
  y.color(color)
  s.tracer(25)
  y.hideturtle()
  y.penup()
  y.goto(startcoor)
  y.lt(90)
  y.pendown()
  for i in range(times):
    y.fd(pxperstep * ra)
    y.bk(pxperstep * ra)
    y.penup()
    y.rt(90)
    y.fd(10)
    y.lt(90)
    y.pendown()
    ra = rint(low, high)
  return ["<class 'pytchart'>", 0.22 * 2]
  
  
def histogram(color='light blue', pxperstep=0.070, linesize=5, high=1000, low=10, times=40, startcoor=(0, 0)):
  """
  Generates a histogram (obviously).

  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line linesize of the graph's line. Defaults to 5.
      high (int, optional): The highest number the chart's random generator goes. Defaults to 1000.
      low (int, optional): The lowest number the chart's random generator goes. Defaults to 10.
      times (int, optional): How many times the it will draw lines in a chart. Defaults to 10.
      startcoor (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).

  returns:
      str, int: The id of the graph (this one is 66)
  """
  y = _root.Turtle('circle')
  ra = rint(low, high)
  y.pensize(linesize)
  y.color(color)
  s.tracer(100)
  y.hideturtle()
  y.penup()
  y.goto(startcoor)
  y.lt(90)
  y.pendown()
  for i in range(times):
    y.fd(pxperstep * ra)
    y.bk(pxperstep * ra)
    y.rt(90)
    y.fd(2.5)
    y.lt(90)
    ra = rint(low, high)
  return ["<class 'pytchart'>", 0.33 * 2]
  
  
def bubblegraph(color='light blue', pxperstep=0.070, linesize=5, high=1000, low=10, times=10, linelength=510, startcoor=(0, 0)):
  """
  Generates a bubble graph (obviously).

  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line size of the graph's line. Defaults to 5.
      high (int, optional): The highest number the chart's random generator goes. Defaults to 1000.
      low (int, optional): The lowest number the chart's random generator goes. Defaults to 10.
      times (int, optional): How many times the it will draw lines in a chart. Defaults to 10.
      linelength (int, optional): The length of the line. Defaults to 510.
      startcoor (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).

  returns:
      str, int: The id of the graph (this one is 88)
  """
  y = _root.Turtle('circle')
  y.shape('circle')
  ra = rint(low, high)
  y.color(color)
  s.tracer(25)
  y.penup()
  y.goto(startcoor)
  y.lt(45)
  y.pendown()
  y.pensize(linesize)
  y.fd(linelength)
  y.bk(linelength)
  y.penup()
  for i in range(times):
    y.fd(pxperstep * ra)
    y.stamp()
    y.rt(45)
    y.fd(10)
    y.lt(45)
    ra = rint(low, high)
  print('Chart initialized')
  print('App initialized: true')
  print('Setttings init;')
  print('Color: ' + color)
  print('Pixels per 1 step: ' + str(pxperstep))
  print('Line size: ' + str(linesize))
  print('Highest graph goes: ' + str(high))
  print('Lowest graph goes: ' + str(low))
  print('Times executed: ' + str(times))
  print('Line length: ' + str(linelength))
  print('Start coordinates: ' + str(startcoor))
  return ["<class 'pytchart'>", 0.44 * 2]
  
  
def sidebargraph(color='light blue', pxperstep=0.70, linesize=8, high=1000, low=10, times=10, startcoor=(0, 0)):
  """
  Generates a side bar graph (obviously) from the left to the right.

  Args:
      color (str, optional): The color of the graph. Defaults to 'light blue'.
      pxperstep (float, optional): How far the drawer moves per 1 step. Defaults to 0.070.
      linesize (int, optional): The line linesize of the graph's line. Defaults to 5.
      high (int, optional): The highest number the chart's random generator goes. Defaults to 1000.
      low (int, optional): The lowest number the chart's random generator goes. Defaults to 10.
      times (int, optional): How many times it will draw lines in a chart. Defaults to 10.
      startcoor (tuple, optional): Where the line graph's origin coordinates are. Defaults to (0, 0).

  returns:
      str, int: The id of the graph (this one is 99)
  """
  y = _root.Turtle('circle')
  y.hideturtle()
  ra = rint(low, high)
  y.pensize(linesize)
  y.color(color)
  s.tracer(25)
  y.penup()
  y.goto(startcoor)
  y.pendown()
  for i in range(times):
    y.fd(pxperstep * ra)
    y.bk(pxperstep * ra)
    y.rt(90)
    y.penup()
    y.fd(20)
    y.lt(90)
    y.pendown()
    ra = rint(low, high)
  return ["<class 'pytchart'>", 0.55 * 2]


def randomgraph(color: str, pxperstep: int or float, linesize: int or float, high: int or float, low: int or float, times: int, linelength: int or float, startcoor: tuple or list):
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
      startcoor (tuple or list): Where the line graph's origin coordinates are.
  """
  c = rint(1, 5)
  if c == 1:
    linegraph(color, pxperstep, linesize, high, low, times, startcoor)
  elif c == 2:
    bargraph(color, pxperstep, linesize, high, low, times, startcoor)
  elif c == 3:
    histogram(color, pxperstep, linesize, high, low, times, startcoor)
  elif c == 4:
    sidebargraph(color, pxperstep, linesize, high, low, times, startcoor)
  elif c == 5:
    bubblegraph(color, pxperstep, linesize, high, low, times, linelength, startcoor)
  
  
def examplesofchartsfrompytchart(print_or_return='print'):
  """
  Gives example of charts from this module.

  Args:
      print_or_return (str, optional): Either prints the results or returns it. Defaults to 'print'.

  returns:
      str: Examples of charts from module.
  """
  if print_or_return == 'print':
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

  returns:
      str, int: The id of the function (this one is 1.32)
  """
  t = _root.Turtle()
  t.hideturtle()
  t.color(color)
  t.penup()
  t.goto(coordinates)
  t.pendown()
  t.write(text, False, 'center', font)
  return ["<class 'pytchart'>", 0.66 * 2, text]
  
  
def box(squarelength: int or float, linesize: int or float, color: str, startcoor: tuple or list):
  """
  Function to create a box.

  Args:
      squarelength (int or float): Length of square
      linesize (int or float): linesize of border
      color (str): Color of border
      startcoor (tuple or list): 

  returns:
      str, int: The id of the function (this one is 1.54)
  """
  sl = squarelength
  t = _root.Turtle()
  s.tracer(0)
  t.color(color)
  t.pensize(linesize)
  t.hideturtle()
  t.penup()
  t.goto(startcoor)
  t.pendown()
  t.lt(90)
  for i in range(4):
    t.fd(sl)
    t.rt(90)
  return ["<class 'pytchart'>", 0.77 * 2]


def clearall():
  """
  Clears everything in the screen.

  returns:
      str, int: The id of the function (this one is 1.98)
  """
  s.clear()
  return ["<class 'pytchart'>", 0.99 * 2]


def renderchart():
  """
  Renders the chart.

  Returns:
      str, int: The id of the function
  """
  s.update()
  s.mainloop()
  return ["<class 'pytchart'>", 0.108 * 2]


def windowname(thename: str):
  """
  Adds the parameter's argument to the window's name.

  Args:
      thename (str): Window name

  returns:
      str, int: The id of the function
  """
  s.title(thename)
  return ["<class 'pytchart'>", 122 * 2]


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
  
  
class Mover(_root.Turtle):
  """
  Class to move an object

  Args:
      r (module): Turtle module
  """
  
  
  def __init__(self):
    pass
  
  
  def obj(self):
    return _root.Turtle()
    
    
  def rootobj(self):
    return _root
