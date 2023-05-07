alpha_list = ['a' , 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

make_string = []
for x in alpha_list:
  for y in alpha_list:
    if x != y:
      make_string.append(x+y)

print(make_string)
print(len(make_string))

word = input()
a = make_string.index(word)
print(a+1)
