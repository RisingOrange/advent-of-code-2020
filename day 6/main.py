from collections import Counter

def main(raw):
    groups_of_affirmations = [ 
        block.split('\n') 
        for block in raw.split('\n\n') 
    ]

    result = 0
    for affirmations_group in groups_of_affirmations:
        affirmation_per_question = Counter()
        for affirmations_of_person in affirmations_group:
            affirmation_per_question.update(affirmations_of_person)
        result += len([count for count in affirmation_per_question.values() if count == len(affirmations_group)])
    return result
        

if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(main(raw))

