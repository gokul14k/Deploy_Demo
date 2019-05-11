class A():


    def factorial(self,n):

        if not isinstance(n, int):
            print('Factorial is only defined for integers.')
            return None
        elif n<0:
            print("Factorial is only defined for Positive Numbers")
        elif n == 0:
            return 1
        else:
            space = ' ' * (4 * n)
            print(space, 'factorial', n)
            recurse = self.factorial(n - 1)
            #print(recurse)
            result = n * recurse
            print(space, 'returning', result)
            return result

    def a(self):
        Final_Result=self.factorial(4)
        print ("Final_Result : ",Final_Result)

A().a()