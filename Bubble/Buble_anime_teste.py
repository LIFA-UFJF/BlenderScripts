# https://blender.stackexchange.com/questions/249996/how-do-i-do-animation-using-csv-file

import bpy
import csv

csvfilename = "C:/Users/rodri/Downloads/Blender_scripts/Bubble/Bubble-teste0.csv"

print(csvfilename)
object = bpy.context.active_object
object.location = (0.0,0.0,0.0)
with open(csvfilename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(csvreader):
        if i >0:
            print(i,row)
            fn = int(float(row[0])/0.1)
            #print(fn)
    #       fn = int(row[0])
            loc = ( float(row[1]) , 0.0, 0.0 )
#        rot = (float(row[4]), float(row[5]), float(row[6]))
            print(fn, loc)
            #object.location = loc
            object.scale[0] = loc[0]*0.1
            object.scale[1] = loc[0]*0.1
            object.scale[2] = loc[0]*0.1                        
    #        object.rotation_euler = rot
            object.keyframe_insert(data_path="scale", frame=fn)
#        object.keyframe_insert(data_path="rotation_euler", frame=fn)