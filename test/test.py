#!/usr/bin/env python
import pyx
from pyx import *
from pyx.path import *

import profile
import pstats

def drawpathwbbox(c, p):
    c.draw(p, color.rgb.red)
    bp=p.bpath()
    c.draw(bp, color.rgb.green, canvas.linestyle.dashed)
    bbox=p.bbox()
    c.draw(rect("%f t pt" % bbox.llx,            "%f t pt" % bbox.lly,
   	        "%f t pt" % (bbox.urx-bbox.llx), "%f t pt" % (bbox.ury-bbox.lly)))

def testspeed():
    "coordinates as strings"
    
    c=canvas.canvas()
    p=path([moveto(0,0)])

    for i in xrange(1000):
        p.append(lineto("%d pt" % i, "%d pt" % i))

    c.draw(p)
    c.writetofile("testspeed")

def testspeed2():
    "coordinates in user units"

    c=canvas.canvas()
    p=path([moveto(0,0)])

    for i in xrange(1000):
        p.append(lineto(i,i))

    c.draw(p)
    c.writetofile("testspeed")

def testspeed3():
    "coordinates in pts (internal routines)"

    c=canvas.canvas()
    p=path([pyx.path._moveto(0,0)])

    for i in xrange(1000):
        p.append(pyx.path._lineto(i, i))

    c.draw(p)
    c.writetofile("testspeed")

def testarcs(c):
    def testarc(c, x, y, phi1, phi2):
        p=path([arc(x,y, 0.5, phi1, phi2)])
        bp=p.bpath()
        c.draw(p, color.rgb.red)
        c.draw(bp, color.rgb.green, canvas.linestyle.dashed)

    def testarcn(c, x, y, phi1, phi2):
        p=path([arcn(x,y, 0.5, phi1, phi2)])
        bp=p.bpath()
        c.draw(p, color.rgb.red)
        c.draw(bp, color.rgb.green, canvas.linestyle.dashed)

    def testarct(c, r, x0, y0, dx1, dy1, dx2, dy2):
        p=path([moveto(x0,y0), arct(x0+dx1,y0+dy1, x0+dx2, y0+dy2, r), rlineto(dx2-dx1, dy2-dy1)])
        bp=p.bpath()
        c.draw(p, color.rgb.red, canvas.linewidth.Thick)
        c.draw(bp, color.rgb.green, canvas.linewidth.THin)


    testarc(c, 1, 2, 0, 90)
    testarc(c, 2, 2, -90, 90)
    testarc(c, 3, 2, 270, 90)
    testarc(c, 4, 2, 90, -90)
    testarc(c, 5, 2, 90, 270)
    testarc(c, 4, 3, 45, -90)
    testarc(c, 2, 3, 45, -90-2*360)
    testarc(c, 1, 3, 45, +90+2*360)

    testarcn(c, 1, 5, 0, 90) 
    testarcn(c, 2, 5, -90, 90) 
    testarcn(c, 3, 5, 270, 90) 
    testarcn(c, 4, 5, 90, -90) 
    testarcn(c, 5, 5, 90, 270) 
    testarcn(c, 4, 6, 45, -90) 
    testarcn(c, 2, 6, 45, -90-360) 
    testarcn(c, 1, 6, 45, -90+360)

    testarct(c, 0.5, 1, 8, 0, 1, 1, 1)
    testarct(c, 0.5, 3, 8, 1, 1, 1, 2)
    testarct(c, 0.5, 5, 8, 1, 0, 2, 1)
    testarct(c, 0.5, 7, 8, 1, 0, 2, 0)
    testarct(c, 0.0, 9, 8, 0, 1, 1, 1)

#    testarct(c, 0.5, 11, 8, 0, 1, 0, 0) # not allowed


def testmidpointsplit(c):
    p=path([moveto(10,10), rlineto(2,2), arc(15,12,1,30,300),closepath()])
    bpsplit=p.bpath().MidPointSplit()
    c.draw(p, color.rgb.red)
    c.draw(bpsplit, color.rgb.green, canvas.linestyle.dashed)


def testarcbbox(c):
    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, phi*0.1, 1, 0, phi)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, 5+phi*0.1, 1, phi, 360)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, 10+phi*0.1, 1, phi, phi+30)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, 15+phi*0.1, 1, phi, phi+120)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, 20+phi*0.1, 1, phi, phi+210)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, 25+phi*0.1, 1, phi, phi+300)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([arc(phi*0.1, 30+phi*0.1, 1, phi, phi+390)]))
       

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(20+phi*0.1, phi*0.09),
                             arc(20+phi*0.1, phi*0.1, 1, 0, phi)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(20+phi*0.1, 5+phi*0.11),
                             arc(20+phi*0.1, 5+phi*0.1, 1, 0, phi)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(20+phi*0.1, 10+phi*0.09),
                             arcn(20+phi*0.1, 10+phi*0.1, 1, 0, phi)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(20+phi*0.1, 15+phi*0.11),
                             arcn(20+phi*0.1, 15+phi*0.1, 1, 0, phi)]))

       

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(50+phi*0.1, phi*0.09),
                             arc(50+phi*0.1, phi*0.1, 1, 0, phi),
                             rlineto(1,1)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(50+phi*0.1, 5+phi*0.11),
                             arc(50+phi*0.1, 5+phi*0.1, 1, 0, phi),
                             rlineto(1,1)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(50+phi*0.1, 10+phi*0.09),
                             arcn(50+phi*0.1, 10+phi*0.1, 1, 0, phi),
                             rlineto(1,1)]))

    for phi in range(0,360,30):
       drawpathwbbox(c,path([moveto(50+phi*0.1, 15+phi*0.11),
                             arcn(50+phi*0.1, 15+phi*0.1, 1, 0, phi),
                             rlineto(1,1)]))





def testcurvetobbox(c):
    drawpathwbbox(c,path([moveto(10,10), curveto(12,16,14,15,12,19)]))


def testtrafobbox(c):
    sc=c.insert(canvas.canvas(trafo.translate(0,10).rotate(10)))

    p=path([moveto(10,10), curveto(12,16,14,15,12,19)]);   drawpathwbbox(sc,p)
    p=path([moveto(5,17), curveto(6,18, 5,16, 7,15)]);     drawpathwbbox(sc,p)

def testclipbbox(c):
    p=rect(6,12,6,4)

    sc=c.insert(canvas.canvas(clip=p))

    p=path([moveto(10,10), curveto(12,16,14,15,12,19)]);   drawpathwbbox(sc,p)
    p=path([moveto(5,17), curveto(6,18, 5,16, 7,15)]);     drawpathwbbox(sc,p)

def testintersectbezier(c):
    p=path([moveto(10,10), curveto(12,16,14,15,12,19)])
    q=path([moveto(12,10), curveto(12,16,14,22,11,16)])

    bp=p.bpath()
    bq=q.bpath()

    c.draw(q)
    c.draw(p)

    isect = bp.intersect(bq)

    for i in isect:
        (x, y) = bp.pos(i[0])
        c.draw(path([moveto(x,y),
                     rmoveto(-0.1, -0.1), rlineto(0.2, 0.2), rmoveto(-0.1, -0.1),
                     rmoveto(-0.1, +0.1), rlineto(0.2, -0.2)]))

c=canvas.canvas()
testarcs(c)
testmidpointsplit(c)
testarcbbox(c)    
testcurvetobbox(c)
testtrafobbox(c)
testclipbbox(c)
testintersectbezier(c)
c.writetofile("test")

#testspeed()
profile.run('testspeed()', 'test.prof')
pstats.Stats("test.prof").sort_stats('time').print_stats(10)

profile.run('testspeed2()', 'test.prof')
pstats.Stats("test.prof").sort_stats('time').print_stats(10)

profile.run('testspeed3()', 'test.prof')
pstats.Stats("test.prof").sort_stats('time').print_stats(10)
