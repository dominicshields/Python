from test import testEqual
def reverse(s):
    y = ""
    w = len(s)
    for x in range(len(s)):
        y += s[w-1]
        w -= 1
    return y

testEqual(reverse("hello"),"olleh")
testEqual(reverse("l"),"l")
testEqual(reverse("follow"),"wollof")
testEqual(reverse(""),"")