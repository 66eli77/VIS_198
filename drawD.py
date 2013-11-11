#!/usr/bin/env python2
import pygame
import sys
import json
import hashlib

from job import Job

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	size = 1920, 1200
	background = pygame.image.load("go.jpg")
	screen = pygame.display.set_mode(size)
	screen.blit(background,(0,0))
	width = 0

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					sys.exit()
									
		pseudoJob = Job(0)
		myjob = pseudoJob.getData()
		
		for n in range(0, len(myjob)):
			drawing(width, myjob[n], screen)
			if (n != len(myjob) -1):
				width += (myjob[n].node * myjob[n].core) / 5
			else:
				width = 0
		print myjob[0].qtime
		pygame.display.flip()
		fpsClock.tick(30)
		
		
def drawing(width, Job, screen):
	rect = pygame.Rect(width, 850, ((Job.node * Job.core) / 5),( -Job.wallrequest / 800))
	pygame.draw.rect(screen, _hexColor(Job.owner), rect)	
	
# Create a hex color value from a value
def _hexColor(x):
    hexVal = int(hashlib.md5(x).hexdigest(), 16) % 0xffffff
    return ( hexVal >> 16
           , hexVal >> 8  & 0xff
           , hexVal       & 0xff
           )
	    
if __name__=="__main__":
    main()