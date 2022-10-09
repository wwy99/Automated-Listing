#User Input Needed
# no1. category 
# no2. item name
# no3. color
# no4. size
# no5. designer
# no6. condition
# no7. url

import gautofill as auto
import time



def autolist(maincat, subcat, Itemname, Designer, Size, Color, Condition, url):
    #open grailed first, then open xianyu, switch back to Grailed
    auto.openxianyu(url)
    #fill in category
    auto.category(maincat, subcat)

     #fill in designer
    auto.designer(Designer)

    #fill in item name
    auto.itemname(Itemname)

    

    #select size
    auto.size(maincat, Size)

    #fill in color
    auto.color(Color)

    #fill in condition 
    auto.condition(Condition)

    #fill in Description
    auto.description(Size)

    #fill in tags
    auto.addtags(maincat)

    #get price
    auto.price(maincat)
    auto.xianyuextend()


    #switch shipping
    #auto.shipping()

    #upload images
    auto.img(Itemname)



if __name__ == '__main__':
    '''
    #Category Guide
    #only support all tops/bottom/outerwear/hats and bags

    #Choose one from the following as maincat:
    main_cat = ['top', 'bot', 'out', 'acce']

    #choose one from the following as subcat(top are out are combined):
    tops_sub = ['longtee', 'polo', 'shirts', 'shorttee', 'sweater', 'sweat', 'tank', 'jersey']
    bot_sub = ['casual', 'cropped', 'denim', 'legging', 'jumpsuit', 'shorts', 'sweat', 'swim']
    out_sub = ['bomber', 'cape', 'denim', 'coat', 'leather', 'light', 'parka', 'rain', 'vest']
    acce_sub = ['bag', 'hat']


    #Size Guide
    #Choose one from the following:
    #sizes = ['xs','s','m','l','xl','xxl']

    #Condtion Guide
    #Condition, 0:new, 1:gently used////
    condition_list = ['New/Never Worn','Gently Used','Used','Very Worn']
    '''
    
    
    autolist(maincat = 'out', subcat = 'leather', Itemname = 'Visvim Elmendorf flighter jacket', Designer='Visvim', Size='s', Color='brown', Condition=1, url= 'https://m.tb.cn/h.fAuwAWg?tk=ehuN2HhZaHN')































































































































































































































































































































































    



   

    

