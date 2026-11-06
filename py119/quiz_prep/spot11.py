"""
Inputs: string
Outputs: string

Explicit Rules:
- url will be passed to the function
- function must return the domain name

Implicit Rules:
- the domain name is the string after "http://" or "https://" after "www." and before ".com"

Data Structure/s:
- string

Algorithm:
- set cleaned_up to: replace 'http://' in url_string with ''
- set cleaned_up to:replace 'https://' in cleaned_up with ''
- set cleaned_up to:replace 'www.' in cleaned_up with ''
- find the index of the first '.' in cleaned_up
- set cleaned_up to the slice of cleaned_up from the beginning index to the
  index of the first period
- return cleaned_up
"""


def domain_name(url_string):
    cleaned_up = url_string.replace("http://", "")
    cleaned_up = cleaned_up.replace("https://", "")
    cleaned_up = cleaned_up.replace("www.", "")
    dot_idx = cleaned_up.index(".")
    cleaned_up = cleaned_up[:dot_idx]
    return cleaned_up


print(
    domain_name("http://github.com/carbonfive/raygun")
)  # should return "github"
print(domain_name("https://www.cnet.com"))  # should return "cnet"
