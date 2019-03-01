idx = 1
server_cap = 36000

by_course = {}
by_trainer = {}

db = {
    "course": by_course,
    "trainer": by_trainer
}


def get_duration(param):
    for ch in param:
        if ch in ["h", "m"]:
            param = param.replace(ch, " ")
    n = [float(e.strip()) for e in param.split()]
    return (n[0] * 60 + n[1]) * 60


def format_time(total_duration):
    hours = int(total_duration)
    minutes = (total_duration - hours) * 60
    seconds = int((minutes - int(minutes)) * 60)
    return f"{hours:02d}:{int(minutes):02d}:{seconds:02d}"


def print_result(tokens):
    links = db[tokens[1]]

    total_duration = 0.0

    for link in links[tokens[2]]:
        print(link[0])
        total_duration += link[1]

    m, s = divmod(total_duration, 60)
    h, m = divmod(m, 60)
    print(f"total duration: {int(h):02d}:{int(m):02d}:{int(s):02d}")


while True:
    line = input()
    if line.startswith("scrape"):
        print_result(line.split())
        break
    link_params = {}

    lecture_tokens = line.split(";")

    for lecture_token in lecture_tokens:
        token = lecture_token.split(":")

        if token[0] == "course" and token[1] not in by_course:
            by_course[token[1]] = []

        if token[0] == "trainer" and token[1] not in by_trainer:
            by_trainer[token[1]] = []

        if token[0] == "duration":
            link_params[token[0]] = get_duration(token[1])
        else:
            link_params[token[0]] = token[1]

    if server_cap - link_params["duration"] < 0:
        idx += 1
        server_cap = 36000

    server_cap -= link_params["duration"]

    link = f"https://streamcdn{idx}.softuni.bg/" \
        f"course={link_params['course']}" \
        f"&lecture={link_params['lecture']}" \
        f"&trainer={link_params['trainer']}"

    by_course[link_params["course"]].append((link, link_params["duration"]))
    by_trainer[link_params["trainer"]].append((link, link_params["duration"]))
