from tinyec.ec import SubGroup, Curve
from tinyec import registry
import examples.keys.key_generator as kg

if __name__ == '__main__':
    test_field = SubGroup(p=17, g=(15, 13), n=18, h=1)
    test_curve = Curve(a=0, b=7, field=test_field, name='test_curve')
    print(test_curve)

    # to see all possible curves open registry.py
    # real_life_curve = registry.get_curve('brainpoolP256r1')
    # print(real_life_curve)

    (private, public) = kg.generate_key_pair(test_curve)
    shared_secret = kg.generate_shared_secret(test_curve)

    print('private key = ', private)
    print('public key = ', public)
    print('shared secret = ', shared_secret)

