# <pep8-80 compliant>
# <pep8-80 compliant>
import bpy


class all():
    @classmethod
    def new(cls, *args):
        return cls.data.new(*args)

    @classmethod
    def object_(cls, name, object_data):
        object = bpy.data.objects.new(name, object_data)
        bpy.context.scene.collection.objects.link(object)
        return object

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )

    @classmethod
    def make(cls, name):
        return cls.object_(name, cls.new(name))


class most(all):
    """Light data-block for lighting a scene."""
    type_ = None

    @classmethod
    def new(cls, name):
        return super().new(name, cls.type_)



class camera(all):
    """Camera data-block for storing camera settings."""
    data = bpy.data.cameras




class material(all):
    """
    Material data-block to define the appearance of geometric objects for
    rendering.
    """
    data = bpy.data.materials


class mesh(all):
    """Mesh data-block defining geometric surfaces."""
    data = bpy.data.meshes

    @classmethod
    def make(cls, name, mesh=None):
        if not mesh:
            mesh = cls.new(name)
        return cls.object_(name, mesh)


class light(most):
    """Light data-block for lighting a scene."""
    data = bpy.data.lights


class area(light):
    """Area – Directional area light source."""
    type_ = 'AREA'


class point(light):
    """Point – Omnidirectional point light source."""
    type_ = 'POINT'


class spot(light):
    """Spot – Directional cone light source."""
    type_ = 'SPOT'


class sun(light):
    """Sun – Constant direction parallel ray light source."""
    type_ = 'SUN'


class texture(most):
    """Light data-block for lighting a scene."""
    data = bpy.data.lights


class none(texture):
    """None."""
    type_ = 'NONE'


class blend(texture):
    """Blend – Procedural - create a ramp texture."""
    type_ = 'BLEND'


class clouds(texture):
    """Clouds – Procedural - create a cloud-like fractal noise texture."""
    type_ = 'CLOUDS'


class distorted_noise(texture):
    """
    Distorted Noise – Procedural - noise texture distorted by two noise
    algorithms.
    """
    type_ = 'DISTORTED_NOISE'


class image(texture):
    """Image or Movie – Allow for images or movies to be used as textures."""
    type_ = 'IMAGE'


class magic(texture):
    """Magic – Procedural - color texture based on trigonometric functions."""
    type_ = 'MAGIC'


class marble(texture):
    """
    Marble – Procedural - marble-like noise texture with wave generated bands.
    """
    type_ = 'MARBLE'


class musgrave(texture):
    """Musgrave – Procedural - highly flexible fractal noise texture."""
    type_ = 'MUSGRAVE'


class noise(texture):
    """
    Noise – Procedural - random noise, gives a different result every time, for
    every frame, for every pixel.
    """
    type_ = 'NOISE'


class stucci(texture):
    """Stucci – Procedural - create a fractal noise texture."""
    type_ = 'STUCCI'


class voronoi(texture):
    """
    Voronoi – Procedural - create cell-like patterns based on Worley noise.
    """
    type_ = 'VORONOI'


class wood(texture):
    """
    Wood – Procedural - wave generated bands or rings, with optional noise.
    """
    type_ = 'WOOD'


class image(all):
    """Image data-block referencing an external or packed image."""
    data = bpy.data.images

    @classmethod
    def new(cls, name, width, height, alpha, float_buffer, stereo3d, is_data,
            tiled):
        return super().new(
            cls.data,
            name,
            width,
            height,
            alpha,
            float_buffer,
            stereo3d,
            is_data,
            tiled,
        )
    
    @classmethod
    def load(cls, filepath, check_existing=False):
        return cls.data.load(filepath, check_existing=False)    
