scholl_scores_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
					 {'school_class': '4b', 'scores': [4,4,4,4,4]},
					 {'school_class': '5a', 'scores': [5,4,5,4,2]},
					 {'school_class': '5b', 'scores': [4,4,5,5,4]},
					 {'school_class': '11b', 'scores': [3,4,2,5,4]},
					 {'school_class': '10a', 'scores': [4,4,4,4,5]},
					 {'school_class': '10b', 'scores': [3,4,3,2,2]}
					 ]

def mid_scores(list):
	sum_av_scores = 0
	for s_class in scholl_scores_list:
		class_number = s_class.get('school_class')
		all_scores = s_class.get('scores')
		sum_class_scores = 0
		for score in all_scores:
			sum_class_scores += score
		av_score_class = sum_class_scores / len(all_scores)
		sum_av_scores += av_score_class
		print('Class {0}, average score {1}'.format(class_number, av_score_class))
	common_av_score = sum_av_scores / len(scholl_scores_list)
	print('Common average score in school: {0:.2f}'.format(common_av_score))


print('Hello')
print(mid_scores(scholl_scores_list))
