from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import urllib.request
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#User Input Needed
# no1. category 
# no2. item name
# no3. color
# no4. size
# no5. brand
# no6. condition
# no7. url

#only support all tops/bottom/outerwear/hats and bags
main_cat = ['top', 'bot', 'out', 'acce']
tops_sub = ['longtee', 'polo', 'shirts', 'shorttee', 'sweater', 'sweat', 'tank', 'jersey']
#tops_index = [1,2,3,4,5,6,7,8]
bot_sub = ['casual', 'cropped', 'denim', 'legging', 'jumpsuit', 'shorts', 'sweat', 'swim']
out_sub = ['bomber', 'cape', 'denim', 'coat', 'leather', 'light', 'parka', 'rain', 'vest']
acce_sub = ['bag', 'hat']



opp = Options()
opp.add_argument('--profile-directory=Profile 5')
opp.add_argument('user-data-dir=/Users/wwy/Library/Application Support/Google/Chrome')
#Open Grailed
driver = webdriver.Chrome(executable_path= "/Users/wwy/Downloads/chromedriver_2",chrome_options= opp)

driver.get('https://www.grailed.com/sell')

time.sleep(1)

def category(maincat, subcat):
    wait = WebDriverWait(driver, 10)

    #Category 
    menu = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/input')
    menu.click()
    #main category
    top = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/span[1]'
    bot = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/span[2]'
    out = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/span[3]'
    acce = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/span[6]'

    if maincat == 'top':
        #main
        maincat = top
        category = driver.find_element_by_xpath(maincat)
        category.click()
        #sub
        time.sleep(5)
        '''
        subindex = tops_sub.index(subcat)+1
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div/span[{}]'.format(subindex)))).click()
'''
    if maincat == 'bot':
        #main
        maincat = bot
        category = driver.find_element_by_xpath(maincat)
        category.click()
        #sub
        '''
        submenu = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/input')
        submenu.click()
        subindex = bot_sub.index(subcat)+1
        subpath = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div/span[{}]'.format(subindex)
        subcategory = driver.find_element_by_xpath(subpath)
        subcategory.click()
    
    '''
    if maincat == 'out':
        #main
        maincat = out
        category = driver.find_element_by_xpath(maincat)
        category.click()
        #sub
        '''
        submenu = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/input')
        submenu.click()
        subindex = out_sub.index(subcat)+1
        subpath = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div/span[{}]'.format(subindex)
        subcategory = driver.find_element_by_xpath(subpath)
        subcategory.click()
    '''
    if maincat == 'acce':
        #main
        maincat = acce
        category = driver.find_element_by_xpath(maincat)
        category.click()
        #sub
        '''
        submenu = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/input')
        submenu.click()
        bag = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div/span[1]'
        hat = '//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div/span[5]'
               
        if subcat == 'bag':
            subpath = bag
            subcategory = driver.find_element_by_xpath(subpath)
            subcategory.click()
        elif subcat == 'hat':
            subpath = hat
            subcategory = driver.find_element_by_xpath(subpath)
            subcategory.click()
            '''
    else:
        print('invalid input')
        return

def designer(Designer):
    
    #Designer
    designer = Designer
    design = driver.find_element_by_xpath('//*[@id="designer-autocomplete"]')
    design.send_keys(designer)
    time.sleep(2)


def itemname(Itemname):
    #Itemname
    itemname = Itemname
    item = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[2]/input')
    item.send_keys(itemname)

def size(maincat, Size):
    #Size
    sizes = ['xs','s','m','l','xl','xxl']
    size_names = ['US XS / EU 42 / 0', 'US S / EU 44-46 / 1','US M / EU 48-50 / 2','US L / EU 52-54 / 3','US XL / EU 56 / 4','US XXL / EU 58 / 5']
    bot_size_name = 'US 34 / EU 50'
    acce_size_name = 'ONE SIZE'
    
    if maincat == 'top' or maincat == 'out':
        size_index = sizes.index(Size)
        size_text = size_names[size_index]
        element = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[2]/select')
        drp = Select(element)
        drp.select_by_visible_text(size_text) 

        drp.select_by_visible_text(size_text) 
    if maincat == 'bot':
        element = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[2]/select')
        drp = Select(element)
        drp.select_by_visible_text(bot_size_name) 

    if maincat == 'acce':
        element = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[1]/div/div[2]/select')
        drp = Select(element)
        drp.select_by_visible_text(acce_size_name) 
    
    else:
        print('invalid input')
        return
    

def color(Color):
    itemcolor = Color
    color= driver.find_element_by_xpath('//*[@id="color-autocomplete"]')
    color.send_keys(itemcolor)

def condition(Condition):
    #Condition, 0:new, 1:gently used////
    condition_list = ['New/Never Worn','Gently Used','Used','Very Worn']
    condition = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[4]/select')
    drp2 = Select(condition)
    condition_text = condition_list[Condition]
    drp2.select_by_visible_text(condition_text)

def description(Size):
    itemdescription = """
Size: {}. can provide measurements upon request.

Condition: kept in decent condition as shown. All details have shown in the pics, further pic request through DM.

Shipping: All Items are shipped internationally via Fedex/EMS express. Shipment will proceed within three business days. Please allow around ten business days for order delivery. 

Authentication: All items are handpicked and prior authenticated by our specialist to ensure 100% authenticity around the store. Shop with confidence. 

Order Cancel & Return: Due to the specialty of items, all sales are final, we apologize for not accepting cancellations or returns.

""".format(Size)


    description = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[5]/textarea')
    description.send_keys(itemdescription)


def addtags(maincat):
    
    if maincat == 'acce':
        tag = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[6]/div[2]/ul/li/input')

    else:
        tag = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[7]/div[2]/ul/li/input')
    
    tags = []
    tag1 = 'Visvim'
    tags.append(tag1)
    tag2 = 'JapaneseBrand'
    tags.append(tag2)
    tag3 = 'isseymiyake'
    tags.append(tag3)
    tag4 = 'Vintage'
    tags.append(tag4)
    tag5 = 'numbernine'
    tags.append(tag5)
    tag6 = 'wtaps'
    tags.append(tag6)
    tag7 = 'undercover'
    tags.append(tag7)
    tag8 = 'kapital'
    tags.append(tag8)
    tag9 = 'commedesgarcons'
    tags.append(tag9)
    tag10 = 'yohji'
    tags.append(tag10)
    for i in range(len(tags)):
        tag.send_keys(tags[i])
        tag.send_keys(Keys.ENTER)

def openxianyu(url):
    driver.execute_script("window.open('about:blank','secondtab');")
    driver.switch_to.window('secondtab')
    driver.get(url)
    driver.switch_to.window(driver.window_handles[0])




def xianyuextend():
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    button = driver.find_element_by_css_selector('#root > div > div.rax-view-v2.Detail--container--17hcFL4 > div > div.rax-view-v2.normal--descCollpaseContainer--228MYrV > div.rax-view-v2.toggleMod--clickMore--3bu1S-r')
    driver.execute_script("arguments[0].click();", button)
    print('extended')
    
    
    
def price(maincat):
    #retial price from xiayun
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    find = driver.find_element_by_css_selector('#root > div > div.rax-view-v2.Detail--container--17hcFL4 > div > div.rax-view-v2.normal--descCollpaseContainer--228MYrV > div.rax-view-v2.priceMod--priceMod--Yld0tWj > div > div.rax-view-v2.priceMod--priceTextWrap--3PwMboh > span.rax-text-v2.priceMod--soldPrice--20BWwRm')
    retail = int(find.text)
    
    print(retail)
    if retail <=800:
        itemprice = 380


    if retail > 800 and retail <= 1600:
        itemprice = math.ceil((retail/6.5/0.86)*2.5) 

    #fill in sale price in grailed
    if retail >1600 and retail <= 3000:
        itemprice = math.ceil((retail/6.5/0.86)*1.85) + 65
    
    if retail >3000:
        itemprice = math.ceil((retail/6.5/0.86)*1.65)

    if retail >8000:
        itemprice = math.ceil((retail/6.5/0.86)*1.55)

    if retail >12000:
        itemprice = math.ceil((retail/6.5/0.86)*1.4)
            

    
    driver.switch_to.window(driver.window_handles[0])
    if maincat == 'acce':
        price = price = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[7]/div[2]/div[1]/div[1]/label/input')
    else:
        price = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[8]/div[2]/div[1]/div[1]/label/input')
    price.send_keys(itemprice)

    #accept offer - turn on

    #smart pricing -
    # Python program to demonstrate the use of floor() method
      
    
    floorprice = math.floor(itemprice*0.9)
    if maincat == 'acce':
        smart = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[7]/div[2]/div[1]/div[2]/div/label/input')
    else:
        smart = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[8]/div[2]/div[1]/div[2]/div/label/input')
    smart.send_keys(floorprice)

    time.sleep(2)
    
def shipping():
    #change to china add
    time.sleep(1)
    myown = driver.find_element_by_xpath('//*[@id="SellForm"]/div/div[2]/form/div[8]/div[3]/div[1]/button[2]')
    myown.click()
    time.sleep(0.5)
    usa = driver.find_element_by_xpath('//*[@id="MyOwnShippingWrappermyOwnShipping"]')
    usa.click()


def img(itemname):
    #get the images from xianyu and uplaod to grailed
    #switch to xianyu
    time.sleep(6)
    
    imgdiv = driver.find_element_by_css_selector('#root > div > div.rax-view-v2.Detail--container--17hcFL4 > div > div.rax-view-v2.normal--detailContainer--1YGYI4g > div.rax-view-v2.imageListMod--imageWrap--3cJ0bMK')
    
    
    allimg = imgdiv.find_elements_by_xpath('.//*')
    num = len(allimg)
    print('total of {} images found'.format(num))
    
    #drop exceed images
    if num>9:
        allimg = allimg[0:9]
        num = len(allimg)
        print('extra imgs removed')


    #save images
    for i in range(num):
        src = allimg[i].get_attribute('src')
        print(src)
        filename = '/Users/wwy/desktop/gproject/gitem/#{}.png'.format(i)
        urllib.request.urlretrieve(src,filename)
        print('images saved')
        

    #switch to grailed
    driver.switch_to.window(driver.window_handles[0])

    #you can upload at most 8 imgs
    
    cover = driver.find_element_by_xpath('//*[@id="photo_input_0"]')
    cover.send_keys('/Users/wwy/desktop/gproject/gitem/#{}.png'.format(0))
    
    for i in range(1,num):
        imgholder = driver.find_element_by_xpath('//*[@id="photo_input_{}"]'.format(i))
        imgholder.send_keys('/Users/wwy/desktop/gproject/gitem/#{}.png'.format(i))
        print('#{} image loaded'.format(i))
    






    





