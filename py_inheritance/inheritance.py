class A:
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('feature 2 is working')


class B(A):
    def feature3(self):
        print('feature 3 is working')




a1 = A()      
a1.feature1()


b1 = B()
b1.feature3()
b1.feature1()
