import math

def max_beauty_score(beauty_scores, sections):
    start, end = 0, math.ceil(sections / 2)
    max_score = sum(beauty_scores[start:end])
    new_score = max_score
    for next in range(end, sections):
        new_score = new_score - beauty_scores[start] + beauty_scores[next]
        start += 1
        if new_score > max_score:
            max_score = new_score
    return max_score

def main():
    num_tests = int(input().strip())
    for i in range(num_tests):
        sections = int(input().strip())
        beauty_scores = [int(score) for score in input().strip()]
        result = max_beauty_score(beauty_scores, sections)
        print(f'Case #{i + 1}: {result}')

if __name__ == "__main__":
    main()