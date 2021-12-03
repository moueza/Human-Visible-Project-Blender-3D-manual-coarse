# -*- coding: utf-8 -*
#Bl2.93.3
#10by10
#import bpy ; import os ; filename420547 = os.path.join(os.path.dirname(bpy.data.filepath), "Human-Visible-Project-Blender-3D-manual-coarseBl293curvesMERGER.py"); exec(compile(open(filename420547).read(), filename420547, 'exec'))

import os

#import Blender as b
import bpy as b
#from Blender import Library

 prenom = 88888
text = "DDDDu in %s\n" % prenom
#filename= "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/kizomba-Mervil-sem02-avance-Bl28.txt"
filename435 = "/home/peter/POUB/blender/Human-Visible-Project-Blender-3D-manual-coarseBl293curvesMERGERpoub"
#https://blenderartists.org/t/how-to-append-a-collection-with-python-in-2-80/1155113
 
#This module provides access to objects stored in .blend files. With it scripts can append from Blender files to the current scene, like the File->Append menu entry in Blender does. It allows programmers to use .blend files as data files for their scripts.


##https://docs.blender.org/api/2.33/Library-module.html#Example:
def f(name):
     open_library(name)

     def open_library(name):
       Library.Open(name)
       groups = Library.LinkableGroups()

       for db in groups:
         print("DATABLOCK %s:" % db)
         for obname in Library.Datablocks(db):
           print( obname)

       if 'Object' in groups:
         for obname in Library.Datablocks('Object'):
           Library.Load(obname, 'Object', 0) # note the 0...
         Library.Update()

       Library.Close()
       b.Redraw()

#https://blenderartists.org/t/force-view3d-refresh-blender-redraw-in-2-5/506023
#b.Window.FileSelector(f, "Choose Library", "*.blend")
#b.Window.FileSelector(f, "Choose Library", "*.blend")
#bpy.data.scenes[0].update()
#bpy.ops.scene.delete() https://docs.blender.org/api/current/bpy.ops.scene.html