from selenium import webdriver
from selenium.common import exceptions
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def get_website(url):
    driver.get(url)

def search(search_keyword):

    search_script = f'''
        document.getElementById("gh-ac").value = "{search_keyword}"
        document.getElementById("gh-btn").click()
    '''
    driver.execute_script(search_script)

def filter():
    
    filter_script = f'''
        document.querySelector("[aria-label='Completed Items']").click();
    '''
    try:
        driver.execute_script(filter_script)
    except exceptions.JavascriptException as e:
        print(e)

def next():
    next_script = f'''
        document.querySelector("[aria-label='Go to next search page']").click();
    '''
    driver.execute_script(next_script)

def next_pages(num_pages):
    for i in range(num_pages):
        try:
            next()

        except exceptions.JavascriptException as e:
            print(e)
            break

if __name__ == "__main__":

    get_website('https://www.ebay.com/')
    search("cannon e 50")
    filter()
    html = driver.page_source
    f = open("demofile2.txt", "a")
    f.write(html)
    f.close()



