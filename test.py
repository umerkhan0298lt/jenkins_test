class power:
    def set_base(self,x):
        self.__base = x
    def set_exponent(self, y):
        self.__exponent = y
    def get_base():
        print(self.__base)
    def get_exponent():
        print(self.__exponent)
    def find_power(self):
        result = 1
        for i in range(self.__exponent):
            result = result*self.__base
        print(result)

p1 = power()
p1.set_base(3)
p1.set_exponent(2)
p1.get_base
p1.get_exponent
p1.find_power()

# l = ["apple", "banana", "orange", "cake"]
# m = [5,2,3,2,4,7,8,8]
# print(l+m)
# l.insert(3,"kchnh")
# # l.remove("apple")
# l.pop()
# # del(l[1:2])
# print(l)
    
# l = [5,6,8,9,2,1]
# l.sort()
# print(l)
# l.remove(5)
# print(l)
# l.append(10)
# print(l)
# l.reverse()
# print(l)
# l[3:] = []
# l[:2] = []
# print(l)



# l.insert(2, 56)
# print(l)


l = ["apple", "banana",5,6,8,9,2,1, "orange", "cake"] 
int_arr = []
char_arr = []
for i in l:
    if type(i) == int:
        int_arr.append(i)
    else:
        char_arr.append(i)

print(int_arr)
print(char_arr)

char_arr.sort()
print(char_arr)
char_arr.reverse()
print(char_arr)

int_arr.sort()
print(int_arr)
int_arr.reverse()
print(int_arr)



for i in range(0,6,2):
    print(i)