print(not(5<6 and 4<7))
print(6<7 or 7>8 and not(5>7 and 7<8))
print(6>4 and 8>5)

#2
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
new_lorem=lorem.split(" ")
print(len(new_lorem))

#3
text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2="""Loremipsumdolorsitamet, consecteturadipiscingelit, 
seddoeiusmodtemporincididuntutlaboreetdoloremagnaaliqua."""
print(text.replace(" ",""))
print(text2.replace(" ",""))
#4
a="кыргызская республика"
print(a.title())
#5
t='t e s t'
print(t.replace(" ",""))