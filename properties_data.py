'''

 V-Ray/Blender 2.5

 http://vray.cgdo.ru

 Author: Andrey M. Izrantsev (aka bdancer)
 E-Mail: izrantsev@gmail.com

 This plugin is protected by the GNU General Public License v.2

 This program is free software: you can redioutibute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is dioutibuted in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

 All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Group

'''


''' Python modules '''
import os

''' Blender modules '''
import bpy
from bpy.props import *

''' vb modules '''
from vb25.utils import *


class VRayData(bpy.types.IDPropertyGroup):
    pass

bpy.types.Mesh.vray= PointerProperty(
	name= "V-Ray Object Data Settings",
	type=  VRayData,
	description= "V-Ray object data settings."
)

bpy.types.Curve.vray= PointerProperty(
	name= "V-Ray Object Data Settings",
	type=  VRayData,
	description= "V-Ray object data settings."
)


'''
  Plugin: GeomMeshFile
'''
class GeomMeshFile(bpy.types.IDPropertyGroup):
    pass

VRayData.GeomMeshFile= PointerProperty(
	name= "V-Ray Proxy",
	type=  GeomMeshFile,
	description= "V-Ray proxy settings."
)

# GeomMeshFile.BoolProperty(
# 	attr= 'use',
# 	name= "Use Proxy",
# 	description= "Use proxy mesh.",
# 	default= False
# )

# GeomMeshFile.StringProperty(
# 	attr= 'file',
# 	name= "File",
# 	subtype= 'FILE_PATH',
# 	description= "Proxy file."
# )

# GeomMeshFile.EnumProperty(
# 	attr= 'anim_type',
# 	name= "Animation type",
# 	description= "Proxy animation type.",
# 	items=(
# 		("LOOP",     "Loop",      "TODO."),
# 		("ONCE",     "Once",      "TODO."),
# 		("PINGPONG", "Ping-pong", "TODO."),
# 		("STILL",    "Still",     "TODO.")
# 	),
# 	default= "LOOP"
# )

# GeomMeshFile.FloatProperty(
# 	attr= 'anim_speed',
# 	name= "Speed",
# 	description= "Animated proxy playback speed.",
# 	min=0.0, max=1000.0,
# 	soft_min=0.0, soft_max=1.0,
# 	default= 1.0
# )

# GeomMeshFile.FloatProperty(
# 	attr= 'anim_offset',
# 	name= "Offset",
# 	description= "Animated proxy initial frame offset.",
# 	min=0.0, max=1000.0,
# 	soft_min=0.0, soft_max=1.0,
# 	default= 0.0
# )

# GeomMeshFile.FloatProperty(
# 	attr= 'scale',
# 	name= "Scale",
# 	description= "Size scaling factor.",
# 	min=0.0, max=1000.0,
# 	soft_min=0.0, soft_max=2.0,
# 	default= 1.0
# )

# GeomMeshFile.BoolProperty(
# 	attr= 'apply_transforms',
# 	name= "Apply transform",
# 	description= "Apply rotation and location.",
# 	default= False
# )

# GeomMeshFile.BoolProperty(
# 	attr= 'apply_scale',
# 	name= "Apply scale",
# 	description= "Apply scale.",
# 	default= True
# )

GeomMeshFile.use= BoolProperty(
	name= "Use Proxy",
	description= "Use proxy mesh.",
	default= False
)

GeomMeshFile.file= StringProperty(
	name= "File",
	subtype= 'FILE_PATH',
	description= "Proxy file."
)

GeomMeshFile.anim_type= EnumProperty(
	name= "Animation type",
	description= "Proxy animation type.",
	items= (
		('LOOP',"Loop","TODO."),
		('ONCE',"Once","TODO."),
		('PINGPONG',"Ping-pong","TODO."),
		('STILL',"Still","TODO.")
	),
	default= "LOOP"
)

GeomMeshFile.anim_speed= FloatProperty(
	name= "Speed",
	description= "Animated proxy playback speed.",
	min= 0.0,
	max= 1000.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 1.0
)

GeomMeshFile.anim_offset= FloatProperty(
	name= "Offset",
	description= "Animated proxy initial frame offset.",
	min= 0.0,
	max= 1000.0,
	soft_min= 0.0,
	soft_max= 1.0,
	default= 0.0
)

GeomMeshFile.scale= FloatProperty(
	name= "Scale",
	description= "Size scaling factor.",
	min= 0.0,
	max= 1000.0,
	soft_min= 0.0,
	soft_max= 2.0,
	default= 1.0
)

GeomMeshFile.apply_transforms= BoolProperty(
	name= "Apply transform",
	description= "Apply rotation and location.",
	default= False
)

GeomMeshFile.apply_scale= BoolProperty(
	name= "Apply scale",
	description= "Apply scale.",
	default= True
)



'''
  GUI
'''
import properties_data_mesh
properties_data_mesh.DATA_PT_context_mesh.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_normals.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_settings.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_shape_keys.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_texface.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_uv_texture.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_vertex_colors.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_vertex_groups.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.MESH_MT_shape_key_specials.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.MESH_MT_vertex_group_specials.COMPAT_ENGINES.add('VRAY_RENDER')
properties_data_mesh.DATA_PT_context_mesh.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_normals.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_settings.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_shape_keys.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_texface.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_uv_texture.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_vertex_colors.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.DATA_PT_vertex_groups.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.MESH_MT_shape_key_specials.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
properties_data_mesh.MESH_MT_vertex_group_specials.COMPAT_ENGINES.add('VRAY_RENDER_PREVIEW')
del properties_data_mesh


narrowui= 200



def base_poll(cls, context):
	rd= context.scene.render
	return (context.mesh) and (rd.engine in cls.COMPAT_ENGINES)


class DataButtonsPanel():
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'data'


class DATA_PT_vray_proxy(DataButtonsPanel, bpy.types.Panel):
	bl_label = "Proxy"
	bl_default_closed = True
	
	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		return base_poll(__class__, context)

	def draw_header(self, context):
		ob= context.mesh.vray.GeomMeshFile
		self.layout.prop(ob, 'use', text="")

	def draw(self, context):
		ob= context.mesh.vray.GeomMeshFile

		layout= self.layout

		wide_ui= context.region.width > narrowui

		layout.active= ob.use

		split= layout.split()
		col= split.column()
		col.prop(ob, 'file')

		split= layout.split()
		col= split.column()
		col.prop(ob, 'anim_type')

		split= layout.split()
		col= split.column()
		col.prop(ob, 'anim_speed')
		if wide_ui:
			col= split.column()
		col.prop(ob, 'anim_offset')

		split= layout.split()
		col= split.column()
		col.label(text="Proxy generation:")
		split= layout.split()
		split.active= False
		col= split.column()
		col.operator('vray_create_proxy')
		if wide_ui:
			col= split.column()
		col.operator('vray_replace_with_proxy', text="Replace with proxy")

		split= layout.split()
		split.active= False
		col= split.column()
		col.prop(ob, 'apply_transforms')
		if wide_ui:
			col= split.column()
		col.prop(ob, 'apply_scale')