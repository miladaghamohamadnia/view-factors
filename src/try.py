import OpenGL,sys,os,traceback
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.EXT.framebuffer_object import *
from OpenGL.GL.ARB.framebuffer_object import *
import numpy as np
import random

import trimesh 
mesh = trimesh.load('C:\\Users\\Casti\\projects\\temporary\\Radiosity\\3Dscenes\\test.obj')

print(mesh.faces.shape)
print(mesh.faces[0])

print(mesh.face_normals.shape)
print(mesh.vertices.shape)




GLUTwindow_width, GLUTwindow_height = 500,500

def drawFilled(verts, norms, drawNormal = True, doLighting = True, useTexture = True):
  for v in verts:
    # if useTexture:
    #   glTexCoord2f(v.texCoords[0], v.texCoords[1])
    # elif v.color:
    #   glColor3f(v.color[0], v.color[1], v.color[2])
    print("****************")
    print(v, norms)
    # glNormal3fv(norms)
    glVertex3fv(v)

def renderPointerImage():
  PointerDisplayList = -1
  if PointerDisplayList != -1: #Deallocate previous display list
    glDeleteLists(PointerDisplayList, 1)
  PointerDisplayList = glGenLists(1)
  glNewList(PointerDisplayList, GL_COMPILE)
  glDisable(GL_LIGHTING)
  # #Render all tiles with the color of their index in the tiles list
  # for tile in range(len(mesh.faces)):
  for tile in range(10):
    #Now split the integer ID into 4 separate bytes
    f = mesh.faces[tile]
    V = [mesh.vertices[i] for i in f]
    N = mesh.face_normals[tile]
    [R, G, B, A] = [random.randint(0,222), 12, 222, 250]
    # glColor4fv([R/255, G/255, B/255, A/255])
    glColor4fv([1,1,1,1])
    for v in V:
      print("****************")
      print(v, N)
      # glNormal3fv(N)
      glVertex3fv(v)
  glEndList()
  glCallList(PointerDisplayList)


def GLUTRedraw():
  glClearColor(0.0, 0.0, 0.0, 0.0)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  # glViewport(0, 0, GLUTwindow_width, GLUTwindow_height)
  # glScissor(0, 0, GLUTwindow_width, GLUTwindow_height)

  #Set up projection and modelview matrices
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glTranslatef(0.0,0.0,-6.0)
  # frustW, nearDist, farDist = 0.1, 0.2, 10
  # glFrustum(-frustW, frustW, -frustW, frustW, nearDist, farDist)
  # glLightfv(GL_LIGHT0, GL_POSITION, [3.0, 4.0, 5.0, 0.0]);
  # glLightfv(GL_LIGHT1, GL_POSITION,  [-3.0, -2.0, -3.0, 0.0]);
  
  # glEnable(GL_LIGHTING)

  #self.radiosity.renderPointerImage()
  #self.radiosity.scene.renderGL()
  renderPointerImage()
  glutSwapBuffers()


def initGL():
  glutInit('')
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowSize(GLUTwindow_width, GLUTwindow_height)
  glutInitWindowPosition(50, 50)
  glutCreateWindow('Viewer')
  # glutReshapeFunc(self.GLUTResize)
  glutDisplayFunc(GLUTRedraw)
  # glutIdleFunc(GLUTRedraw)
  # glutKeyboardFunc(self.GLUTKeyboard)
  # glutKeyboardUpFunc(self.GLUTKeyboardUp)
  # glutSpecialFunc(self.GLUTSpecial)
  # glutSpecialUpFunc(self.GLUTSpecialUp)
  # glutMouseFunc(self.GLUTMouse)
  # glutMotionFunc(self.GLUTMotion)
  
  # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
  # glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
  # glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
  # glEnable(GL_LIGHT0)
  # glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
  # glEnable(GL_LIGHT1)
  # glEnable(GL_NORMALIZE)
  # glEnable(GL_LIGHTING)
  
  # glEnable(GL_DEPTH_TEST)
  
  glutMainLoop()

initGL()







#This function pushes a matrix onto the stack that puts everything
#in the frame of a camera which is centered at position "P",
#is pointing towards "t", and has vector "r" to the right
#t - towards vector
#u - up vector
#r - right vector
#P - Camera center
def gotoCameraFrame(t, u, r, P):
	rotMat = Matrix4([r.x, u.x, -t.x, 0, r.y, u.y, -t.y, 0, r.z, u.z, -t.z, 0, 0, 0, 0, 1])
	rotMat = rotMat.Inverse()
	transMat = Matrix4([1, 0, 0, -P.x, 0, 1, 0, -P.y, 0, 0, 1, -P.z, 0, 0, 0, 1])
	#Translate first then rotate
	mat = rotMat*transMat
	#OpenGL is column major and mine are row major so take transpose
	mat = mat.Transpose()
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glMultMatrixd(mat.m)






# glBegin(GL_POLYGON)

# Rclear, Gclear, Bclear, Aclear = [244,244,244,255]
# glClearColor(Rclear, Gclear, Bclear, Aclear)
# glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# xdim, ydim = 300,300
# glViewport(0, 0, xdim, ydim)
# glScissor(0, 0, xdim, ydim)
# glMatrixMode(GL_PROJECTION)
# glLoadIdentity()
# glFrustum(-frustW, frustW, -frustW, frustW, self.hemicube.nearDist, self.hemicube.farDist)
# gotoCameraFrame(t, u, r, P)











