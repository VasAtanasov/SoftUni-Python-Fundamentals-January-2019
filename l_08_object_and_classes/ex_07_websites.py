class Website:
    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = queries

    def __str__(self):
        output = f"https://www.{self.host}.{self.domain}"
        if self.queries:
            return output + f"/query?={'&'.join(map(lambda query: f'[{query}]', self.queries))}"
        else:
            return output


while True:
    line = input()
    if "end" == line:
        break

    tokens = line.split(" | ")
    site = None
    if len(tokens) == 2:
        site = Website(tokens[0], tokens[1])
    else:
        site = Website(tokens[0], tokens[1], tokens[2].split(","))

    print(site)
