# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FatherA:

    def __init__(self):
        print('init action in father class A')


class SubClassB(FatherA):

    def __init__(self):
        print('init action in subclass B')
        super(SubClassB, self).__init__()  # 在子类中调用父类的方法：super().方法名称(参数)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    b = SubClassB()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
