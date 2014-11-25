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

    tableX=table_size[0]
    tableY=table_size[1]

    dx=(ballX-lastX)
    dy=(ballY-lastY)

    YGuess=ballY
    
    #print('Ball Angle is:', ballAngle*360/math.pi/2)
    #print('Ball slope is:', slope)

    if dx !=0:
	slope = dy/dx
	ballAngle = -math.atan2(dy,dx)
	XGuess = ballX
	
	if dx<0:
	    while(0<XGuess):
		if ballAngle>0:
		    XGuess -= (ballY/math.tan(ballAngle))
		    YGuess= (math.tan(ballAngle)*(XGuess))
		    ballAngle *=-1
		else:
		    XGuess += ((tableY-ballY)/math.tan(ballAngle))
		    YGuess=tableY-(math.tan(ballAngle)*(XGuess-tableX))
		    ballAngle *=-1
	    print(YGuess)		    
	'''
	if dx>0:
	    while(XGuess<tableX):
		if ballAngle>0:
		    XGuess += (ballY/math.tan(ballAngle))
		    YGuess= (math.tan(ballAngle)*(XGuess-tableX))
		    ballAngle *=-1
		else:
		    XGuess -= ((tableY-ballY)/math.tan(ballAngle))
		    YGuess=tableY+(math.tan(ballAngle)*(XGuess-tableX))
		    ballAngle *=-1
	    print(YGuess)
	'''
	        
	
    '''
	if(dx>0):
	    while(XGuess<paddleX):
		ballAngle=ballAngle%(2*math.pi)
		if ballAngle>0:
		    XGuess += (ballY/math.tan(ballAngle))
		    print(ballAngle, " ", XGuess)
		    ballAngle = (2*math.pi)-ballAngle
		elif ballAangle<0:
		    XGuess -= ((tableY-ballY)/math.tan(ballAngle))
		    print(ballAngle, " ", XGuess)
		    ballAngle = (2*math.pi)-ballAngle
		else:
		    YGuess = ballY
		    XGuess = tableX+1
	    ballAngle = (2*math.pi)-ballAngle
	    #print(XGuess)
	elif(dx<0):
	    pass
    '''
    if ballY > paddleY:
	return "down"
    else:
	return "up"
	'''
	while(0<XGuess and XGuess<tableX):
	    if ballAngle>0:
		if dx>0:
		    XGuess = XGuess-(ballY/math.tan(ballAngle))
		elif dx<0:
		    XGuess = XGuess+(ballY/math.tan(ballAngle))
		ballAngle = (2*math.pi)-ballAngle
	    elif ballAngle<0:
		if dx>0:
		    XGuess = XGuess-(ballY/math.tan(ballAngle))
		elif dx<0:
		    XGuess = XGuess+(ballY/math.tan(ballAngle))
		ballAngle = (2*math.pi)-ballAngle
	    else:
		pass
	    
	ballAngle = 2*math.pi-ballAngle
	print(XGuess)
	
	if(XGuess<0):
	    YGuess= ballY-(math.tan(ballAngle)*ballX)

	    print(YGuess)
	elif(XGuess>tableX):
	    YGuess= ballY-(math.tan(ballAngle)*(ballX-tableX))
	    print(YGuess)
	'''    
    	

