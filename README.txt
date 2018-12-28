Example of a web-scraping web app that uses Python (and the BeautifulSoup parsing library). It abuses the Django framework just to get a quick way to execute a Python script from an AJAX call - not good Django practice at all I don't think.

Mostly done as an exercise to learn a real-world application of Python, and to create a version of NDNation that is easier to read. Could be adapted to other websites by updating the logic in NDNScraper_private.py, as much as of that is site-specific.

Update 12/27/18: In the process of porting this over to run on an Azure instance, I'm working through changing this to be served using a newer instance of Django, which has temporarily broken things. The core scraping logic would be portable pretty easily to a different framework if needed. This isn't currently running on my site due to the cost of keeping a Python instance running on Azure.

Reminder - boot sequence:
1. Prereq: python 2.7 installed
2. Navigate to /django_code
3. python manage.py runserver
4. Connect browser to the site (domain/~user/HTMLScraper/index.html)

