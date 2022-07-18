def get_results(results, submission):
    print("Results:")
    [print(f"{key} | {value}") for key, value in results.items()]
    print("Submissions:")
    [print(f"{key} - {value}") for key, value in submission.items()]


command = input()
submission = {}
results = {}


while command != "exam finished":
    params = command.split("-")
    name = params[0]
    if len(params) > 2:
        language, points = params[1], int(params[2])
        if name not in results:
            results[name] = 0
        if points > results[name]:
            results[name] = points
        if language not in submission:
            submission[language] = 0
        submission[language] += 1
    else:
        del results[name]

    command = input()

get_results(results, submission)

