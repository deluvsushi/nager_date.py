# nager_date.py
Web-API for [date.nager.at](https://date.nager.at) popular project to query holidays that currently support's over 100 countries

## Example
```python
import nager_date
nager_date = nager_date.NagerDate()
country_info = nager_date.get_country_info(country_code="")
print(country_info)
```
