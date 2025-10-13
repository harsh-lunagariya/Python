# Iterator
nums = [1,2,5,7,78,54]

it = iter(nums)

for i in range(0,len(nums)):
    print(next(it))

#Generator

def gen():
    yield 1
    yield 2
    yield 3
    yield 4

#why this give me only 1 in every case : because in every time it create a new object of gen
print(gen().__next__())
print(gen().__next__())
print(gen().__next__())
print(gen().__next__())

# and this give me proper answer

var = gen()
print(var.__next__())
print(var.__next__())
print(var.__next__())
print(var.__next__())



def topten():
    n=1
    while(n<=10):
        sq = n*n
        yield sq
        n += 1

vals = topten()

for i in vals:
    print(i)

print("complete")

# custome iterator function

def listitr(lst):
    for item in lst:
        yield item

for i in listitr([1,2,4,5,10,6,7,8]):
    print(i)

# Write a custom iterator that returns the squares of odd numbers from a list, 
# skipping those divisible by 5, and stops after yielding 3 valid results.

data = [1, 3, 5, 7, 9, 10, 11]

class customeiterator:
    def __init__(self,data):
        self.data = iter(data)
        self.count = 0
        self.maxcount = 3
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.maxcount:
            raise StopIteration

        while True:
            try :
                num = next(self.data)
            except StopIteration:
                raise StopIteration
            if num%2!=0:
                sq = num**2
                if sq%5 != 0:
                    self.count +=1
                    return sq

it = customeiterator(data)
for i in it:
    print(i)
