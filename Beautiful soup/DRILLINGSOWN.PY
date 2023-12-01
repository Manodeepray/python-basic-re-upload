from bs4 import BeautifulSoup
soup= BeautifulSoup("""<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>
<p>My third paragraph.</p>
<p>My third paragraph.</p>

</body>
</html>""","html.parser")
print(soup.body)
print(soup.body())
print(soup.body.p)

print(soup.find_all('p'))
array=soup.find_all('p')
print(array[1])


