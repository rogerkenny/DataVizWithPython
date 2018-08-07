import re

def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r"[a-zA-Z0-9\-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$", s)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
	fi = open('emails_001.txt', 'r')	
	n = int(fi.readline().strip())
	emails = []
	for _ in range(n):
		emails.append(fi.readline().strip())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)