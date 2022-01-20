# -*- coding: utf-8 -*
#Bl2.93.3
#10by10


#TODO delete own coll
#TODO delete img

import bpy
import os
#import bpy ; import os ; filename420547 = os.path.join(os.path.dirname(bpy.data.filepath), "Human-Visible-Project-Blender-3D-manual-coarseBl293curvesMERGER.py"); exec(compile(open(filename420547).read(), filename420547, 'exec'))
prenom = 88888
text = "DDDDu in %s\n" % prenom
#filename= "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/kizomba-Mervil-sem02-avance-Bl28.txt"
filename435 = "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/poub.txt"
 
f = open(filename435,'a')
print('lbl4')
f.write(text)
f.close
    
print("lbl20 len = ",len(bpy.data.collections))


#https://blender.stackexchange.com/questions/34540/how-to-link-append-a-data-block-using-the-python-api ++++ +++++++++++++++
# name of collection(s) to append or link
coll_name = "Coll"

# append, set to true to keep the link to the original file
link = False 

filepath="/home/peter/POUB/Human-Visible-Project-Blender-3D/Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend"
# link all collections starting with 'MyCollection'
with bpy.data.libraries.load(filepath, link=link) as (data_from, data_to):
    data_to.collections = [c for c in data_from.collections if c.startswith(coll_name)]

# link collection to scene collection
for coll in data_to.collections:
    if coll is not None:
       bpy.context.scene.collection.children.link(coll)