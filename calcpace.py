from functions import dist
from functions import timerun
from functions import adjust
from functions import calcpace
from functions import predictrun
from functions import converttime
from functions import toprint
from functions import date
from functions import observations
from functions import setdata
from functions import getdata
from functions import deletedata
from functions import createtable
from texts import menu_text
from texts import invalidoption_text

#Menu inicial
menu_text()
option = input()
if option == '1':
    total = dist()
    totaltime= timerun()
    adjusted = adjust(totaltime)
    finalpace = calcpace(adjusted, total)
    convertedpace = converttime(finalpace)
    impress = toprint(convertedpace)
elif option == '2':
    total = dist()
    totaltime= timerun()
    adjusted = adjust(totaltime)
    calctemp = predictrun(adjusted, total)
    convertedtemprun = converttime(calctemp)
    impress = toprint(convertedtemprun)
elif option == '3':
    createtable()
    thedate = date()
    total = dist()
    totaltime = timerun()
    adjusted = adjust(totaltime)
    finalpace = calcpace(adjusted, total)
    convertedpace = converttime(finalpace)           
    obs = observations()
    escrever = setdata(thedate, total, totaltime, convertedpace, obs)
elif option == '4':
    getdata()
    deletedata()
elif option == '5':
    getdata()
else:
    invalidoption_text()
