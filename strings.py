s1 = "abc"
s2 = "def"
print("%s | %s" % (s1, s2))
print("%(str1)s | %(str2)s" % {'str1': s1, 'str2': s2})

a = 123.123123123123
print("%s" % a)
print("%.3f" % a)
print("%20.3f" % a)
print("%020.3f" % a)
print("{}".format(123))
print("{n1} {n2} {n3}".format(n1=1, n2=2, n3=3))

print(f'{s1 * 2} {s2}')

# methods
a = "Hello"
print(a.center(20))
