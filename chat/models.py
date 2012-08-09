from django.db import models

import string
import random

# Create your models here.

def tokenize(mystring):
	output = ""
	if mystring[-1] not in string.punctuation:
		mystring += "."
	for letter in mystring:
		if letter in string.punctuation:
			output += " "
		output += letter
	return output.strip().split()

def strip_punctuation(word_list):
	result = []
	for i, word in enumerate(word_list):
		if not word[0] in string.punctuation:
			result.append(word)
	return result

class Bot(models.Model):
	name = models.CharField(max_length=40)

	def train(self, word_list):
		prev = None
		for word in word_list:
			if prev != None:
				newpair = WordPair(first=prev, second=word, bot=self)
				newpair.save()
			prev = word

	def respond(self, word_list):
		word_list = list(word_list)
		random.shuffle(word_list)
		prev_word = "the"  #TODO: Magic string
		for prev_word in word_list:
			if len(WordPair.objects.filter(bot=self, first=prev_word)) > 0:
				break;

		result = prev_word
		while not prev_word[0] in ".?!":
			pairs = WordPair.objects.filter(bot=self, first=prev_word)
			if len(pairs) == 0:
				prev_word = '.'
			else:
				index = random.randint(0, pairs.count()-1)
				pair = pairs.all()[index]
				prev_word = pairs.order_by('?')[0].second
			result += " " + prev_word
		return result

	def ask(self, question):
		word_list = tokenize(question)
		self.train(word_list)
		return self.respond(strip_punctuation(word_list))

class WordPair(models.Model):
	first = models.CharField(max_length=40)
	second = models.CharField(max_length=40)
	bot = models.ForeignKey(Bot)
	def __unicode__(self):
		return "{0}:  {1} => {2}".format(self.bot, self.first, self.second)

