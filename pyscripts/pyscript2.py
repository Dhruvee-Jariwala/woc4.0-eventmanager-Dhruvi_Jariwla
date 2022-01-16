from bs4 import BeautifulSoup
import requests

def find_jobs():
    skill_not_known = input("Which skill you don't know? ------> ")

    html_obj = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_obj,'html.parser')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').text

        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            job_desc = job.find('ul',class_='list-job-dtl clearfix').find('li').text
            more_info = job.header.h2.a['href']
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')

            if skill_not_known not in skills:
                job_file = open("job_file.txt","a")
                job_file.write("Company : " + company_name + "\n")
                job_file.write(job_desc + "\n")
                job_file.write("Skills required : " + skills + "\n")
                job_file.write("More info : " + more_info + "\n")
                job_file.write("===================================================" + "\n")
                job_file.write("\n")
                print("File saved - " + str(index))
                job_file.close()

if __name__ == '__main__':
    find_jobs()
