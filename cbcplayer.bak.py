import curses
from curses import wrapper
import subprocess
import os
import string
import configparser

def main(stdscr):
        config = configparser.ConfigParser()
        config.read('player.ini')

        curses.curs_set(0)

        stdscr.refresh()

        drawMenu(stdscr)

def drawMenu(stdscr):
        stdscr.clear()
        rows = curses.LINES
        cols = curses.COLS

        drawHorzLines(stdscr,0,cols,'-')
        drawHorzLines(stdscr,2,cols,'-')

        stdscr.addstr(1,1,"CBC Radio One - London")
        stdscr.addstr(4,1,"p)  Play")
        stdscr.addstr(5,1,"s)  Stop")
        stdscr.addstr(6,1,"q)  Quit")
        stdscr.addstr(4,15,"m)  Mute")
        stdscr.addstr(5,15,"n)  Un-mute")
        stdscr.addstr(6,15,"z)  Snooze")
        drawHorzLines(stdscr,rows-2,cols,'*')
        drawStatusBar(stdscr,'')

        stdscr.refresh()
        getKeys(stdscr)

def drawHorzLines(stdscr,row,cols,c):
        for x in range(0,cols):
                stdscr.addstr(row,x,c)

def drawStatusBar(stdscr,stat):
        getvolume = subprocess.check_output(['mpc', 'volume'])
        getvolume = getvolume.decode("utf-8")
        x = len(getvolume) - 1
        getvolume = getvolume[0:x]
        stdscr.addstr(curses.LINES-1,curses.COLS-15,getvolume)
        if len(stat) > 0:
                stdscr.addstr(curses.LINES-1,0,stat)
        stdscr.refresh()

def playCBC(stdscr):
        stdscr.refresh()
        subprocess.run(['mpc','play'],stdout=subprocess.PIPE)
        #stdscr.addstr(4,1,"p)  Playing")
        drawStatusBar(stdscr,'Playing')
        stdscr.refresh()

def getKeys(stdscr):
        while True:
                k = stdscr.getch()
                if k == ord('p'):
                        playCBC(stdscr)
                elif k == ord('s'):
                        subprocess.run(['mpc','stop'],stdout=subprocess.PIPE)
                        drawStatusBar(stdscr, 'Stopped')
                elif k == ord('u'):
                        subprocess.run(['mpc', 'volume', '+1'],stdout=subprocess.PIPE)
                        drawStatusBar(stdscr,'')
                elif k == ord('d'):
                        subprocess.run(['mpc','volume','-1'],stdout=subprocess.PIPE)
                        drawStatusBar(stdscr,'')
                elif k == ord('m'):
                        subprocess.run(['mpc','volume','0'],stdout=subprocess.PIPE)
                        drawStatusBar(stdscr,'Muted          ')
                elif k == ord('n'):
                        subprocess.run(['mpc','volume','40'],stdout=subprocess.PIPE)
                        drawStatusBar(stdscr,'Playing')
                elif k == ord('z'):
                        subprocess.run(['mpc', 'volume', '0'],stdout=subprocess.PIPE)
                        rawStatusBar(stdscr, 'Snoozing')
                elif k == ord('q'):
                        subprocess.run(['mpc','stop'],stdout=subprocess.PIPE)
                        break


wrapper(main)