numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]


numbers.extend(even_numbers)
print(numbers)


#numbers.extend(even_numbers)
#print(numbers)  [1,2,3,4,5,[6,8,10]]


#insert(index, value)


numbers.insert(3,4.9)
print(numbers)


#remove() -> remove specific element


numbers.remove(1)
print(numbers)


#pop() -> deletes index value


numbers.pop(4)
print(numbers)


numbers.pop()
print(numbers)



numbers.clear()
print(numbers)


numbers2 = [2,12,4,1,36,32]
numbers2.sort()
print(numbers2)


numbers3 = [2,12,4,1,36,32]
numbers3.reverse()
print(numbers3)



programming_languages = ['Rust', 'Java', 'Python', 'C++']
newTest = programming_languages.index('Java') # 1
print(newTest)


numbers4 = ['gdd','iuhh','iooie','jdne','oieoje']
newTest = numbers4.index('iooie')
print(newTest)
