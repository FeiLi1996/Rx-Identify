
import requests 
from bs4 import BeautifulSoup



def image_identifier(pictureText):
    url = f'https://medcounselor.goldstandard.com/default.aspx?token=97a1a080cd7a272c6307&module=drugid&s=1&page=searchresults&s=1&side1={pictureText}&color=0&shape=0&pageNum=1'

    r= requests.get(url)



    soup = BeautifulSoup(r.text, 'html.parser')
    final_data=[];

    links2=soup.find_all('span',{'class':'results-item'})

  
    print('separate')

    try:
        print(links2[1].get_text()) # manufacturer
        print(links2[2].get_text()) # name
        print(links2[3].get_text()) # description and imprint number
        #refactor to get multiple information for each drug... currently only 1 drug
        
        # fei=[{1:'hi'},{2:'hi'},{3:'hi'},{4:'hi'},{5:'hi'}]

        # print( 'hi' in fei[0][1])
        # print(fei[0][1])
        #check if description already in the list.
        #add shape option??
    except LookupError:
        return 'No data were retrieved.'

    description_and_imprint = links2[3].get_text()
    split = description_and_imprint.split(', side 1')
    print(split)
    description = split[0]
    imprint='side 1'+ split[1]
   
        
    final_data.append(
        {
            'name':links2[2].get_text(),
            'manufacturer':links2[1].get_text(),
            'description':description,
            'imprint':imprint

        }
    )
    return final_data


