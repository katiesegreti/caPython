def is_even(x):
    if x %2 == 0:
        return True
    else:
        return False
        
        
print is_even(900)

def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False
        

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total
    

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
    
    
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
        
        
  
def reverse(text):
  length = len(text) - 1
  new_text = ""
  while length >= 0:
    new_text = new_text + text[l]
    l -= 1
  return new_text
  
  
def anti_vowel(text):
  no_vowel = ""
  for i in text:
    if i != "A" and i != "a" and i != "E" and i != "e" and i != "I" and i != "i" and i != "O" and i != "o" and i != "U" and i != "u":
      no_vowel = no_vowel + i
  return no_vowel
  
  
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total = 0
  for i in word:
    total += score[i]
  return total
  
  
def censor(text, word):
  sentence = text.split(" ")
  new_text = []
  asterisks = "*" * len(word)
  for w in sentence:
    if w == word:
      new_text.append(asterisks)
    else:
      new_text.append(w)
  return " ".join(new_text)
  
  
def count(sequence, item):
  total = 0
  for i in sequence:
    if i == item:
      total += 1
  return total
  

def purify(numbers):
  new_list = []
  for i in numbers:
    if i % 2 == 0:
      new_list.append(i)
  return new_list
  

def product(numbers):
  total = 1
  for i in numbers:
    total = total * i
  return total
  

def remove_duplicates(listy):
  new_listy = []
  for i in listy:
    if i not in new_listy:
      new_listy.append(i)
  return new_listy
  
  
def median(numbers):
  numbers.sort()
  length = len(numbers)
  if length % 2 == 1:
    return numbers[length / 2]
  else:
    return (numbers[(length + 1) / 2] + numbers[(length - 1) / 2]) / 2.0
    
