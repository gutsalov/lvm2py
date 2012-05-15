#This file is part of lvm2py.

#lvm2py is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#lvm2py is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with lvm2py. If not, see <http://www.gnu.org/licenses/>.

from ctypes import *
from . import lvmlib, lvm_t

class volume_group(Structure):
    pass

vg_t = POINTER(volume_group)

class physical_volume(Structure):
    pass

pv_t = POINTER(physical_volume)

class dm_list(Structure):
    pass

dm_list._fields_ = [('n', POINTER(dm_list)), ('p', POINTER(dm_list))]

class lvm_str_list(Structure):
    _fields_ = [
        ('list', dm_list),
        ('str', c_char_p),
    ]

lvm_str_list_t = lvm_str_list

class lvm_pv_list(Structure):
    _fields_ = [
        ('list', dm_list),
        ('pv', pv_t),
    ]

lvm_pv_list_t = lvm_pv_list

version = lvmlib.lvm_library_get_version
version.restype = c_char_p
lvm_quit = lvmlib.lvm_quit
lvm_quit.argtypes = [lvm_t]
lvm_scan = lvmlib.lvm_scan
lvm_scan.argtypes = [lvm_t]
lvm_list_vg_names = lvmlib.lvm_list_vg_names
lvm_list_vg_names.argtypes = [lvm_t]
lvm_list_vg_names.restype = POINTER(dm_list)
dm_list_empty = lvmlib.dm_list_empty
dm_list_empty.argtypes = [POINTER(dm_list)]
lvm_quit.argtypes = [lvm_t]
dm_list_start = lvmlib.dm_list_start
dm_list_start.argtypes = [POINTER(dm_list), POINTER(dm_list)]
dm_list_end = lvmlib.dm_list_end
dm_list_end.argtypes = [POINTER(dm_list), POINTER(dm_list)]

# VG Functions
lvm_vg_create = lvmlib.lvm_vg_create
lvm_vg_create.argtypes = [lvm_t, c_char_p]
lvm_vg_create.restype = vg_t
lvm_vg_open = lvmlib.lvm_vg_open
lvm_vg_open.argtypes = [lvm_t, c_char_p, c_char_p]
lvm_vg_open.restype = vg_t
lvm_vg_write = lvmlib.lvm_vg_write
lvm_vg_write.argtypes = [vg_t]
lvm_vg_remove = lvmlib.lvm_vg_remove
lvm_vg_remove.argtypes = [vg_t]
lvm_vg_close = lvmlib.lvm_vg_close
lvm_vg_close.argtypes = [vg_t]
lvm_vg_extend = lvmlib.lvm_vg_extend
lvm_vg_extend.argtypes = [vg_t, c_char_p]
lvm_vg_get_uuid = lvmlib.lvm_vg_get_uuid
lvm_vg_get_uuid.argtypes = [vg_t]
lvm_vg_get_uuid.restype = c_char_p
lvm_vg_get_name = lvmlib.lvm_vg_get_name
lvm_vg_get_name.argtypes = [vg_t]
lvm_vg_get_name.restype = c_char_p
lvm_vg_get_size = lvmlib.lvm_vg_get_size
lvm_vg_get_size.argtypes = [vg_t]
lvm_vg_get_size.restype = c_ulonglong
lvm_vg_get_free_size = lvmlib.lvm_vg_get_free_size
lvm_vg_get_free_size.argtypes = [vg_t]
lvm_vg_get_free_size.restype = c_ulonglong
lvm_vg_get_extent_size = lvmlib.lvm_vg_get_extent_size
lvm_vg_get_extent_size.argtypes = [vg_t]
lvm_vg_get_extent_size.restype = c_ulonglong
lvm_vg_get_extent_count = lvmlib.lvm_vg_get_extent_count
lvm_vg_get_extent_count.argtypes = [vg_t]
lvm_vg_get_extent_count.restype = c_ulonglong
lvm_vg_get_free_extent_count = lvmlib.lvm_vg_get_free_extent_count
lvm_vg_get_free_extent_count.argtypes = [vg_t]
lvm_vg_get_free_extent_count.restype = c_ulonglong
lvm_vg_get_pv_count = lvmlib.lvm_vg_get_pv_count
lvm_vg_get_pv_count.argtypes = [vg_t]
lvm_vg_get_pv_count.restype = c_ulonglong
lvm_vg_get_max_pv = lvmlib.lvm_vg_get_max_pv
lvm_vg_get_max_pv.argtypes = [vg_t]
lvm_vg_get_max_pv.restype = c_ulonglong
lvm_vg_get_max_lv = lvmlib.lvm_vg_get_max_lv
lvm_vg_get_max_lv.argtypes = [vg_t]
lvm_vg_get_max_lv.restype = c_ulonglong
lvm_vgname_from_device = lvmlib.lvm_vgname_from_device
lvm_vgname_from_device.argtypes = [vg_t, c_char_p]
lvm_vgname_from_device.restype = c_char_p
lvm_vg_list_pvs = lvmlib.lvm_vg_list_pvs
lvm_vg_list_pvs.argtypes = [vg_t]
lvm_vg_list_pvs.restype = POINTER(dm_list)

# PV Functions
lvm_pv_get_name = lvmlib.lvm_pv_get_name
lvm_pv_get_name.argtypes = [pv_t]
lvm_pv_get_name.restype = c_char_p