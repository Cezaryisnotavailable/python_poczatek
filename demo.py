# print(dir(2))
# print(type(dir(2)))
#
#
#
# class Test:
#     @staticmethod
#     def testing():
#         pass
#
# test = Test
# test.testing()
import os


def first():
    print(1)
    return True


def second():
    print(2)
    return False


def third():
    print(3)
    return False


first() and second() and third()

print(bool([]))

pre_project_root = os.path.abspath(__file__)
print(pre_project_root)
project_root = os.path.dirname(os.path.abspath(__file__))
print(project_root)
base_dir = os.path.dirname(project_root)
print(base_dir)
temp = os.path.dirname(base_dir)
print(temp)

