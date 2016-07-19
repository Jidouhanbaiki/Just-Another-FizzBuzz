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
