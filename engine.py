def evaluate(data, fixture_path):
    state = data["initial"]
    applied = set()
    findings = []
    for index, delivery in enumerate(data["deliveries"]):
        accepted = delivery["accepted"]
        resulting_state = delivery["state"]
        event_id = delivery["event_id"]
        if type(accepted) is not bool or not isinstance(event_id, str) or not event_id:
            raise ValueError("deliveries require an event ID and a boolean accepted field")
        if accepted:
            if event_id in applied:
                findings.append({"code": "duplicate_applied", "delivery": index})
            elif resulting_state not in data["transitions"].get(state, []):
                findings.append({"code": "invalid_transition", "delivery": index})
            applied.add(event_id)
        elif resulting_state != state:
            findings.append({"code": "rejected_event_changed_state", "delivery": index})
        state = resulting_state
    return findings
