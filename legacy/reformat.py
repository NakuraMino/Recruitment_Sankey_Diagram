import csv


# Format: 
# [Applied]
# [Resume Rejected, Resume Ghosted, Coding Challenge]
# [recruiter phone call]
# [on-campus]
# [onsite]
#

with open("data/applications2021.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    applied_total = 0
    cc_total = 0
    recruiter_total = 0
    phone_total = 0
    on_total = 0
    onsite_total = 0
    accepted = 0
    ghosted = 0
    rejected = 0
    ongoing = 0

    sankey_rows = {}

    for row in csv_reader:
        comp = row['Company']
        role = row['Role name']
        date = row['Applied Date']
        cc = row['Coding Challenge']
        recruiter = row['Recruiter']
        phone = row['Phone']
        on_campus = row['On-Campus']
        onsite = row['Onsite']
        result = row['Result']

        if role != '' or date != '':
            sankey = "['Applied'"
            applied_total += 1

            if cc != '':
                sankey += ", 'Coding Challenge'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Coding Challenge'"
                cc_total += 1
            
            if recruiter != '':
                sankey += ", 'Chat w/ recruiter'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Chat w/ recruiter'"
                recruiter_total += 1
            
            if phone != '':
                sankey += ", 'Phone Interview'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Phone Interview'"
                phone_total += 1
            
            if on_campus != '':
                sankey += ", 'On-campus Interview'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['On-campus Interview'"
                
                on_total += 1

            if onsite != '':
                sankey += ", 'Onsite'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Onsite' "

                onsite_total += 1
            
            if result == "Accepted!":
                sankey += ", 'Accepted!'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Accepted!' "

                accepted += 1
            elif result == '':
                sankey += ", 'Ghosted'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Ghosted' "

                ghosted += 1
            elif result == "ongoing":
                sankey += ", 'Ongoing'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Ongoing' "

                ongoing += 1
            else:
                sankey += ", 'Rejected'"

                if sankey not in sankey_rows:
                    sankey_rows[sankey] = 0
                sankey_rows[sankey] += 1

                sankey = "['Rejected' "

                rejected += 1

    for key in sankey_rows:
        print(key + ", " + str(sankey_rows[key]) + "],")

    print()


    print("applied_total: " + str(applied_total))
    print("coding challenges: " + str(cc_total))
    print("Talks with Recruiter: " + str(recruiter_total))
    print("Phone Interviews: " + str(phone_total))
    print("On-Campus Interviews: " + str(on_total))
    print("Onsite Interviews: " + str(onsite_total))
    print("Accepted: " + str(accepted))
    print("Ghosted: " + str(ghosted))
    print("Rejected: " + str(rejected))
    print("Ongoing: " + str(ongoing))
