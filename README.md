# Description
A simple program for:  
* extracting the main content from a Wikipedia article, without the unnecessary links and references in text format. 
* speech generation from the extracted text.

# Requirements

* Ubuntu 16.04
* Python 2.6 and the following python modules:
	* beautifulsoup - for extracting data from html
 	* pyttsx - for speech generation
 	* urllib2 - for opening URLs
 	* sys	
 	
You can install them using pip.

# Execution
```shell
python text_extract.py 'article name'
python text2speech.py
```