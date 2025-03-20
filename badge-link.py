import os  

directory = '.github/workflows'  
base_url = 'https://github.com/charan-happy/GithubActions-Certification-Journey/actions/workflows/'  

for filename in os.listdir(directory):  
    if filename.endswith('.yml'):  
        print(f"[![{filename} Status]({base_url}{filename}/badge.svg?branch=main)]({base_url}{filename})\n")  