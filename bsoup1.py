from bs4 import BeautifulSoup
#from pyparsing import Literal, Word, Optional
import urllib2
import urlparse
li=[]
name=[]
site=[]
region=[]
sites=[]
alternative=[]
dob=[]
dod=[]
achievement=[]
gender=[]
places=[]
count=0
results=''
crawling='http://en.wikipedia.org/wiki/List_of_Indian_independence_activists'
url2=urlparse.urlparse(crawling)
print url2.geturl()
req=urllib2.Request(crawling,headers={'User-Agent' : "Magic Browser"})
print req
list_names=[]
response=urllib2.urlopen(req)
msg=response.read()
soup=BeautifulSoup(msg)
tr=soup.find_all('tr')
tr=str(tr).split(',')
for tr1 in tr:
        soup=BeautifulSoup(tr1)
        td=soup.find_all('td')
        td_len=len(soup.find_all('td'))
        if td_len==3:
            td=str(td).split(',')
            for td2 in td:
                soup=BeautifulSoup(td2)
                div=len(soup.find_all('div'))
                if div==0:
                    list_names.append(td2)
        else:
            continue
soup=BeautifulSoup(str(list_names))
count_n=0
count_r=0
for td in soup.findAll('td'):
        str1=td.get_text()
        count=count+1
        if count%3==1:
                a=td.find('a')
                site='http://en.wikipedia.org'+a["href"]
                sites.append(site)
                if str1=='':
                        name.append('None')
                else:
                        name.append(str1)
        elif count%3==2:
                if str1=='':
                        region.append('None')
                else:
                        region.append(str1)
        else:
                continue
count_reg=0
count_name=0
credits=''
for reg in region:
        if reg=='None':
                del name[count_reg]
                del region[count_reg]
                del sites[count_reg]
                count_reg=count_reg+1
        else:
                count_reg=count_reg+1
                continue

for nam in name:
        if nam=='Bhairav Murmu':
                del name[count_name]
                del region[count_name]
                del sites[count_name]
                count_name=count_name+1
        else:
                count_name=count_name+1
                continue
count_name=0
for nam in name:
        if nam=='Chand Murmu':
                del name[count_name]
                del region[count_name]
                del sites[count_name]
                count_name=count_name+1
        else:
                count_name=count_name+1
                continue
count=0
for site in sites:
        print site
        url2=urlparse.urlparse(site)
        req=urllib2.Request(site,headers={'User-Agent' : "Magic Browser"})
        #print req
        response=urllib2.urlopen(req)
        #print response
        msg=response.read()
        soup=BeautifulSoup(msg)
        pelement=soup.find_all('p')
        #text = "Allowed Hello Hollow"
        '''for i in range(0,len(pelement)):
                #print [n for n in xrange(len(pelement[i])) if str(pelement[i]).find('at', n) == n]
                v=str(pelement[i]).find('at')
                print str(pelement[i])[v+1]'''
                
        
        male=0
        female=0
        #print len(pelement)
        for i in range(0,len(pelement)):
                #print 'hi'
                male=male+str(pelement[i]).count('He')
                female=female+str(pelement[i]).count('she')
                female=female+str(pelement[i]).count('Her')
        print 'male',male
        print 'female',female
        if female>male:
                gender.append('Female')
        else:
                gender.append('Male')
                #print b
                #val2=(pelement[i].finad_all('She'))
                #print val
                #print val2
        #print pelement
        #tdelement = soup.find('td', id='persondata-label')
        tdelement = soup.findAll("td", { "class" : "persondata-label" })
        if tdelement!=[]:
        #print len(tdelement)
                for i in range (0,7):
                        if i==1:
                                trelement=str(tdelement[i].parent)
                                soup=BeautifulSoup(trelement)
                                td=soup.find_all('td')
                                #print td
                                val=td[1].get_text()
                                if val!='':
                                        v=repr(val)
                                        print v[2]
                                        if v[2]=='\\':
                                                print 'no'
                                                alternative.append('None')
                                        else:
                                                alternative.append(val)
                                else: 
                                        alternative.append('None')
                        elif i==2:
                                trelement=str(tdelement[i].parent)
                                soup=BeautifulSoup(trelement)
                                td=soup.find_all('td')
                                #print td
                                val=td[1].get_text()
                                if val!='':
                                        achievement.append(val)
                                else:
                                        achievement.append('None')
                        elif i==3:
                                trelement=str(tdelement[i].parent)
                                soup=BeautifulSoup(trelement)
                                td=soup.find_all('td')
                                #print td
                                val=td[1].get_text()
                                if val!='':
                                        dob.append(val)
                                else:
                                        dob.append('None')
                        elif i==5:
                                trelement=str(tdelement[i].parent)
                                soup=BeautifulSoup(trelement)
                                td=soup.find_all('td')
                                #print td
                                val=td[1].get_text()
                                if val!='':
                                        dod.append(val)
                                else:
                                        dod.append('None')
                        elif i==4:
                                trelement=str(tdelement[i].parent)
                                soup=BeautifulSoup(trelement)
                                td=soup.find_all('td')
                                #print td
                                val=td[1].get_text()
                                if val!='':
                                        #print val
                                        
                                        li=val.split(',')
                                        for i in range(0,len(li)):
                                                v=li[i]
                                                if v[0]==' ':
                                                        l=len(li[i])
                                                        v=v[1:l]
                                                places.append(v)
                        elif i==6:
                                trelement=str(tdelement[i].parent)
                                soup=BeautifulSoup(trelement)
                                td=soup.find_all('td')
                                #print td
                                val=td[1].get_text()
                                if val!='':
                                        #print val
                                        
                                        li=val.split(',')
                                        for i in range(0,len(li)):
                                                v=li[i]
                                                if v[0]==' ':
                                                        l=len(li[i])
                                                        v=v[1:l]
                                                places.append(v)
                                else:
                                        print 'None'
        else:
                achievement.append('None')
                dob.append('None')
                dod.append('None')
                alternative.append('None')
        #print soup.title'''
'''print name
print region
print sites
print len(name)
print len(region)
print len(sites)


for li in alternative:
        print type(li[0])
        print li[0].Unidecode'''
print name
print achievement
print dob
print dod
print alternative
print region
print gender
print len(name)
print len(achievement)
print len(dob)
print len(dod)
print len(alternative)
print len(region)
print len(gender)
fp=open("b.txt","w")
count=0
a=0
for birth in dob:
        if birth=='None':
                count=count+1
                continue
        else:
                fp.write(name[count]+';'+gender[count]+';'+dob[count]+';'+dod[count]+';'+region[count]+';'+achievement[count]+';'+alternative[count]+'\n')
                count=count+1
fp.close()

fp=open("name.txt","w")
count=0
a=0
for birth in dob:
        if birth=='None':
                count=count+1
                continue
        else:
                st=''
                li=name[count].split()
                for i in range(0,len(li)):
                        st=st+str(li[i])
                fp.write(st.lower()+'\n')
                count=count+1
fp.close()

fp=open("place.txt","w")
count=0
a=0
for place in places:
        fp.write(place.lower()+'\n')
fp.close()
