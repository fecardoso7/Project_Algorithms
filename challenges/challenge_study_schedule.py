def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for beginning, finish in permanence_period:
            if beginning <= target_time <= finish:
                count += 1
        return count
    except TypeError:
        return None
    