#ID
#Name
#Class Name
#Tag Name
#Link Text & Partial Link Text
#CSS Selector
#XPath


from selenium import webdriver

driver=webdriver.Chrome("PATH")

driver.maximize_window()
driver.delete_all_cookies()


driver.get("https://www.google.co.in")
print(driver.title)
# driver.find_element_by_id("lst-ib").send_keys("Hello World")            #by id
# search=driver.find_element_by_name('q')                                 #by name
# search.send_keys("Hello Google")
# search.submit()
#
# driver.find_element_by_link_text("Google Translate Sings: \"Hello\" by Adele - YouTube").click()    #by linktext
# driver.find_element_by_partial_link_text("Hello Google - ").click()                                  #by partiallinktext
# driver.find_element_by_xpath("//h3[@class='r H1u2de']//a").click()                                   #by xpath




#CSS Selectors
# Tag and ID            css=tag#id
# Tag and Class         css=tag.class
# Tag and Attribute     css=tag[attribute=value]

# Tag, Class, and Attribute         css=tag.class[attribute=value]
# Sub-String Matches
#   Starts With (^)
#   Ends With ($)
#   Contains (*)
# Child Elements
#   Direct Child
#   Sub-child
#   nth-child



# Tag and ID
# search=driver.find_element_by_css_selector("input#lst-ib")
# search.send_keys("Hello Google")
# search.submit()
#
# Tag and Class
# search=driver.find_element_by_css_selector("input.gsfi")
# search.send_keys("Hello Google")
# search.submit()

# Tag and Attribute
# search=driver.find_element_by_css_selector("input[name='q']")
# search.send_keys("Hello Google")
# search.submit()



# # Tag, Class, and Attribute
# search=driver.find_element_by_css_selector("input.gsfi[name='q']")
# search.send_keys("Hello Google")
# search.submit()


# Starts With (^)
# search=driver.find_element_by_css_selector("input[id^='lst']")
# search.send_keys("Hello Google")
# search.submit()

#Ends With ($)
# search=driver.find_element_by_css_selector("input[id$='ib']")
# search.send_keys("Hello Google")
# search.submit()

#Contains (*)
# search=driver.find_element_by_css_selector("input[id*='-ib']")
# search=driver.find_element_by_css_selector("input:contains('lst-ib')")         #alternate method
# search.send_keys("Hello Google")
# search.submit()

# Child Elements
#   Direct Child                                                    parentLocator>childLocator
# search=driver.find_element_by_css_selector("div#gs_lc0>input")
# search.send_keys("Hello Google")
# search.submit()


#   Sub-child               parentLocator>locator1 locator2
# search=driver.find_element_by_css_selector("div#sb_ifc0>div>input")
# search.send_keys("Hello Google")
# search.submit()

#   nth-child
search=driver.find_element_by_css_selector("div#gs_lc0 input:nth-of-type(1)")
search.send_keys("Hello Google")
search.submit()


