import os
import sys

import bpy

WINGHOME = R"C:\Program Files\Wing Pro 9"
os.environ["WINGHOME"] = WINGHOME

if WINGHOME not in sys.path:
    sys.path.append(WINGHOME)

wingdbstub = __import__("wingdbstub")
wingdbstub.Ensure()

bpy.ops.celestine.register('INVOKE_DEFAULT')

viewer = __import__("viewer")
viewer.main(sys.path[0], ["blender", "main"], False)
