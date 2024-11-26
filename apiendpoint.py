'''
Create a command line tool in python, having these features:
○ Get the latest tag of given repository name.
○ Create new tag, by increase the latest tag by 1.
■ Example: latest tag: v2 -> new tag will be v3
○ Make a new release from a tag.
■ Use release name from user input.
■ If not, auto generate release name by format "release/dd-mm-yy"
'''
import requests

import os
#from dotenv import load_dotenv
#load_dotenv()
GITHUB_API_KEY = os.environ.get(
    'GITHUB_API_KEY')  # https://github.com/settings/tokens

#make requests
headers = {
    'Authorization': f'token {GITHUB_API_KEY}',
}
#repo_name = 'python/cpython'
repo_name = 'pyenv/pyenv'

url = f'https://api.github.com/repos/{repo_name}/tags'

res = requests.get(url, headers=headers)

print(f'{res.status_code=}')
print(res.json())
'''
{
        "name": "v20160726",
        "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20160726",
        "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20160726",
        "commit": 
        {
            "sha": "7da05ee9643dcd03562580a62a7fb802036cd200",
            "url": "https://api.github.com/repos/pyenv/pyenv/commits/7da05ee9643dcd03562580a62a7fb802036cd200"
        },
        "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTYwNzI2"
}
'''

d = res.json()
latest_tag_d = d[0]
print(f'''\n Latest tag\n {latest_tag_d['name']}''')
