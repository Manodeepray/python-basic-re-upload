from bs4 import BeautifulSoup
soup= BeautifulSoup("<html> <p> asdasd <strong> hello <a> hello </html>","html.parser")
                    
print(soup.prettify())#fixes html code as well
"""
output:  
<html>
 <p>
  asdasd
  <strong>
   hello
   <a>
    hello
   </a>
  </strong>
 </p>
</html>
"""