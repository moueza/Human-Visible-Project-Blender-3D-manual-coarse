# -*- coding: utf-8 -*
#Bl2.93.3
#10by10
#https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3
#text edit http://jmsoler.free.fr/didacticiel/blender/tutor/python_script00_en.htm

#py  https://docs.blender.org/api/current/info_quickstart.html
#concat https://stackoverflow.com/questions/20441035/unsupported-operand-types-for-int-and-str#jkhk

#https://stackoverflow.com/questions/11604548/running-python-script-in-blender
#filename = "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/kizomba-Mervil-sem02-avance-Bl28.py"
#exec(compile(open(filename).read(), filename, 'exec'))
#

# import bpy ; import os ; filename420547 = os.path.join(os.path.dirname(bpy.data.filepath), "kizomba-Mervil-sem02-avance-Bl28.py"); exec(compile(open(filename420547).read(), filename420547, 'exec'))

#male armature color ? In pose mode, assign
#IPO above 120 ? Photocopies output...end : 120->180


#print(n,n+1 ,  " neutralisation")

#quaternions : 


#save
#from https://github.com/moueza/covid19-corona-virus-scilab/blob/master/PYTHON/time_series_covid19_confirmed_global.py
#from Magazine Linux magazine blue HS 40 H p84
prenom = 88888
text = "DDDDu in %s\n" % prenom
#filename= "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/kizomba-Mervil-sem02-avance-Bl28.txt"
filename435 = "/home/peter/POUB/blender/DANSE/kizombaSemba/COURS/poub.txt"
#concat + and str()
#with open('./'+kizomba-Mervil-sem02-avance-Bl28+'.txt') as csv_fileConfirmed:
            #csv_reader = csv.reader(csv_fileConfirmed, delimiter=',')
#https://stackoverflow.com/questions/31414263/python-using-open-w-filenotfounderror
#l=str(line[0])+','+str(line[1])+','+str(line[2])+'\n'
f = open(filename435,'a')
print('lbl4')
f.write(text)
f.close
            #line_count = 0
            # print(f'longh = {line_count.length}')
            # print(f'longh = {len(line_count)}') KO
            # print(len(csv_reader)) KO
            # https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
            #matt = np.matrix('1 2; 3 4')
      
            #arrayMoi = []
            #for roww in csv_reader:
                #if line_count != 0:
                    #print(f'\t {line_count} {roww[1]} {int(roww[4]) + 1000}')
fileRef="Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend"
print(len(bpy.data.collections))
#delete already ancient collections

for collection in bpy.data.collections :
   bpy.data.collections.remove(collection)
   print(collection.name) 
   #or index  
   if (collection.name.find('Coll', 0, 50)):
        bpy.data.collections.remove(collection)
        print(True)
        #https://b3d.interplanety.org/en/removing-collections-through-the-blender-python-api/
        for obj in collection.objects:
           bpy.data.objects.remove(obj, do_unlink=True)    
           bpy.data.collections.remove(collection)
   else:
        print(False)
        
#print(bpy.data.collections[2])
