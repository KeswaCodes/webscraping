# cUrl_URL = curl -v -X GET "https://api.adzuna.com/v1/api/jobs/za/search/1?app_id=95c5a470&app_key=937982dda4b2b82969e27656088b9e0d&results_per_page=1&what_and=software%20engineering"
import requests

# TODO: loop through the first 5 pages or so to get results, getting all 100 posts on each page
# TODO: work on formatting string to required url string

'''
    main driver function
'''
def main():
    jobs = getJobs()           # get jobs from the database
    filtered = filterJobs(jobs, "Johannesburg")
    filteredJobs = matchPost(filtered, "software engineer") # get all the jobs according to the user's job post



'''
    function makes API request to adzuna job webscraper API and returns the results    
    @returnValue: (JSON object) a list of dictionaries of the jobs from the adzuna database
'''
def getJobs():

    url = "https://api.adzuna.com/v1/api/jobs/za/search/1"
    params = {"app_id":"95c5a470", "app_key":"937982dda4b2b82969e27656088b9e0d", "results_per_page": 20, "what_and":"software engineering"}
    result = requests.get(url, params=params)
    return result.json().get("results")



'''
    function appends jobs to list if they do match the user's location    
    @jobs is a list of jobs returned from the database
    @returnValue: a list of jobs matching user desired location
'''
def filterJobs(jobs, user_location):
    listJobs = []                  # create a list for jobs matching the user location 
    for job in jobs:
        matchesLocation = matchJobLocation(user_location, job)
        if matchesLocation:
            listJobs.append(job)
    return listJobs



'''
    function matches job location on for jobs on database to user's location
    @returnValue: True if the job location matches user location, False if otherwise
'''
def matchJobLocation(target_location, result):

    job_location_str = result.get("location").get("display_name")
    res = "".join(job_location_str)                                           # get the location of the post
    location = res.split(",")[0]
    if location == target_location:
        return True
    return False



'''
    function matches jobs according to the job post
    @jobs: a list of jobs matching the user location
    @returnValue: a list of jobs matching the user's desired job post
'''
def matchPost(jobs, desired_post):
    matches = []
    for job in jobs:
        title = job.get("title")
        # print("Title ===> ", desired_post in title.lower())
        if desired_post in title.lower():
            matches.append(job)
    return matches
            


# company_name = results[0].get("company").get("display_name")                  # get company name



# post_url = results[0].get("redirect_url")                                     # get link to job post (user must already have an OFFERZEN account, add disclaimer)








if __name__ == "__main__":
    main()