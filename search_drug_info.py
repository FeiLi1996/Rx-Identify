
from typing import cast
import requests 
from bs4 import BeautifulSoup



# def image_identifier(_tictureText):
#     url = f'https://medcounselor.goldstandard.com/default.aspx?token=97a1a080cd7a272c6307&module=drugid&s=1&page=searchresults&s=1&side1={_tictureText}&color=0&shape=0&pageNum=1'

#     r= requests.get(url)



#     soup = BeautifulSoup(r.text, 'html.parser')
#     final_data=[];

#     links2=soup.find_all('span',{'class':'results-item'})

  
#     print('separate')

#     try:
#         print(links2[1].get_text()) # manufacturer
#         print(links2[2].get_text()) # name
#         print(links2[3].get_text()) # description and imprint number
#         #refactor to get multiple information for each drug... currently only 1 drug
        
#         # fei=[{1:'hi'},{2:'hi'},{3:'hi'},{4:'hi'},{5:'hi'}]

#         # print( 'hi' in fei[0][1])
#         # print(fei[0][1])
#         #check if description already in the list.
#         #add shape option??
#     except LookupError:
#         return 'No data were retrieved.'

#     description_and_imprint = links2[3].get_text()
#     split = description_and_imprint.split(', side 1')
#     print(split)
#     description = split[0]
#     imprint='side 1'+ split[1]
   
        
#     final_data.append(
#         {
#             'name':links2[2].get_text(),
#             'manufacturer':links2[1].get_text(),
#             'description':description,
#             'imprint':imprint

#         }
#     )
#     return final_data





def image_identifier(picture_text,shape_value):
    url = f'https://medcounselor.goldstandard.com/default.aspx?token=97a1a080cd7a272c6307&module=drugid&s=1&page=searchresults&s=1&side1={picture_text}&color=0&shape={shape_value}&pageNum=1'
    print(url,'urlllll')
    r= requests.get(url)



    soup = BeautifulSoup(r.text, 'html.parser')
    final_data=[];

    #drugs_result=soup.find_all('span',{'class':'results-item'})
  
    drugs_result2=soup.find('ul',{'class':'mchm-list'}).findAll('li',recursive=False)
    print(picture_text,shape_value)
    print(drugs_result2)
    print('separate')

    try:
        # print(links2[1].get_text()) # manufacturer
        # print(links2[2].get_text()) # name
        # print(links2[3].get_text()) # description and imprint number
        #refactor to get multiple information for each drug... currently only 1 drug
        
        # fei=[{1:'hi'},{2:'hi'},{3:'hi'},{4:'hi'},{5:'hi'}]

        # print( 'hi' in fei[0][1])
        # print(fei[0][1])
        #check if description already in the list.
        #add shape option??


        # for drug in drugs_result:
        #     print(drug,'hellllllo')
        #     print('helllo separator')
        
    
        
        # print(drugs_result2[0],'testting')
        # print('sepppp1')
        # print(drugs_result2[1])
        # print('sepppp2')
        # print(drugs_result2[2],'testting')
        # print('sepppp3')
        # print(drugs_result2[3])
        # print('sepppp4')
        # print(drugs_result2[4])
        #soup.select('div > p')[1].get_text(strip=True)
        drug_exist = False
        for drug in drugs_result2[:30]:
            try:
                description_and_imprint = drug.select('span')[-1].get_text()
            except:
                continue
            

            drug_name =drug.select('span')[0].get_text()
            for drug_in_collection in final_data:
                if(drug_name in drug_in_collection['name'] ):
                    drug_exist = True
                else:
                    continue

            if (not drug_exist):
                split = description_and_imprint.split(', side 1')
                print(split)
                description = split[0]
                imprint='side 1'+ split[1]
                print(final_data,'1')
                final_data.append(
                    {
                        'name':drug_name,
                        'manufacturer':drug.select('span')[3].get_text(),
                        'description':description,
                        'imprint':imprint

                    }
                )
            drug_exist = False
            print(final_data,'2')
    
    except LookupError:
        return 'No data were retrieved.'
    

        # print(drugs_result2[0].select('span')[0].get_text(),'testing1') # name w/ dosage

        # print(drugs_result2[0].select('span')[3].get_text(),'testing4') # manufactuere

        # print(drugs_result2[0].select('span')[5].get_text(),'testing6') #extra name w/o dosage
        # print(drugs_result2[0].select('span')[6].get_text(),'testing7') # description




        # print(drugs_result2[1].select('span')[0].get_text(),'testing1') # name w/ dosage

        # print(drugs_result2[1].select('span')[3].get_text(),'testing4') # manufactuere

        # print(drugs_result2[1].select('span')[5].get_text(),'testing6') #extra name w/o dosage
        # print(drugs_result2[1].select('span')[6].get_text(),'testing7') # description




    print(final_data,'helllo final')
    print('ehlllo???')
    # description_and_imprint = links2[3].get_text()
    # split = description_and_imprint.split(', side 1')
    # print(split)
    # description = split[0]
    # imprint='side 1'+ split[1]
   
        
    # final_data.append(
    #     {
    #         'name':links2[2].get_text(),
    #         'manufacturer':links2[1].get_text(),
    #         'description':description,
    #         'imprint':imprint

    #     }
    # )
    return final_data


