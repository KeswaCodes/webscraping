# cUrl_URL = curl -v -X GET "https://api.adzuna.com/v1/api/jobs/za/search/1?app_id=95c5a470&app_key=937982dda4b2b82969e27656088b9e0d&results_per_page=1&what_and=software%20engineering"

# TODO: loop through the first 5 pages or so to get results, getting all 100 posts on each page
# TODO: work on formatting string to required url string



# {"__CLASS__":"Adzuna::API::Response::JobSearchResults","count":8511,"mean":593139.52,}
# {"__CLASS__":"Adzuna::API::Response::JobSearchResults","count":8512,"mean":593139.52}
results = [{"latitude":-26.703988,"longitude":27.079099,"created":"2022-10-28T10:48:53Z","salary_is_predicted":"0","company":{"__CLASS__":"Adzuna::API::Response::Company","display_name":"OfferZen"},"description":"Software Engineer Are you a talented software engineer looking for your Dream Developer Job? OfferZen, the developer jobs marketplace, reverses the job search process. We connect developers with a vast network of top tech companies that are eager to apply to interview you This could be the last job posting you ever have to click on Why waste time applying to 100 different companies when you could build one OfferZen profile and have them come to you? You'll also receive upfront information about\u2026","redirect_url":"https://www.adzuna.co.za/land/ad/3633238261?se=iB6niMJ17xGoHIzMZVutLA&utm_medium=api&utm_source=95c5a470&v=E1E94E6532C7E6CA2DDAC0BD764C5D0055926DD9","location":{"area":["South Africa","North West","Southern","Potchefstroom"],"display_name":"Potchefstroom, Southern","__CLASS__":"Adzuna::API::Response::Location"},"title":"Software Engineer","__CLASS__":"Adzuna::API::Response::Job","id":"3633238261","category":{"__CLASS__":"Adzuna::API::Response::Category","label":"IT Jobs","tag":"it-jobs"},"adref":"eyJhbGciOiJIUzI1NiJ9.eyJpIjoiMzYzMzIzODI2MSIsInMiOiJpQjZuaU1KMTd4R29ISXpNWlZ1dExBIn0.hipGTC2Xn3hShXz8hgb4xmeltz9FMyFfU1CDfKRQyqw"}]



# job_location_str = results[0].get("location").get("display_name")
# res = "".join(job_location_str)                                           # get the location of the post
# location = res.split(",")[0]


# title = results[0].get("title")                                             # get the post title


# company_name = results[0].get("company").get("display_name")                  # get company name



# post_url = results[0].get("redirect_url")                                     # get link to job post (user must already have an OFFERZEN account, add disclaimer)








for r in results:
    print(r)
    print()
    print()

