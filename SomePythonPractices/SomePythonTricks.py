#Some consise but might be useful Python tricks
class Tricks:
# 1. Check duplications 
# Use Set()


    def all_unique(lst:List[int]):
        return len(lst)==len(set(lst))
    # If True, no duplications

# 2. Check the memory usage
    import sys
    var = 10
    print(sys.getsizeof(var))

# 3. Calculate Byte Size
    def byte_size(string):
        return (len(string.encode(utf-8)))

# 4. Print str N times
    n = 3
    s = "Python is the best language in the world"
    print(s*n)

# 5. Capitalize each word in a str
    s1 = "Python is the best language in the world"
    print(s.title())
    # Output will be "Python Is The Best Language In The World"

# 6. Chunk
    from math import ceil
    def chunk(lst, size):
        return list(
            map(lambda x: lst[x*size:x * size + size],
            list(range(0,ceil(len(lst)/size))))
        )
    chunk([1,2,3,4,5],2)
    # Output resembles: [[1,2],[3,4],5]

# 7. Using zip() to transpose an array
    array = [[ a ,  b ], [ c ,  d ], [ e ,  f ]]    
    transposed = zip(*array)    
    print(transposed) # [( a ,  c ,  e ), ( b ,  d ,  f )]

# 8. re   
    import re    
    def count_vowels(str):    
        return len(len(re.findall(r [aeiou] , str, re.IGNORECASE)))    
    count_vowels( foobar ) # 3    
    count_vowels( gym ) # 0

# 9. Lower the first character
    def decapitalize(string):    
        return str[:1].lower() + str[1:]    
    decapitalize( FooBar ) #  fooBar     
    decapitalize( FooBar ) #  fooBar