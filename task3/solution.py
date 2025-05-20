def merge_intervals(times):
    times = sorted((times[i], times[i+1]) for i in range(0, len(times), 2))
    merged = []
    for start, end in times:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

def intersect_intervals(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            result.append([start, end])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil = merge_intervals(intervals['pupil'])
    tutor = merge_intervals(intervals['tutor'])
    lesson_interval = [[lesson[0], lesson[1]]]
    pupil_in_lesson = intersect_intervals(pupil, lesson_interval)
    tutor_in_lesson = intersect_intervals(tutor, lesson_interval)
    both_present = intersect_intervals(pupil_in_lesson, tutor_in_lesson)
    return sum(end - start for start, end in both_present)
