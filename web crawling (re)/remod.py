import re
print(dir(re))

string="broda mi name gusta yu"
r=re.search('mi',string)
print(r)
start=r.start()
end=r.end()
print(start)
print(end)
