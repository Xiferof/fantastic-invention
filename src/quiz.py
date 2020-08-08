import os
import csv
import random
def generate_random_backround_list():
    with open(os.getcwd() + '/data/colour_list.csv', 'r') as f:
        reader = csv.reader(f)
        colour_list = reader.__next__()
    random.shuffle(colour_list)
    return colour_list


class Quiz:
    def __init__(self, username):
        """
        load the questions from disk, randomise them in place
        """
        self.question_list = list()
        self.response_index = dict()
        self.username = username 
        self.current_question_index = -1
        with open(os.getcwd() + '/data/question_list.csv', 'r') as f:
            reader = csv.reader(f)
            for x in reader:
                self.question_list.append(x)

    def present_question(self):
        """Presents the next question

        Returns:
            None
        TODO use generators here for speed and neater code
        """
        
        for x in range(len(self.question_list)):
            self.current_question_index = x
            yield self.question_list[x]
        
    def record_response(self, index:int):
        """records the response for the current question

        Args:
            index (int): index of the response
        """
        self.response_index[self.question_list[self.current_question_index][0]] = index
    def store_responses(self):
        """stores the responses into the database
        """
        csv_response = list()
        for key in self.response_index:
            csv_response.append(key, self.response_index[key])
        with open(os.getcwd() + '/data/user_response.csv', 'a') as f:
            writer = csv.writer(f)
            # write the user name
            writer.writerow(self.username)
            # write key, value of responses
            write.writerows(csv_response)

        