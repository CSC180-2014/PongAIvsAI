import math
import sys
lastX=0
lastY=0
ballX=480/2
ballY=280/2
XGuess=480
YGuess=280
'''
    return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
'''
def chaser(paddle_frect, other_paddle_frect, ball_frect, table_size):

    global lastX
    global lastY
    global ballX
    global ballY
    global XGuess
    global YGuess
    lastX=ballX
    lastY=ballY

    paddleX=paddle_frect.pos[0]
    paddleY=paddle_frect.pos[1]+paddle_frect.size[1]/2
    ballX=ball_frect.pos[0]+ball_frect.size[0]/2
    ballY=ball_frect.pos[1]+ball_frect.size[1]/2

    ballR=ball_frect.size[0]/2
    
    paddleL=paddle_frect.size[1]
    tableX=table_size[0]
    tableY=table_size[1]

    dx=(ballX-lastX)
    dy=(ballY-lastY)

    YGuess=ballY
    XGuess=ballX
    bounces=0
    if(dx>0):
	while(XGuess<(paddleX-ballR)):
	    bounces+=1
	    if(dy>0):
		XGuess+=(tableY-ballY-ballR)/dy*dx
	    else:
		XGuess+=abs((ballY-ballR)/dy)*dx
	    dy=-dy		
	dy=-dy
	if(dy>0):
	    YGuess=tableY-(XGuess-paddleX-ballR)/dx*dy
	else:
	    YGuess=-((XGuess-paddleX-ballR)/dx*dy)
	if (((paddleY-paddleL/3) < YGuess < (paddleY+paddleL/3)) and bounce==1):
	    if paddleY<YGuess:
		YGuess-=paddleL/3
	    else:
		YGuess+=paddleL/3	
    else:
	YGuess=tableY/2
    if YGuess > paddleY:
	return "down"
    else:
	return "up"