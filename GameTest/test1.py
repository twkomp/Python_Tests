import pygame
import pygame.time
pygame.init()
display = pygame.display.set_mode((500,500))
pygame.display.set_caption('graphical Test')

clock = pygame.time.Clock
objects = []


def calcphysics(object1,object2):
	posx1,posx2 = objects[object1][1],objects[object2][1]
	posy1,posy2 = objects[object1][2],objects[object2][2]
	
	sizex1,sizex2 = objects[object1][3],objects[object2][3]
	sizey1,sizey2 = objects[object1][4],objects[object2][4]
	points1 = [[posx1,posy1],[posx1+sizex1,posy1],[posx1,posy1+sizey1],[posx1+sizex1,posy1+sizey1]]
	points2 = [[posx2,posy2],[posx2+sizex2,posy2],[posx2,posy2+posy2],[posx2+sizex2,posy2+posy2]]
	print(points1,points2)
	if points1[0][0]>=points2[0][0] and points1[0][0]<=points2[1][0] and points1[0][1]>=points2[2][1] and points1[0][1]<=points2[3][1]:
		collision = True
	elif points1[1][0]>=points2[0][0] and points1[1][0]<=points2[1][0] and points1[1][1]>=points2[2][1] and points1[1][1]<=points2[3][1]:
		collision = True
	elif points1[2][0]>=points2[0][0] and points1[2][0]<=points2[1][0] and points1[2][1]>=points2[2][1] and points1[2][1]<=points2[3][1]:
		collision = True
	elif points1[3][0]>=points2[0][0] and points1[3][0]<=points2[1][0] and points1[3][1]>=points2[2][1] and points1[3][1]<=points2[3][1]:
		collision = True
	else:
		collision = False
	return collision
def addrect(x,y,x2,y2,color):
	rect = pygame.draw.rect(display,color,[x,y,x2,y2],0)
	objects.append([rect,x,y,x2,y2])

addrect(0,400,500,10,(255,255,255))
addrect(20,410,50,50,(0,0,255))

print(calcphysics(1,0))

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		
	pygame.display.update()
	pygame.time.wait(25)