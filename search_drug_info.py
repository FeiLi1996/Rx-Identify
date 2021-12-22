
import requests 
from bs4 import BeautifulSoup


def image_identifier(picture_text,shape_value):
    url = f'https://medcounselor.goldstandard.com/default.aspx?token=97a1a080cd7a272c6307&module=drugid&s=1&page=searchresults&s=1&side1={picture_text}&color=0&shape={shape_value}&pageNum=1'
    r= requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    final_data=[]
    drugs_result=soup.find('ul',{'class':'mchm-list'}).findAll('li',recursive=False)
    drug_exist = False
    try:
        for drug in drugs_result[:30]:
            try:
                description_and_imprint = drug.select('span')[-1].get_text()
            except IndexError:
                #need this continue because everyother list is used as a divider instead of holding drug information. Will throw index out of boound error
                continue
            drug_name =drug.select('span')[0].get_text()
            for drug_in_collection in final_data:
                if(drug_name in drug_in_collection['name'] ):
                    drug_exist = True
                    break
                else:
                    continue

            if (not drug_exist):
                split = description_and_imprint.split(', side 1')
                description = split[0]
                imprint='side 1'+ split[1]

                final_data.append(
                    {
                        'name':drug_name,
                        'manufacturer':drug.select('span')[3].get_text(),
                        'description':description,
                        'imprint':imprint

                    }
                )
            drug_exist = False
    except LookupError:
        return 'No data were retrieved.'
    return final_data


