#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
import time
text = "This is is a string that contains a string."
 
def f1():
    print("Called f1")

def f2(f):
    f()

#------

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args,**kwargs)
        print("Ended")
        return val

    return wrapper

#Here the decorator means everytime we call f it will pass to the function f1
@f1
def f(a,b,c):
    print(a)
    print(b)
    print(c)
@f1
def add(x,y):
    return x + y

def timeFunction(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        val = f(*args, **kwargs)
        end = time.time()
        print(end - start)
        return val
    return wrapper

#-----
text = "This is is a string that contains a string."
def dup_words(text):
   words = text.split()
   uniqueList = []
   for w in words:
      if w not in uniqueList:
       uniqueList.append(w)
   return uniqueList
 
#print(dup_words(text))
#text = "aaabbbcccddeeffggaaaaaabbbbbbbbbbbbbbbbbbbbbaaaaaaaassssshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkhiiii"
text = "aabbccd"
@timeFunction
def solution1(text): 
    singles = []
    for a in text:
       if text.count(a) == 1:
          singles.append(a)

    for i, j in enumerate(singles):
       if i == 0:
          return j

print(solution1(text))
'''
#Steves
text = "aaabbbcccddeeffggaaaaaabbbbbbbbbbbbbbbbbbbbbaaaaaaaassssshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkq"
#text = "aabbccd"

def solution1(text): 
    singles = []
    for a in text:
       if text.count(a) == 1:
          singles.append(a)

    for i, j in enumerate(singles):
       if i == 0:
          return j

start = time.time()
print(solution1(text))
end = time.time()
print(end-start)

#Solution 2
def solution2(text):
    order = []
    counts = {}
    for w in text:
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1
            order.append(w)

    for w in order:
        if counts[w] == 1:
            return w
    return None

start = time.time()
print(solution2(text))
end = time.time()
print(end-start)

#Print First non repeating character
def firstNonRepeatingChar(s):
    string_length = len(s)
    left = 0
    right = 1
    seen = []
    if string_length <= 0:
        return None
    while (left < string_length) and (right < string_length):
        if s[left] == s[right]:
            right += 1
            seen.append(s[left])
        elif (s[left] != s[right]) and (s[left] in seen):
            left = right
            right += 1
        elif (s[left] != s[right]) and (s[left] not in seen):
            return s[left]
    
    if (s[string_length - 1] not in seen):
        return s[string_length - 1]

    return None

start = time.time()
print(firstNonRepeatingChar(text))
end = time.time()
print(end-start)





test1 = "aabbccb"

for a in test1:
    if test1.count(a) == 1:
        print(a)


def summer_69(arr):
    if not arr:
        return 0
    
    if 6 in arr:
        a = arr.index(6)
        b = arr.index(9)
        del arr[a:b +1]
    
    return sum(arr)
    

    y = []
    for x in arr:
      if 6 in arr:
        a = arr.index(6)
        b = arr.index(9)
        del arr[a:b + 1]
        y = arr
      else:
        return sum(arr) 


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([]))
'''
print("\n")
from signedjson.key import generate_signing_key, get_verify_key, encode_signing_key_base64
from signedjson.sign import (
    sign_json, verify_signed_json, SignatureVerifyException
)

signing_key = generate_signing_key('zxcvb')
base_64_signing_key = encode_signing_key_base64(signing_key)
print(base_64_signing_key)
signed_json = sign_json({'my_key': 'my_data'},'Drew', signing_key)
print(signed_json)
verify_key = get_verify_key(signing_key)
base_64_verify_key = encode_signing_key_base64(verify_key)
print(base_64_verify_key)
#check = get_verify_key(base_64_signing_key)

try:
    verify_signed_json(signed_json, 'Drew', verify_key)
    print('Signature is valid')
except SignatureVerifyException:
    print('Signature is invalid')