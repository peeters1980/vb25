'''

  V-Ray/Blender 2.5

  http://vray.cgdo.ru

  Author: Andrey M. Izrantsev (aka bdancer)
  E-Mail: izrantsev@cgdo.ru

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.

'''


''' Blender modules '''
import bpy

''' vb modules '''
from vb25.utils import *
from vb25.plugins import *


def write_UVWGenProjection(bus):
	TYPE= {
		'FLAT':   1,
		'SPHERE': 2,
		'TUBE':   3,
		'BALL':   4,
		#'CUBE':   5,
		'CUBE':   6,
		'TRI':    6,
		'PERS':   8,
	}

	ofile=   bus['files']['material']
	scene=   bus['scene']
	ob=      bus['node']['object']

	slot=    bus['mtex']['slot']
	texture= bus['mtex']['texture']
	uvwgen=  bus['mtex']['name'] + 'UVP'

	VRayTexture= texture.vray
	if VRayTexture.object:
		texture_object= get_data_by_name(sce, 'objects', VRayTexture.object)
		if texture_object:
			ob= texture_object

	ofile.write("\nUVWGenProjection %s {" % uvwgen)
	ofile.write("\n\ttype= %d;" % TYPE[VRayTexture.mapping])
	if ob:
		uvw_transform= mathutils.Matrix.Rotation(math.radians(90.0), 4, 'X')
		uvw_transform*= ob.matrix_world.copy().inverted()
		ofile.write("\n\tuvw_transform= %s; // %s" % a(sce,transform(uvw_transform)), ob.name)
	ofile.write("\n}\n")

	return uvwgen


def write_UVWGenChannel(params):
	ofile= bus['files']['textures']
	sce=   bus['scene']

	slot=     bus['mtex']['slot']
	texture=  bus['mtex']['texture']
	uvw_name= bus['mtex']['name'] + 'UVC'

	VRaySlot=    texture.vray_slot
	VRayTexture= texture.vray
	
	uvw_channel= 1
	if slot:
		uvw_channel= get_uv_layer_id(bus['uvs'], slot.uv_layer)
		
	uvwgen= write_UVWGenProjection(ofile, sce, params) if VRayTexture.texture_coords == 'ORCO' else None

	ofile.write("\nUVWGenChannel %s {" % uvw_name)
	ofile.write("\n\tuvw_channel= %i;" % uvw_channel)
	if hasattr(texture,'use_mirror_x'):
		ofile.write("\n\twrap_u= %d;" % (2 if texture.use_mirror_x else 0))
		ofile.write("\n\twrap_v= %d;" % (2 if texture.use_mirror_y else 0))
	if hasattr(texture,'repeat_x'):
		ofile.write("\n\tuvw_transform= interpolate((%i, Transform(" % sce.frame_current)
		ofile.write("\n\t\tMatrix(")
		ofile.write("\n\t\t\tVector(1.0,0.0,0.0)*%.3f," % (texture.repeat_x if VRayTexture.tile in ('TILEUV','TILEU') else 1.0))
		ofile.write("\n\t\t\tVector(0.0,1.0,0.0)*%.3f," % (texture.repeat_y if VRayTexture.tile in ('TILEUV','TILEV') else 1.0))
		ofile.write("\n\t\t\tVector(0.0,0.0,1.0)")
		ofile.write("\n\t\t),")
		ofile.write("\n\t\tVector(%.3f,%.3f,0.0)" % ((slot.offset[0], slot.offset[1]) if slot else (1.0,1.0)))
		ofile.write("\n\t)));")
	if uvwgen:
		ofile.write("\n\tuvwgen= %s;" % uvwgen)
	ofile.write("\n}\n")

	bus['material']['normal_uvwgen']= uvwgen

	return uvw_name


def write_UVWGenEnvironment(params):
	MAPPING_TYPE= {
		'SPHERE':  'spherical',
		'ANGULAR': 'angular',
		'SCREEN':  'screen',
		'TUBE':    'max_cylindrical',
		'CUBIC':   'cubic',
		'MBALL':   'mirror_ball',
	}

	slot= params.get('slot')
	texture= params.get('texture')

	VRaySlot=    texture.vray_slot
	VRayTexture= texture.vray

	uvw_name= bus['name'] + 'UVE'
	
	ofile.write("\nUVWGenEnvironment %s {" % uvw_name)
	if 'rotate' in params:
		ofile.write("\n\tuvw_matrix= %s;" % transform(mathutils.Matrix.Rotation(math.radians(bus['rotate']['angle']), 4, bus['rotate']['axis'])))
	ofile.write("\n\tmapping_type= \"%s\";" % MAPPING_TYPE[VRayTexture.environment_mapping])
	ofile.write("\n}\n")
	
	return uvw_name