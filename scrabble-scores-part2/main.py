import Test

def best_start(lst, word):
	best_score = 0
	best_score_index = 0
	for i in range(len(lst) - len(word) + 1):
		s = score(lst[i:i+len(word)], word)
		if (s > best_score):
			best_score = s
			best_score_index = i

	return best_score_index

def score(lst, word):
	total = 0
	multiplier = 1
	values = {
		'a': 1,
		'b': 3,
		'c': 3,
		'd': 2,
		'e': 1,
		'f': 4,
		'g': 2,
		'h': 4,
		'i': 1,
		'j': 8,
		'k': 5,
		'l': 2,
		'm': 3,
		'n': 1,
		'o': 1,
		'p': 3,
		'q': 10,
		'r': 1,
		's': 1,
		't': 1,
		'u': 1,
		'v': 4,
		'w': 4,
		'x': 8,
		'y': 4,
		'z': 10
	}

	for i in range(len(lst)):
		letter_value = values[word[i].lower()]
		if (lst[i] == 'DL'):
			total += letter_value * 2
		elif (lst[i] == 'TL'):
			total += letter_value * 3
		elif (lst[i] == 'DW'):
			multiplier *= 2
		else:
			total += letter_value

	return (total * multiplier)

Test.assert_equals(best_start(['-','DW','-','-','-','TL','-','-','-','TL','-','-','-','DW','-'], 'quiz'), 0)
Test.assert_equals(best_start(['-','DW','-','-','-','TL','-','-','-','TL','-','-','-','DW','-'], 'quit'), 5)
Test.assert_equals(best_start(['-','DW','-','-','-','TL','-','-','-','TL','-','-','-','DW','-'], 'quart'), 9)
Test.assert_equals(best_start(['-','DW','-','-','-','TL','-','-','-','TL','-','-','-','DW','-'], 'quartz'), 0)
