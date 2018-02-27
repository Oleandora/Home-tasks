scholl_scores_list = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                      {'school_class': '4b', 'scores': [4, 4, 4, 4, 4]},
                      {'school_class': '5a', 'scores': [5, 4, 5, 4, 2]},
                      {'school_class': '5b', 'scores': [4, 4, 5, 5, 4]},
                      {'school_class': '11b', 'scores': [3, 4, 2, 5, 4]},
                      {'school_class': '10a', 'scores': [4, 4, 4, 4, 5]},
                      {'school_class': '10b', 'scores': [3, 4, 3, 2, 2]}
                      ]


def average_scores(scholl_list):
    sum_of_average_scores = 0
    for s_class in scholl_list:
        class_number = s_class.get('school_class')
        all_scores = s_class.get('scores')
        sum_class_scores = 0
        for score in all_scores:
            sum_class_scores += score
        average_score_of_class = sum_class_scores / len(all_scores)
        sum_of_average_scores += average_score_of_class
        print('Class {0}, average score of class {1}'.format(class_number, average_score_of_class))
    school_common_average_score = sum_of_average_scores / len(scholl_list)
    print('Common average score in school: {0:.2f}'.format(school_common_average_score))


print('Hello')
print(average_scores(scholl_scores_list))
