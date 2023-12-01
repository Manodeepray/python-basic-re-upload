from bs4 import BeautifulSoup
html_doc="""<html>
<body>
<head><title>test html </title></head>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
<p>My third paragraph.</p>
<p>My third paragraph.</p>

</body>
</html>"""
soup= BeautifulSoup(html_doc,"html.parser")

head_tag=soup.head
print(head_tag)
print(head_tag.contents)

body_tag=soup.body

for i in body_tag.children:
    print(i)
    
for i in body_tag.descendants:
    print(i)
    
head_tag=soup.head

print(head_tag.title.string)
print(head_tag.title.parent)
print(head_tag.parent)
