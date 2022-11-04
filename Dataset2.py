#1Problem 
a = 0
def b():
    global a
    a = c(a)
    
def c(a):
    return a + 2

b()
b()
b()
a
"""
addition of 2
 a = 0+2 = 2
 a = 2+2 = 4
 a = 4+2 = 6
a = 6 
"""
#2Problem.

def filelength(filename):
    try:
        file_open = open(filename)
        data = file_open.read()
        file_open.close()
        print(len(data))
    except:
        print("File " +filename + " not found.")
filelength('idterm.py')    



#Problem 3:
class Marsupial:
    def __init__(self):
         self.pouch = []
    def put_in_pouch(self,name):
          self.pouch.append(name)
    def pouch_contents(self):
          print(self.pouch)

c1 = Marsupial()
c1.put_in_pouch('doll')
c1.put_in_pouch('firetruck')
c1.put_in_pouch('kitten')
c1.pouch_contents()

class Kangaroo(Marsupial):
  def __init__(self,x,y):
    super().__init__()
    self.x = x
    self.y = y
  
  def jump(self,dx,dy):
    self.x += dx
    self.y += dy
  
  def __str__(self):
    return f"I am kangaroo located at coordinates ({self.x},{self.y})"

k = Kangaroo(0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents()
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)




#4Problem.
def collatz(n):
 
    while n!=1:
        
        print(n)

        if n%2 is 0:
            #n is even
            n=n//2
        else:
            #n is odd
            n=3*n+1
    
    print(1)
n=int(input("Could You Please enter the number"))
collatz(n)

# 5 Problem 
#Decimal_binary_conversion
def getbinary(number):
   
    if number == 0:
        return 0
       
    number_1 = getbinary(number//2)
     
    return number % 2 + 10 * number_1
   
decimal = 14
print(getbinary(decimal))

#6Problem
from html.parser import HTMLParser

#Inheriting
class HeadingParser(HTMLParser):
    #headings
    headings = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    
    def tag1(self, tag, attrs):
        if tag in self.headers:
            print(tag)

    def tag2(self, tag):
        if tag in self.headers:
            print(tag)

    def data(self, data):
        print(data)

parser = HeadingParser()
infile = open("C:/Users/Owner/Desktop/w3c.html")
content = infile.read()
infile.close()
hp = HeadingParser()
hp.feed(content)

# 7 Problem
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
def webdir(url,depth,indent):
  if depth ==0:
    return 
  print(" "*indent+ f"{url}")
  req1 = Request(url)
  page = urlopen(req1)
  b_soup = BeautifulSoup(page, "lxml")
  urls = []
  for link in b_soup.findAll('a'):
    
    if link.get('href') and 'https' ==  link.get('href')[:5]:
      urls.append(link.get('href'))
  for link in urls:
    webdir(link,depth-1,indent+1)

#webdir('https://www.webscraper.io/test-sites/e-commerce/static', 3, 0)
    


# 8Problem
#sqlqueries
"""
CREATE TABLE weather
(
city varchar(15),
country varchar(15),
season varchar(15),
temperature float,
rainfall float
);

# Insering Values
INSERT INTO weather VALUES('Mumbai', 'India', 'Winter', 24.8,5.9),
('Mumbai', 'India', 'Spring', 28.4,16.2),
('Mumbai', 'India', 'Summer', 27.9,1549.4),
('Mumbai', 'India', 'Fall', 27.6,346.0),
('London', 'United kingdom', 'Winter', 4.2,207.7),
('London', 'United kingdom', 'Spring', 8.3,169.6),
('London', 'United kingdom','Summer', 15.7,157.0),
('London', 'United kingdom','Fall', 10.4,218.5),
('Cairo', 'Egypt','Winter', 13.6,16.5),
('Cairo', 'Egypt', 'Spring', 20.7,6.5);

#Query1
select * from weather
#Query2
select distinct(city) from weather
#Query3
select * from weather
where country = 'India'
#Query4
select * from weather 
where Season = 'Fall'
#query5
select city,country,season from weather
where rainfall between 200 and 400
#Query6
select city,country,season from weather
where season = 'Fall' and temprature > 20
order by Temprature 
#Query7
select sum(Rainfall) from weather
where city = 'Cairo'
#Query8
select season,sum(rainfall)
from weather
group by season 
"""


#9Problem. 
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# Printing in upper case
print([n.upper() for n in words])

# Printing in lower case
print([n.lower() for n in words])

# Printing length
print([len(n) for n in words])

#uppercase and lowercase
print([[n.upper(), n.lower(), len(n)] for n in words])

# Printing words having 4 or more characters
print([n for n in words if len(n)>=4])


print("****************************************")
print("\n end")




