from .bbpy import data


def camera(name):
    return data.camera.new(name)


class light():
    @staticmethod
    def area(name):
        return data.light.new(name, 'AREA')

    @staticmethod
    def point(name):
        return data.light.new(name, 'POINT')

    @staticmethod
    def spot(name):
        return data.light.new(name, 'SPOT')

    @staticmethod
    def sun(name):
        return data.light.new(name, 'SUN')


def material(name):
    return data.material.new(name)


def mesh(name):
    return data.mesh(name)


class texture():
    @staticmethod
    def blend(name):
        return data.texture.new(name, 'BLEND')

    @staticmethod
    def clouds(name):
        return data.texture.new(name, 'CLOUDS')

    @staticmethod
    def distorted_noise(name):
        return data.texture.new(name, 'DISTORTED_NOISE')

    @staticmethod
    def image(name):
        return data.texture.new(name, 'IMAGE')

    @staticmethod
    def magic(name):
        return data.texture.new(name, 'MAGIC')

    @staticmethod
    def marble(name):
        return data.texture.new(name, 'MARBLE')

    @staticmethod
    def musgrave(name):
        return data.texture.new(name, 'MUSGRAVE')

    def noise(name):
        return data.texture.new(name, 'NOISE')

    @staticmethod
    def none(name):
        return data.texture.new(name, 'NONE')

    @staticmethod
    def stucci(name):
        return data.texture.new(name, 'STUCCI')

    @staticmethod
    def voronoi(name):
        return data.texture.new(name, 'VORONOI')

    @staticmethod
    def wood(name):
        return data.texture.new(name, 'WOOD')
