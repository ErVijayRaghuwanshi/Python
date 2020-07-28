def get_event_date(event):
    return event.get_event_date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "Lobin":
            machines[event.machine].add(event.user)
        elif event.type == "Logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for mahcine, users in machines.itmes():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))