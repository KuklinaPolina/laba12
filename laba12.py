def a12():
    class Restaurant:
        def __init__(self, rn, ct):
            self.rn = rn
            self.ct = ct
        def describe_restaurant(self):
            print("Restaurant name: ", self.rn)
            print("Cuisine type: ", self.ct)
    nRe = Restaurant("LALALA", "Italian")
    class IceCreamStand(Restaurant):
        def __init__(self, rn, ct):
            super().__init__(rn, ct)
            self.v = ['vanilla', 'chocolate', 'strawberry']
        def f(self):
            print("Dostypnie vkusi:")
            for v in self.v:
                print(" - ", v)
    s = IceCreamStand("Morogenoe", "Ice Cream")
    print("Restaurant name:", s.rn)
    print("Cuisine type:", s.ct)
    s.f()
def b12():
    class Restaurant:
        def __init__(self, rn, ct):
            self.rn = rn
            self.ct = ct
        def describe_restaurant(self):
            print("Restaurant name: ", self.rn)
            print("Cuisine type: ", self.ct)
    class IceCreamStand(Restaurant):
        def __init__(self, rn, ct, l, h):
            super().__init__(rn, ct)
            self.l = l
            self.h = h
            self.v = ['vanilla', 'chocolate', 'strawberry', 'mint']

        def nv(self, v):
            self.v.append(v)
            print(f"{v} vkuca net v nalichii")

        def rv(self, v):
            if v in self.v:
                self.v.remove(v)
                print(f"{v} ydalion iz cpicka")
            else:
                print(f"{v} vkuca net v nalichii")

        def cv(self, v):
            if v in self.v:
                print(f"{v} morogenoe ect v nalichii")
            else:
                print(f"{flavor} morogenoe net v nalichii")

        def eskimo(self):
            print("Morogenoe na palochke")

        def ctakanchik(self):
            print("Morogenoe v ctakanchike")

        def zakaz(self, type):
            if type == "eskimo":
                print("Morogenoe na palochke")
            elif type == "ctakanchik":
                print("Morogenoe v ctakanchike")
            else:
                print("Net takogo morogenogo")
    s = IceCreamStand("Moroshka", "Ice Cream", "Zvioznay 5", "9:00 - 21:00")
    s.nv("caramel")
    s.rv("strawberry")
    s.cv("chocolate")
    s.eskimo()
    s.ctakanchik()
    s.zakaz("stick")
b12()