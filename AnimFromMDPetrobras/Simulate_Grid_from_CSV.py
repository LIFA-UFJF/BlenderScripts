# https://blender.stackexchange.com/questions/249996/how-do-i-do-animation-using-csv-file

import bpy
import csv
import bmesh
from mathutils import Vector
import itertools

path = "C:/Users/rodri/Downloads/Blender_scripts/AnimFromMDPetrobras/"
csvfilename = path+"2025_02_22-10_00_31_AM/data/paraview/paraview_data_t000220.csv"

print(csvfilename)
xyz_data = []
vxvyvz_data = []
tipo_data = []
mass_data = []

with open(csvfilename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(csvreader):
        if i == 0:
            print(i,row)
        else:
            #print(i,row)            
            # 'x', 'y', 'z', 'vx', 'vy', 'vz', 'rho', 'press', 'tipo', 'mass'
            xi,yi,zi = float(row[0]),float(row[1]),float(row[2])
            vxi,vyi,vzi = float(row[3]),float(row[4]),float(row[5])
            rhoi,pressi = float(row[6]),float(row[7])
            tipoi,massi = int(row[8]),float(row[9])
            
            xyz_data.append( (xi,yi,zi) )
            vxvyvz_data.append( (vxi,vyi,vzi) )
            tipo_data.append( tipoi )
            mass_data.append( massi )
            
            #bpy.ops.mesh.primitive_uv_sphere_add(radius=2, enter_editmode=False, align='WORLD', location=(xi,yi,zi), scale=(1, 1, 1))


            #fn = int(float(row[0])/0.1)
            #print(fn)
    #       fn = int(row[0])
            #loc = ( float(row[1]) , 0.0, 0.0 )
#        rot = (float(row[4]), float(row[5]), float(row[6]))
            #print(fn, loc)
            #object.location = loc
            #object.scale[0] = loc[0]*0.1
            #object.scale[1] = loc[0]*0.1
            #object.scale[2] = loc[0]*0.1                        
    #        object.rotation_euler = rot
            #object.keyframe_insert(data_path="scale", frame=fn)
#        object.keyframe_insert(data_path="rotation_euler", frame=fn)


vertices = xyz_data
xyz_data0 = []
xyz_data1 = []
xyz_data3 = []
xyz_data7 = []

# create and add a vertices
for i,coord in enumerate(xyz_data):
    print(tipo_data[i])
    if (tipo_data[i]==0):
        xyz_data0.append(coord)
    elif (tipo_data[i]==1):
        xyz_data1.append(coord)
    elif (tipo_data[i]==3):
        xyz_data3.append(coord)
    elif (tipo_data[i]==7):
        xyz_data7.append(coord)



#obj_name = "walls0"

obj_name = "water1"

# create the mesh data
mesh_data = bpy.data.meshes.new(f"{obj_name}_data")

# create the mesh object using the mesh data
mesh_obj = bpy.data.objects.new(obj_name, mesh_data)

# add the mesh object into the scene
bpy.context.scene.collection.objects.link(mesh_obj)

# create a new bmesh
bm = bmesh.new()

# Criar vértices no BMesh
vertices = [bm.verts.new(p) for p in xyz_data1]
bm.verts.ensure_lookup_table()

max_distance = 1.5

# Conectar vértices que estão dentro da distância máxima
for v1, v2 in itertools.combinations(vertices, 2):
    if (v1.co - v2.co).length <= max_distance:
        bm.edges.new((v1, v2))

#for vert_indices in face_vert_indices:
#    bm.faces.new([bm.verts[index] for index in vert_indices])

# writes the bmesh data into the mesh data
bm.to_mesh(mesh_data)

# [Optional] update the mesh data (helps with redrawing the mesh in the viewport)
mesh_data.update()

# clean up/free memory that was allocated for the bmesh
bm.free()