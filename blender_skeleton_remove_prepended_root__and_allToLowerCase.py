# Blender Python script - Tested with v2.70, should work with 2.6+.

import bpy

#------- FUNCTIONS ------------------------------------------------------------#

#ACT
def act():#context):
    #a = context.armature
    #print(a)
    #if a is None:
    a = bpy.data.armatures['Armature']    #TODO better use 0 as index?
    remove_pattern = "prop-"
    if not a:
        print("Armature still not found!")
        return False
    for b in a.bones:
        old_name = b.name
        print(b.name)
        if b.name.find(remove_pattern) != -1:
            print('found prepended ' + remove_pattern)
            b.name = b.name.replace(remove_pattern, "")
        #b.name = b.name.lower()
        if (old_name != b.name):
            print('bone renamed to:' + b.name)
        else:
            print('nothing to do - report bug in blenderartists or wildfireforums if you think something is wrong.\r\nhttp://www.wildfiregames.com/forum/index.php?showtopic=15552&page=19#entry286903')
        print("\r\n")
    return True


act()#context)