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
    
print("lbl20 coll len = ",len(bpy.data.collections))


#https://blender.stackexchange.com/questions/34540/how-to-link-append-a-data-block-using-the-python-api ++++ +++++++++++++++
# name of collection(s) to append or link
coll_name = "Coll"

# append, set to true to keep the link to the original file
link = False 

filepath="/home/peter/POUB/Human-Visible-Project-Blender-3D/Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend"
# link all collections starting with 'MyCollection'
 
#https://b3d.interplanety.org/en/removing-collections-through-the-blender-python-api/

#del all https://docs.blender.org/api/current/bpy.data.html
   
print("lbl20 mesh len = ",len( bpy.data.meshes))
#for mesh   in bpy.data.meshes:
 #       #print mesh
  #      print( "meshh")
     #   bpy.data.meshes.remove(mesh)


#https://b3d.interplanety.org/en/removing-collections-through-the-blender-python-api/
fini=False
cpt=0
while(not(fini)):
   siz=len(bpy.data.collections)
   print("siz=",siz," cpt=",cpt)
   if(siz>0):
      coll=bpy.data.collections[cpt]
         
      for obj in coll.objects:
         bpy.data.objects.remove(obj, do_unlink=True)
         
      bpy.data.collections.remove(coll)
      #cpt+=1
   else:
      fini=True