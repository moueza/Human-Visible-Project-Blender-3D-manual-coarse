# -*- coding: utf-8 -*
#Bl2.93.3
#10by10

import bpy
import os
 
prenom = 88888
text = "DDDDu in %s\n" % prenom
#filename= "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/kizomba-Mervil-sem02-avance-Bl28.txt"
filename435 = "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/poub.txt"
 
f = open(filename435,'a')
print('lbl4')
f.write(text)
f.close
    
fileRef="Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend"
print("lbl20 len = ",len(bpy.data.collections))



#delete already ancient collections
#generate for test
for collection in bpy.data.collections :
   print(collection.name) 
   #bpy.data.collections.remove(collection)
   #or index       
   if (not(-1 == collection.name.find('Coll'))):
        print(True)
        #https://b3d.interplanety.org/en/removing-collections-through-the-blender-python-api/
        for obj in collection.objects:
           #lbl45
           bpy.data.objects.remove(obj, do_unlink=True)    
        bpy.data.collections.remove(collection)
           #lbl45
           

   else:
        print(False)
   
#print(bpy.data.collections[2])



#import APPEND https://b3d.interplanety.org/en/how-to-append-an-object-from-another-blend-file-to-the-scene-using-the-blender-python-api/
filepath = "/home/peter/POUB/Human-Visible-Project-Blender-3D/Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend"
#file_path = 'D:/11.blend'bpy.ops.wm.append( filename="Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend")
#inner_path = 'Collection'
#object_name = 'Suzanne'
#bpy.ops.wm.append(
#    filepath=os.path.join(file_path, inner_path, object_name),
#    directory=os.path.join(file_path, inner_path),
#    filename=object_name
#    )

#blender python api objects of another file
#https://blender.stackexchange.com/questions/75746/import-multiple-objects-using-python
#    ancien lib doc   https://docs.blender.org/api/blender_python_api_current/bpy.types.BlendDataLibraries.html?highlight=blenddatalibraries
#    modern lib doc https://docs.blender.org/api/current/bpy.types.BlendDataLibraries.html
with bpy.data.libraries.load(filepath) as (data_from, data_to):
    #data_to.objects = [name for name in data_from.objects if name.startswith("house")]
    data_to.objects = [name for name in data_from.objects ]

# link them to scene
scene = bpy.context.scene
for obj in data_to.objects:
    if obj is not None:
        scene.objects.link(obj)