marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2, 'investor relations')
print(marketing)

Emailmarketing = marketing.copy()
Emailmarketing.sort()

internalEmails = ['internal communication']
print(internalEmails + Emailmarketing)

#tuple
Emails = tuple(Emailmarketing)
print(Emails)




#Dictionary
chanels = {"Google" : 1480, "Email" : 300, "Natural Traffic" : 440, "TV Spot" : 700}
print(chanels)
print(chanels["Email"])

chanelsUpdate = {"Natural Traffic" : 520, "News" : 600}
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
print(chanels.pop("Email"))
print(chanels)





