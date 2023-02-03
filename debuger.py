import os
import sys

import bpy

WINGHOME = R"C:\Program Files\Wing Pro 9"
os.environ["WINGHOME"] = WINGHOME

if WINGHOME not in sys.path:
    sys.path.append(WINGHOME)

wingdbstub = __import__("wingdbstub")
wingdbstub.Ensure()

bpy.ops.celestine.start('INVOKE_DEFAULT')

celestine = __import__("celestine")
celestine.main(["-a", "demo", "-i", "blender", "main"], False)
