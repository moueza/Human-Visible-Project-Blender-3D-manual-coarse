#!/bin/bash
#for illustrative image in web
#cd ~/POUB/Human-Visible-Project-Blender-3D
~/blender-2.93.4-linux-x64/blender -b  ~/POUB/Human-Visible-Project-Blender-3D/Human-Visible-Project-Blender-3D-manual-coarseBl293curves.blend -x 1  -F JPEG -f 0
mv /tmp/0000.jpg ~/POUB/Human-Visible-Project-Blender-3D/Human-Visible-Project-Blender-3D-manual-coarseBl293curves.jpg
cp  ~/POUB/Human-Visible-Project-Blender-3D/Human-Visible-Project-Blender-3D-manual-coarseBl293curves.jpg web
