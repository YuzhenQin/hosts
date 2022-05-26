import dns.resolver

DEBUG = False

with open('domains') as f:
    domains = f.readlines()

resolver = dns.resolver.Resolver()
resolver.nameservers = [ '8.8.8.8', '8.8.4.4' ]

for i in domains:
    q = resolver.resolve(i.strip(), 'A')
    for i in q.response.answer:
        if DEBUG:
            print(i.to_text())
        else:
            ans = i.to_text().split()
            if ans[3] == 'A':
                print(ans[0].rstrip('.'), ans[4])