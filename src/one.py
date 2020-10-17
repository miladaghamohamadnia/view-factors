from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# import serial
import os
import random
 
 
window = 0
GLUTwindow_height, GLUTwindow_width = 640,480
#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

#shift
X_SHIFT = 0.0
Y_SHIFT = 0.0
Z_SHIFT = -100

DIRECTION = 1
GLUTButton = [0, 0, 0, 0, 0]
GLUTmouse = [0, 0]
COLOR = [1,0,0]
needsPointerDisplayUpdate = True
PointerDisplayList = -1

import trimesh 
# mesh = trimesh.load('C:\\Users\\Casti\\projects\\temporary\\Radiosity\\3Dscenes\\test.obj')
mesh = trimesh.load('C:\\Users\\Casti\\projects\\temporary\\form_factors\\models\\confetti_2k.obj')


def renderPointerImage():
  global needsPointerDisplayUpdate, PointerDisplayList, COLOR
  if needsPointerDisplayUpdate:
    if PointerDisplayList != -1: #Deallocate previous display list
      glDeleteLists(PointerDisplayList, 1)
    PointerDisplayList = glGenLists(1)
    glNewList(PointerDisplayList, GL_COMPILE)
    glDisable(GL_LIGHTING)
    for tile in range(len(mesh.faces)):
      #Now split the integer ID into 4 separate bytes
      f = mesh.faces[tile]
      V = [mesh.vertices[i] for i in f]
      N = mesh.face_normals[tile]
      glColor3fv([c/(tile/len(mesh.faces)+1) for c in COLOR])
      # glColor4i(123,12,57,222)
      glBegin(GL_TRIANGLES)
      # glNormal3fv(N)
      for v in V:
        glVertex3fv( v )
      glEnd()
    glEndList()
    needsPointerDisplayUpdate = False
  glCallList(PointerDisplayList)

def InitGL(Width, Height): 
 
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 

        xdim, ydim = 100,100
        glViewport(0, 0, xdim, ydim)
        glScissor(0, 0, xdim, ydim)

        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
def keyPressed(key, x, y):
        global DIRECTION, COLOR, needsPointerDisplayUpdate
        global X_SHIFT, Y_SHIFT, Z_SHIFT
        if key==b'e':
          DIRECTION = 1-DIRECTION
        if key==b' ':
          needsPointerDisplayUpdate = True
          if COLOR[0]:
            COLOR = [0,1,0]
          else:
            COLOR = [1,0,0]
        if key==b'a':
          X_SHIFT += -.2
        if key==b'd':
          X_SHIFT += .2
        if key==b'w':
          Y_SHIFT += .2
        if key==b's':
          Y_SHIFT += -.2
        if key==b'q':
          Z_SHIFT += 5
        if key==b'z':
          Z_SHIFT += -5
        glutPostRedisplay()
 



def DrawGLScene():
        global X_AXIS,Y_AXIS,Z_AXIS
        global X_SHIFT, Y_SHIFT, Z_SHIFT
        global DIRECTION
        global COLOR
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
        glLoadIdentity()
        glTranslatef(X_SHIFT,Y_SHIFT,Z_SHIFT)
        ### <> rotation block ###
        glRotatef(X_AXIS,1.0,0.0,0.0)
        glRotatef(Y_AXIS,0.0,1.0,0.0)
        glRotatef(Z_AXIS,0.0,0.0,1.0)
        X_AXIS = X_AXIS + (-.020 if DIRECTION else 0.010)
        Z_AXIS = Z_AXIS + (-.020 if DIRECTION else 0.010)
        ### </> rotation block ###
        renderPointerImage()
        glutSwapBuffers()
        
 
 
 
def main():
 
        global window
        global GLUTwindow_height, GLUTwindow_width
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(GLUTwindow_height, GLUTwindow_width)
        glutInitWindowPosition(200,100)

        window = glutCreateWindow('OpenGL Python Cube')
 
        glutDisplayFunc(DrawGLScene)
        glutIdleFunc(DrawGLScene)
        glutKeyboardFunc(keyPressed)
        InitGL(GLUTwindow_height, GLUTwindow_width)
        renderPointerImage()
        glutMainLoop()
        
 

main() 