
## Introduction

atnd.py is a wrapper class that allows you to access [ATND API](http://atnd.org/doc/api.html) easily.


## Usage

Query parameters must be set to ``Atnd`` class as arguments when you make an instance of the class. If you want to search a event regarding "ruby", you have to write argument like this: ``obj = Atnd(keyword="ruby")``  

```python   
from atnd import Atnd  
obj = Atnd(keyword_or="ruby,python", ym="201303")  
obj.get_json_data()
obj.show_results()  
```
