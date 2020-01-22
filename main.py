from os import system, name 
import time



#-----------------FUNCTIONS--------------------------------------

def view(lay0,lay1,lay2,lay3,lay4,xpos, ypos):
  mid = int(((len(lay0))/2)+xpos)
  viewsize=20
  si = int(mid-viewsize)
  ei = int(mid+viewsize)
  printtoscreen(mid,si,ei,lay0,lay1,lay2,lay3,lay4)
  
def printtoscreen(xpos,ypos,x,y,expos,eypos,expos1,eypos1,expos2,eypos2):
  lay0="............................................................."
  lay0=list(lay0)
  lay1="............................................................."
  lay1=list(lay1)
  lay2="..            .     .         .         .                  .."
  lay2=list(lay2)
  lay3="..            .     .         .         .                  .."
  lay3=list(lay3)
  lay4="..........    .     .    .    .    ......                  .."
  lay4=list(lay4)
  lay5="..            .     .    .    .                            .."
  lay5=list(lay5)
  lay6="..            .     .    .    .                            .."
  lay6=list(lay6)
  lay7=".....    ......     .    .    .    ......                  .."
  lay7=list(lay7)
  lay8="..                       .    .         .                  .."
  lay8=list(lay8)
  lay9="..                       .    .         .                  .."
  lay9=list(lay9)
  lay10="..    ....................    ......    .                  .."
  lay10=list(lay10)
  lay11="..                       .         .                       .."
  lay11=list(lay11)
  lay12="..                       .         .                       .."
  lay12=list(lay12)
  lay13="...............      .....    .    .    .                  .."
  lay13=list(lay13)
  lay14="..                   .        .    .    .                  .."
  lay14=list(lay14)
  lay15="..                   .        .         .                  .."
  lay15=list(lay15)
  lay16="......    ................    .         .                  .."
  lay16=list(lay16)
  lay17="..                            .    .    .                  .."
  lay17=list(lay17)
  lay18="..                            .    .    .                  .."
  lay18=list(lay18)
  lay19="............................................................."
  lay19=list(lay19)
  lay20="............................................................."
  lay20=list(lay20)
  ei = len(lay0)
  si = 0
  i=si
  
  player(xpos,ypos,lay0,lay1,lay2,lay3,lay4,lay5,lay6,lay7,lay8,lay9,lay10,lay11,lay12,lay13,lay14,lay15,lay16,lay17,lay18,lay19,lay20,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)

  #enemy movement
  
  
  if(xpos>expos):
    xdiff=xpos-expos
  else:
    xdiff=expos-xpos
  if(ypos>eypos):
    ydiff=ypos-eypos
  else:
    ydiff=eypos-ypos
  
  #print("xdiff",xdiff)
  #print("ydiff",ydiff)

  if(xdiff>ydiff and xpos>expos):
    expos+=1
  elif(xdiff>ydiff and xpos<expos):
    expos-=1
  if(xdiff<ydiff and ypos>eypos):
    eypos+=1
  elif(xdiff<ydiff and xpos<expos):
    eypos-=1


  #enemy1 movement
  if(xpos>expos1):
    xdiff1=xpos-expos1
  else:
    xdiff1=expos1-xpos
  if(ypos>eypos1):
    ydiff1=ypos-eypos1
  else:
    ydiff1=eypos1-ypos
  
  #print("xdiff1",xdiff1)
  #print("ydiff1",ydiff1)

  if(xdiff1>ydiff1 and xpos>expos1):
    expos1+=1
  elif(xdiff1>ydiff1 and xpos<expos1):
    expos1-=1
  if(xdiff1<ydiff1 and ypos>eypos1):
    eypos1+=1
  elif(xdiff1<ydiff1 and xpos<expos1):
    eypos1-=1
  if(xdiff1==ydiff1 and xpos>expos1):
    expos1+=1
  elif(xdiff1==ydiff1 and xpos<expos1):
    expos2-=1

  #enemy2 movement
  if(xpos>expos2):
    xdiff2=xpos-expos2
  else:
    xdiff2=expos2-xpos
  if(ypos>eypos2):
    ydiff2=ypos-eypos2
  else:
    ydiff2=eypos2-ypos
  
  #print("xdiff2",xdiff2)
  #print("ydiff2",ydiff2)

  if(xdiff2>ydiff2 and xpos>expos2):
    expos2+=1
  elif(xdiff2>ydiff2 and xpos<expos2):
    expos2-=1
  if(xdiff2<ydiff2 and ypos>eypos2):
    eypos2+=1
  elif(xdiff2<ydiff2 and ypos<expos2):
    eypos2-=1
  if(xdiff2==ydiff2 and xpos>expos2):
    expos2+=1
  elif(xdiff2==ydiff2 and xpos<expos2):
    expos2-=1
  if(xdiff==0):
    if(ypos>eypos2):
      eypos2+=1
    else:
      eypos-=1
  if(ydiff==0):
    if(xpos>expos2):
      expos2+=1
    else:
      expos-=1
  
  enemy(expos,eypos,lay0,lay1,lay2,lay3,lay4,lay5,lay6,lay7,lay8,lay9,lay10,lay11,lay12,lay13,lay14,lay15,lay16,lay17,lay18,lay19,lay20,x,y)
  if(xpos==expos and ypos==eypos):
    quit('You lose!!!')

  x=None
  y=None
  while(i<ei):
    print(lay0[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay1[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay2[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay3[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay4[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay5[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay6[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay7[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay8[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay9[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay10[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay11[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay12[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay13[i], end = '')
    i+=1
  i=si
  print("")
  while(i<ei):
    print(lay14[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay15[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay16[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay17[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay18[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay19[i], end = '')
    i+=1
  i=si
  print('')
  while(i<ei):
    print(lay20[i], end = '')
    i+=1

  print("\nview")
  
  inp = input("")
  if(inp=='a'):
    xpos-=1
    x=False
  elif(inp=="d"):
    xpos+=1
    x=True
  elif(inp=='w'):
    ypos-=1
    y=False
  elif(inp=='s'):
    ypos+=1
    y=True
  elif(inp=='t'):
    if(xdiff==1 or xdiff==-1 or ydiff==1 or ydiff==-1):
      print("attack on enemy 0")
      expos+=10
    if(xdiff1==1 or xdiff1==-1 or ydiff1==1 or ydiff1==-1):
      print("attack on enemy 1")
      expos1+=10
    if(xdiff2==1 or xdiff2==-1 or ydiff2==1 or ydiff2==-1):
      print("attack on enemy 2")
      expos2+=10
      
  clear()
  printtoscreen(xpos,ypos,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)

def clear(): 
  _ = system('clear') 

def player(pxpos,pypos,lay0,lay1,lay2,lay3,lay4,lay5,lay6,lay7,lay8,lay9,lay10,lay11,lay12,lay13,lay14,lay15,lay16,lay17,lay18,lay19,lay20,x,y,expos,eypos,expos1,eypos1,expos2,eypos2):

  playericon = 'O'
  if (pypos==0 and lay0[pxpos]!='.'):
    lay0[pxpos] = playericon
  elif (pypos==1 and lay1[pxpos]!='.'):
    lay1[pxpos] = playericon
  elif (pypos==2 and lay2[pxpos]!='.'):
    lay2[pxpos] = playericon
  elif (pypos==3 and lay3[pxpos]!='.'):
    lay3[pxpos] = playericon
  elif (pypos==4 and lay4[pxpos]!='.'):
    lay4[pxpos] = playericon
  elif (pypos==5 and lay5[pxpos]!='.'):
    lay5[pxpos] = playericon
  elif (pypos==6 and lay6[pxpos]!='.'):
    lay6[pxpos] = playericon
  elif (pypos==7 and lay7[pxpos]!='.'):
    lay7[pxpos] = playericon
  elif (pypos==8 and lay8[pxpos]!='.'):
    lay8[pxpos] = playericon
  elif (pypos==9 and lay9[pxpos]!='.'):
    lay9[pxpos] = playericon
  elif (pypos==10 and lay10[pxpos]!='.'):
    lay10[pxpos] = playericon
  elif (pypos==11 and lay11[pxpos]!='.'):
    lay11[pxpos] = playericon
  elif (pypos==12 and lay12[pxpos]!='.'):
    lay12[pxpos] = playericon
  elif (pypos==13 and lay13[pxpos]!='.'):
    lay13[pxpos] = playericon
  elif (pypos==14 and lay14[pxpos]!='.'):
    lay14[pxpos] = playericon
  elif (pypos==15 and lay15[pxpos]!='.'):
    lay15[pxpos] = playericon
  elif (pypos==16 and lay16[pxpos]!='.'):
    lay16[pxpos] = playericon
  elif (pypos==17 and lay17[pxpos]!='.'):
    lay17[pxpos] = playericon
  elif (pypos==18 and lay18[pxpos]!='.'):
    lay18[pxpos] = playericon
  elif (pypos==19 and lay19[pxpos]!='.'):
    lay19[pxpos] = playericon
  elif (pypos==20 and lay20[pxpos]!='.'):
    lay20[pxpos] = playericon
  else:
    if(x==True):
      printtoscreen(pxpos-1,pypos,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)
    elif(x==False):
      printtoscreen(pxpos+1,pypos,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)
    elif(y==True):
      printtoscreen(pxpos,pypos-1,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)
    elif(y==False):
      printtoscreen(pxpos,pypos+1,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)
  if (pxpos>=41):
    quit('You Win!')

def enemy(pxpos,pypos,lay0,lay1,lay2,lay3,lay4,lay5,lay6,lay7,lay8,lay9,lay10,lay11,lay12,lay13,lay14,lay15,lay16,lay17,lay18,lay19,lay20,x,y):
  enemyicon = 'X'
  if (pypos==0 and lay0[pxpos]!='.'):
    lay0[pxpos] = enemyicon
  elif (pypos==1 and lay1[pxpos]!='.'):
    lay1[pxpos] = enemyicon
  elif (pypos==2 and lay2[pxpos]!='.'):
    lay2[pxpos] = enemyicon
  elif (pypos==3 and lay3[pxpos]!='.'):
    lay3[pxpos] = enemyicon
  elif (pypos==4 and lay4[pxpos]!='.'):
    lay4[pxpos] = enemyicon
  elif (pypos==5 and lay5[pxpos]!='.'):
    lay5[pxpos] = enemyicon
  elif (pypos==6 and lay6[pxpos]!='.'):
    lay6[pxpos] = enemyicon
  elif (pypos==7 and lay7[pxpos]!='.'):
    lay7[pxpos] = enemyicon
  elif (pypos==8 and lay8[pxpos]!='.'):
    lay8[pxpos] = enemyicon
  elif (pypos==9 and lay9[pxpos]!='.'):
    lay9[pxpos] = enemyicon
  elif (pypos==10 and lay10[pxpos]!='.'):
    lay10[pxpos] = enemyicon
  elif (pypos==11 and lay11[pxpos]!='.'):
    lay11[pxpos] = enemyicon
  elif (pypos==12 and lay12[pxpos]!='.'):
    lay12[pxpos] = enemyicon
  elif (pypos==13 and lay13[pxpos]!='.'):
    lay13[pxpos] = enemyicon
  elif (pypos==14 and lay14[pxpos]!='.'):
    lay14[pxpos] = enemyicon
  elif (pypos==15 and lay15[pxpos]!='.'):
    lay15[pxpos] = enemyicon
  elif (pypos==16 and lay16[pxpos]!='.'):
    lay16[pxpos] = enemyicon
  elif (pypos==17 and lay17[pxpos]!='.'):
    lay17[pxpos] = enemyicon
  elif (pypos==18 and lay18[pxpos]!='.'):
    lay18[pxpos] = enemyicon
  elif (pypos==19 and lay19[pxpos]!='.'):
    lay19[pxpos] = enemyicon
  elif (pypos==20 and lay20[pxpos]!='.'):
    lay20[pxpos] = enemyicon



#------------------------------CODE-----------------------
x=None
y=None
i=0
xpos=6
ypos=3

expos=3
eypos=3

expos1=26
eypos1=9

expos2=30
eypos2=17
printtoscreen(xpos,ypos,x,y,expos,eypos,expos1,eypos1,expos2,eypos2)



'''
  enemy(expos1,eypos1,lay0,lay1,lay2,lay3,lay4,lay5,lay6,lay7,lay8,lay9,lay10,lay11,lay12,lay13,lay14,lay15,lay16,lay17,lay18,lay19,lay20,x,y)
  if(xpos==expos1 and ypos==eypos1):
    quit('You lose!!!')

  enemy(expos2,eypos2,lay0,lay1,lay2,lay3,lay4,lay5,lay6,lay7,lay8,lay9,lay10,lay11,lay12,lay13,lay14,lay15,lay16,lay17,lay18,lay19,lay20,x,y)
  if(xpos==expos2 and ypos==eypos2):
    quit('You lose!!!')'''

