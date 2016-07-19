# simple mapping

arr = [i for i in range(1, 101)]
rules = ((15, "FizzBuzz"), (3, "Fizz"), (5, "Buzz"))


def fizzbuzz(arr, div, word):
	def remainder(a, b):
		return True if type(a)==type("") else a % b
	return map(lambda x: x if remainder(x, div) else word, arr)

for rule in rules:
	arr = fizzbuzz(arr, *rule)

print arr


# take 1.a

arr = [i for i in range(1, 101)]
rules = ((15, "FizzBuzz"), (3, "Fizz"), (5, "Buzz"))


def fizzbuzz(arr, div, word):
	return map(lambda x: x if div.__rmod__(x) else word, arr)

for rule in rules:
	arr = fizzbuzz(arr, *rule)

print arr



# take 2

arr = [i for i in range(1, 101)]
rules = ((3, "Fizz"), (5, "Buzz"))

arr = map(lambda x: [x, ""], arr)

for r_num, r_str in rules:
	arr = map(
		lambda (x_num, x_str): [x_num, x_str + r_str] if not x_num % r_num else [x_num, x_str], 
		arr
	)

arr = [x_str if x_str else x_num for x_num, x_str in arr]
print arr


# take 3 - that's perfect

rules = ((3, "Fizz"), (5, "Buzz"))

arr = []
for i in range(1,101):
	arr.append("")
	for r_num, r_str in rules:
		arr[-1] += "" if i % r_num else r_str
	arr[-1] = arr[-1] or i

print arr



# take 4 - generator

rules = ((3, "Fizz"), (5, "Buzz"))

def fbrange(n, rules):
	def fb(arr):
		fb_str = "".join([elem for elem in arr if type(elem) == type("")])
		return fb_str or arr[0]
	i = 1
	while i < n:
		yield fb([i if i % r_num else r_str for r_num, r_str in rules])
		i += 1

print list(fbrange(101, rules))


# take 5 

def fbrange(n):
	i = [1, 1, 1]
	while i[0] < n:
		delta = "" if i[1] else "Fizz"
		delta += "" if i[2] else "Buzz"
		yield delta or i[0]
		i = map(lambda x: x+1, i)
		i[1] = 0 if i[1] == 3 else i[1]
		i[2] = 0 if i[2] == 5 else i[2]

print list(fbrange(101))

# take 5.a

rules = ((3, "Fizz"), (5, "Buzz"))

def fbrange(n, rules):
	i = [1, 1, 1]
	while i[0] < n:
		delta = ""
		for j in range(len(rules)):	
			i[j+1] = 0 if i[j+1] == rules[j][0] else i[j+1]
			delta += "" if i[j+1] else rules[j][1]
			
		yield delta or i[0]
		i = map(lambda x: x+1, i)

print list(fbrange(101, rules))

# take 6 inspired by https://gist.github.com/jshurst/b6591c0140e8aad8e55e

rules = ((lambda x: x % 3, 0 ,"Kamen"), (lambda x: x % 5, 0 ,"Rider"))

arr = []
for i in range(1,101):
    next_var = ""
    for action, condition, result in rules:	
        next_var += result if action(i) == condition else ""
    next_var = next_var or i
    arr.append(next_var)

print arr


# take 6.a

rules = ((lambda x: x % 3, 0 ,"Fizz"), (lambda x: x % 5, 0 ,"Buzz"))

def execute(user_input, action, condition, output):
	return output if action(user_input) == condition else ""

arr = []
for i in range(1,101):
    next_var = ""
    for rule in rules:	
        next_var += execute(i, *rule)
    next_var = next_var or i
    arr.append(next_var)

print arr


# take 7 functional fizzbuzz without "if"

arr = []
for i in range(1,101):
	rules = {
		(False, False): i, 
		(True, False): "Fizz",
		(False, True): "Buzz",
		(True, True): "FizzBuzz",
	}
	arr.append(rules[(not i % 3, not i % 5)]) 

print arr
