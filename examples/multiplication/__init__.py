import examples.multiplication.multiply_generator_point as mgp
from tinyec.ec import SubGroup, Curve


if __name__ == '__main__':
    field = SubGroup(p=17, g=(15, 13), n=18, h=1)
    curve = Curve(a=0, b=7, field=field, name='curve')
    print('curve:', curve)
    print('generator: ', curve.g)
    print('cyclic order: ', curve.field.n)

    mgp.multiply_by_all_factors(18, curve)
