from graphics import *
import math

def drawLine(x, y, x2, y2, r, g, b, outline):
    line = Polygon(Point(x, y), Point(x2, y2))
    line.setOutline(color_rgb(r, g, b))
    line.setWidth(outline)
    line.draw(win)
def drawSquare(x, y, x2, y2, r, g, b, r2, g2, b2, fill, outline):
    square = Rectangle(Point(x, y), Point(x2, y2))
    if fill:
        square.setFill(color_rgb(r, g, b))
    square.setOutline(color_rgb(r2, g2, b2))
    square.setWidth(outline)
    square.draw(win)
def drawCircle(x, y, x2, y2, r, g, b, r2, g2, b2, fill, outline):
    if x > x2:
        xDist = x - x2
    else:
        xDist = x2 - x
    if y > y2:
        yDist = y - y2
    else:
        yDist = y2 - y
    radius = math.sqrt((xDist**2) + (yDist ** 2))
    radius = int(radius)
    while x - radius < 200:
        radius -= 1
    circle = Circle(Point(x, y), radius)
    if fill:
        circle.setFill(color_rgb(r, g, b))
    circle.setOutline(color_rgb(r2, g2, b2))
    circle.setWidth(outline)
    circle.draw(win)
def polygon(x, y, r, g, b, r2, g2, b2, fill, outline):
    finishLine = Rectangle(Point(-10, 600), Point(200, 800))
    finishLine.setFill(color_rgb(255, 200, 200))
    finishLine.draw(win)
    finishText = Text(Point(100, 625), "Finish")
    finishText.draw(win)
    pointList = []
    while 1 == 1:
        exitLoop = False
        pointList.append(Point(x, y))
        clickPoint = win.getMouse()
        #x = clickPoint.getX()
        #y = clickPoint.getY()
        while clickPoint.getX() < 200:
            if clickPoint.getY() >= 600:
                exitLoop = True
                break
            else:
                clickPoint = win.getMouse()
        if exitLoop:
            break
        drawLine(clickPoint.getX(), clickPoint.getY(), x, y, 200, 200, 200, 1)
        x = clickPoint.getX()
        y = clickPoint.getY()
    poly = Polygon(*pointList)
    if fill:
        poly.setFill(color_rgb(r, g, b))
    poly.setOutline(color_rgb(r2, g2, b2))
    poly.setWidth(outline)
    poly.draw(win)
    finishLine.undraw()
    finishText.undraw()
#Creating win
win = GraphWin("Window", 1200, 650)
#setting up user interface
for i in range(1, 5):
    square = Rectangle(Point(50, i * 25), Point(150, i * 25 + 20))
    square.draw(win)
text = Text(Point(100, 35), "Line")
text.draw(win)
text = Text(Point(100, 60), "Square")
text.draw(win)
text = Text(Point(100, 85), "Circle")
text.draw(win)
text = Text(Point(100, 110), "Polygon")
text.draw(win)
bg = Rectangle(Point(200, -10), Point(1300, 700))
bg.setFill("white")
bg.draw(win)
text = Text(Point(55, 150), "Fill")
text.draw(win)
text = Text(Point(145, 150), "Outline")
text.draw(win)
square = Rectangle(Point(10, 140), Point(100, 160))
square.draw(win)
square = Rectangle(Point(100, 140), Point(190, 160))
square.draw(win)
text = Text(Point(75, 375), "No fill")
text.draw(win)
square = Rectangle(Point(100, 365), Point(120, 385))
square.draw(win)
colourWheel = Image(Point(100, 250), "colourPicker.png")
colourWheel.draw(win)
arrow = Polygon(Point(80, 420), Point(80, 460), Point(30, 440))
arrow.draw(win)
arrow = Polygon(Point(120, 420), Point(120, 460), Point(170, 440))
arrow.draw(win)
outlineWidthText = Text(Point(100, 440), "1")
text = Text(Point(100, 410), "Outline thickness")
text.draw(win)
outlineWidthText.draw(win)
#setting defaults
mode = 0
colourMode = 0
r = 0
g = 0
b = 0
o_r = 0
o_g = 0
o_b = 0
colourSquare = Rectangle(Point(25, 330), Point(100, 350))
colourSquare.setFill(color_rgb(r, g, b))
colourSquare.setWidth(0)
colourSquare.draw(win)
colourSquare2 = Rectangle(Point(100, 330), Point(175, 350))
colourSquare2.setFill(color_rgb(o_r, o_g, o_b))
colourSquare2.setWidth(0)
colourSquare2.draw(win)
outlineWidth = 1
fill = True
#usage loop
while(1 == 1):
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    if x > 200:
        if mode == 0:
            clickPoint = win.getMouse()
            x2 = clickPoint.getX()
            while x2 < 200:
                clickPoint = win.getMouse()
                x2 = clickPoint.getX()
            y2 = clickPoint.getY()
            drawLine(x, y, x2, y2, o_r, o_g, o_b, outlineWidth)
        elif mode == 1:
            clickPoint = win.getMouse()
            x2 = clickPoint.getX()
            while x2 < 200:
                clickPoint = win.getMouse()
                x2 = clickPoint.getX()
            y2 = clickPoint.getY()
            drawSquare(x, y, x2, y2, r, g, b, o_r, o_g, o_b, fill, outlineWidth)
        elif mode == 2:
            indicatorDot = Circle(Point(x, y), 2)
            indicatorDot.draw(win)
            clickPoint = win.getMouse()
            x2 = clickPoint.getX()
            y2 = clickPoint.getY()
            drawCircle(x, y, x2, y2, r, g, b, o_r, o_g, o_b, fill, outlineWidth)
            indicatorDot.undraw()
        elif mode == 3:
            polygon(x, y, r, g, b, o_r, o_g, o_b, fill, outlineWidth)
    else:
        if y <= 120:
            if x >= 50 and x <= 120:
                if y <= 45 and y >= 25:
                    mode = 0
                elif y <= 70 and y >= 50:
                    mode = 1
                elif y <= 95 and y >= 75:
                    mode = 2
                elif y <= 120 and y >= 100:
                    mode = 3
        elif y >= 175 and y <= 325 and x >= 25 and x <= 175:
            if colourMode == 0:
                r, g, b = colourWheel.getPixel(int(x - 25), int(y - 175))
            else:
                o_r, o_g, o_b = colourWheel.getPixel(int(x - 25), int(y - 175))
            colourSquare.undraw()
            colourSquare = Rectangle(Point(25, 330), Point(100, 350))
            colourSquare.setFill(color_rgb(r, g, b))
            colourSquare.setWidth(0)
            colourSquare.draw(win)
            colourSquare2 = Rectangle(Point(100, 330), Point(175, 350))
            colourSquare2.setFill(color_rgb(o_r, o_g, o_b))
            colourSquare2.setWidth(0)
            colourSquare2.draw(win)
        elif x >= 100 and x <= 120 and y >= 365 and y <= 385:
            if fill:
                fillSquare = Rectangle(Point(100, 365), Point(120, 385))
                fillSquare.setFill("black")
                fillSquare.draw(win)
                fill = False
            else:
                fillSquare.undraw()
                fill = True
        elif x >= 10 and x <= 100 and y >= 140 and y <= 160:
            colourMode = 0
        elif x >= 100 and x <= 190 and y >= 140 and y <= 160:
            colourMode = 1
        elif y >= 420 and y <= 460:
            if x >= 30 and x <= 80:
                if outlineWidth > 0:
                    outlineWidth -= 1
            elif x >= 120 and x <= 170:
                outlineWidth += 1
            outlineWidthText.undraw()
            outlineWidthText = Text(Point(100, 440), str(outlineWidth))
            outlineWidthText.draw(win)
