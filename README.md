onlyinfo
==========
.. image:: https://img.shields.io/pypi/v/discord.py.svg
   :target: https://pypi.org/project/onlyinfo/
   :alt: PyPI version info


A simple OnlyFiles link parser written in Python.

Key Features
-------------

- Very simple to use
- Pythonic

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

```sh

    # Linux/macOS
    python3 -m pip install -U onlyinfo

    # Windows
    py -3 -m pip install -U onlyinfo
```

Quick Example
--------------
```python
import onlyinfomain as only
    
my_scraper = only.Scraper()
download_link = my_scraper.extract(
"https://onlyfiles.io/f/75a4b182af9a4c939efeafc16bfbbfee"
)
song_title = my_scraper.title
print(download_link)
print(song_title)
```
------
