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

import re
for tag in soup.find_all(re.compile("^p")):# tags with letter p
    print(tag.name)
    
