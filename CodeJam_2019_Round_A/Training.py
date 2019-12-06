def lowest_score(student_skills, chosen_students):
    student_skills.sort()
    lowest = 0
    for num in range(chosen_students - 1):
        lowest += student_skills[chosen_students - 1] - student_skills[num]
    curr_lowest = lowest
    for num in range(chosen_students, len(student_skills)):
        lowest = lowest + (student_skills[num] - student_skills[num - 1]) * (chosen_students - 1) \
            - (student_skills[num - 1] - student_skills[num - chosen_students])
        if lowest < curr_lowest:
            curr_lowest = lowest
    return curr_lowest

def main():
    num_tests = int(input().strip())
    for test in range(1, num_tests + 1):
        _, chosen_students = [int(line) for line in input().strip().split()]
        student_skills = [int(line) for line in input().strip().split()]
        print("Case #{}: {}".format(test, lowest_score(student_skills, chosen_students)))

if __name__ == "__main__":
    main()