import requests
import datetime

apiUrl = "https://codeforces.com/api/user.status"

parameters = {"handle": "shifat57"}


def getSubmissions():

    submissions = []

    try:
        req = requests.get(url=apiUrl, params=parameters)

        data = req.json()

        # print(req.json())

        if(data['status'] == 'OK'):
            # submissions = data['result'][0]

            demo = data['result']
            rating = " "
            contest_id = " "

            for i in range(len(demo)):

                if "rating" in demo[i]["problem"]:

                    rating = demo[i]["problem"]["rating"]

                else:
                    rating = "undefined"

                if "contestId" in demo[i]["problem"]:

                    contest_id = str(demo[i]["problem"]["contestId"])

                else:
                    rating = "undefined"

                if(demo[i]["verdict"] == 'OK'):
                    submissions.append({
                        "problem_name": demo[i]["problem"]["name"],

                        "index": demo[i]["problem"]["index"],

                        "submission_id": str(demo[i]["id"]),

                        "contest_id": str(contest_id),

                        "problem_link": "https://codeforces.com/contest/"+contest_id+"/problem/"+demo[i]["problem"]["index"],

                        "solution_link": "https://codeforces.com/contest/"+contest_id+"/submission/" + str(demo[i]["id"]),

                        "rating": str(rating),

                        "tags": ', '.join([str(elem) for elem in (demo[i]["problem"]["tags"])])  ,

                        "programmingLanguage" : demo[i]["programmingLanguage"],
 

                        "submission_time": datetime.datetime.utcfromtimestamp(
                            demo[i]["creationTimeSeconds"]).strftime('%d %B %Y %H:%M:%S'),
                    })

            unique_submissions = list(
                {v['problem_name']: v for v in submissions}.values())


            return unique_submissions

            

    except requests.exceptions.RequestException as error:
        print(error)


# getSubmissions()
