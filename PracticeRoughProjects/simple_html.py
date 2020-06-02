from bs4 import BeautifulSoup

SIMPLE_HTML='''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consecterur epidiscim elit. </p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Jenne</li>
    <li>Charlie</li>
    <li>Jose</li>
</ul>                
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = simple_soup.find('h1').string
    print (h1_tag)


def find_list_items():
    list_items=simple_soup.find_all('li')
    list_contents = [l.string for l in list_items]
    print(list_contents)


def find_subtitle():
    paragraph = simple_soup.find('p',{'class' : 'subtitle'})
    print(paragraph.string)


def find_other_paragraphs():
    paragraphs = simple_soup.find_all('p')
    other_paragraphs=[p for p in paragraphs if 'subtitle' not in p.attrs.get('class',[])]
    print(other_paragraphs[0].string)


find_title()
find_list_items()
find_subtitle()
find_other_paragraphs()