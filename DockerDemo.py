import requests
# from requests.auth import HTTPBasicAuth
import json
# import html_to_json
# from json2html import *
from atlassian import Confluence


'''
old code that uses HTTPBasicAuth,json2html
# url = "https://confluence.asux.aptiv.com/pages/resumedraft.action?draftId=284312698&draftShareId=4552504a-6f77-48bd-a830-9ebc56b6cac5&"#"https://confluence.asux.aptiv.com/display/1CCGF/2022/07/24/This+is+a+Test+Blog+Post+for+Docker-Compiler+Warnings" #"https://confluence.asux.aptiv.com/pages/viewrecentblogposts.action?key=1CCGF"

# #blog_page_res = requests.get(url,data=values,headers={"Accept":"text/plain"})
# #print(f"your request to {url} came back with status code {blog_page_res.status_code}")
# #print(blog_page_res.text)

# blog_page_res = requests.get(url,auth=HTTPBasicAuth("mjqy67","DurgaDevi2137"))
# print(f"your request to {url} came back with status code {blog_page_res.status_code}")
# blog_page_txt = blog_page_res.text
# json_data_in_dict=html_to_json.convert(blog_page_txt)
# #print(json_data_in_dict)
# blog_post_title = json_data_in_dict["html"][0]["head"][0]["title"][0]["_value"]
# blog_post_title=blog_post_title.replace("Warnings","Error")
# #print(blog_post_title)
# json_data_in_dict["html"][0]["head"][0]["title"][0]["_value"] = blog_post_title
# #print(json_data_in_dict["html"][0]["head"][0]["title"][0]["_value"])
# json_data = json.dumps(json_data_in_dict)
# html_data = json2html.convert(json=json_data)
# json_data_str = str(json_data)
# #print(html_data)
# headers = {'Content-Type': 'text/html; charset=utf-8'}
# blog_post = requests.post(url=url,auth=HTTPBasicAuth("mjqy67","DurgaDevi2137"),data =json_data_str,headers=headers)
# print(blog_post.status_code)
#print(blog_page_res.headers)


#url = "https://confluence.asux.aptiv.com/rest/api/content/284313060?expand=body.storage"
#res = requests.get(url,auth=HTTPBasicAuth("mjqy67","DurgaDevi2137"))
#res_text = res.text
#res_json = json.loads(res_text)
#res_html = json2html.convert(res_json)
'''


updatetoconfluence = True
openwebbrowser = True 

confluence_user_token = "ODkzNzcyNjU0MzMyOk6zvh2xxkB70/0nVtUShx+Nbk4y"
userID="mjqy67"
confluence_link = "https://confluence.asux.aptiv.com/pages/viewpage.action?pageId=284313060"
confluence_title = 'Software Test Page'
confluence_page_id = 284313060
confluence_xhtml = "<table><tr><td>Hello World! we are testing!via docker and cloudbees now</td></tr></table>"
def shoot_it_to_confluence(_token, _confluence_page_id, _confluence_page_title, _confluence_xhtml_content):
        confluence = Confluence(
             url='https://confluence.asux.aptiv.com/',
             token = _token)
        for x in range(0, 4):  # try 4 times
            try:
                print('try: '+str(x))
                status = confluence.update_page(
                parent_id=None,
                page_id=_confluence_page_id,
                title=_confluence_page_title,
                body=_confluence_xhtml_content)
                exception_occured = False
            except Exception as str_error:
                print(str_error)
                #logging.warning(str_error)
                exception_occured = True
                pass
            if exception_occured:
                print('Exception occoured while writing to confluence. Trying again in 4 seconds...')
                #logging.warning('Exception occoured while writing to confluence. Trying again in 4 seconds...')
                time.sleep(4)  # wait for 4 seconds before trying to fetch the data again
            else:
                break


shoot_it_to_confluence(confluence_user_token,confluence_page_id,confluence_title,confluence_xhtml)





