# Mandy_Crawl
A web crawler project to scrape *timesjobs.com* for jobs every 10 minutes

**Libraries Used**
1. BeautifulSoup
2. requests
3. time

**Program Functionality**
The program has a main function, **find_jobs()** which contains all the main functions of the program
1. The program allows you to enter a skill your're unfamiliar with and stores it as *unfamiliar_skill*
2. The program requests access to the website and stores it as *html_text*
3. It the creates an instance of the BeautifulSoup as *soup*
4. It then finds the jobs and saves it in *jobs*
5. The program also checks for the date of publication and stores it as *published_date*
6. The results are only displayed if the *published_date* contains *few*
7. The results are the *company_name, skills, more_info*
8. *company_name* returns the company name without white spaces
9. *skills* also returns the skills listed as required by the company without white spaces
10. *more_info* returns the link to more information on the website
11. But the results are once again only displayed if it doesn't contain the *unfamiliar_skill*
12. Once all these are met, the results are saved to a file with a name as the index of the instance it was found. The reults are all diplayed on new lines in the file saved to
13. Finally when the program is run, it calls the main function *find_jobs* and keeps it running and produces new results evry 10 minutes
