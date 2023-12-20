import random
import sys


class ChatAgent:  # replace this with your last name, like SchlueterChatAgent
    """ChatAgent - This is a very simple ELIZA-like computer program in python.
      Your assignent in Programming Assignment 1 is to improve upon it.

      I've created this as a python object so that your agents can chat with one another
      (and also so you can have some practice with python objects)
      """

    def generateReply(self, inString):
        """Pick a random function, and call it on the input string """
        randFunction = random.choice(self.ReplyFunctionList)  # pick a random function, I love python
        reply = randFunction(inString)
        return reply

    def generatePrefix(self, inString):
        if self.UserInputHistory:
            earlier_input = random.choice(self.UserInputHistory)
            return f"Earlier you said that {earlier_input}."
        else:
            return random.choice(self.PrefixList)

    def driverLoop(self):
        reply = "how are you today?"
        while True:
            response = input(reply)
            self.UserInputHistory.append(response)  # Add user input to the history list
            reply = self.generateReply(response)

    def swapPerson(self, inWord):
        """Replace 'I' with 'You', etc"""
        if (inWord in self.PronounDictionary.keys()):  # if the word is in the list of keys
            return self.PronounDictionary[inWord]
        else:
            return inWord



    def switch_person(self, inString):
        """
        the following function takes a string and see if any pronoun needs to be changed to a second person
        e.g. "you" will be replaced with "I" and vice versa
        """
        inWordList = str.split(inString)
        newWordList = []

        for word in inWordList:
            if word in self.PronounDictionary:
                newWordList.append(self.PronounDictionary[word])
            else:
                newWordList.append(word)

        reply = ' '.join(newWordList)
        return reply



    def changePersonAndAddPrefix(self, inString):
        reply = self.switch_person(inString)
        randomPrefix = random.choice(self.PrefixList)
        return ''.join([randomPrefix, reply])

    def generateHedge(self, inString):
        return random.choice(self.HedgeList);

    def __init__(self):
        self.PronounDictionary = {'i': 'you', 'I': 'you', 'am': 'are',
                                  'you': 'I', 'are': 'am', 'myself': 'yourself',
                                  'ourselves': 'yourselves', 'we': 'you', 'us': 'you', 'our': 'your', 'ours': 'yours',
                                  'your': 'my', 'yours': 'mine', 'me': 'you', 'my': 'your', 'mine': 'yours'}

        self.HedgeList = ["Hmm", "That is fascinating", "Let's change the subject,",
                          "Do you have anything more to say? "
                          "You can talk to me.", "Well, I hope"
                                                 "it was great learning experience.",
                          "Hmm, interesting point you raised there,", "That's thought-provoking,",
                          "Let's explore a different angle now,", "Do you have any further insights to offer?",
                          "You're free to express your thoughts here,",
                          "Well, I hope you gained valuable insights from it,",
                          "I appreciate your perspective on this,", "What's your next topic of interest?",
                          "Feel free to share your thoughts openly,", "Is there something else you'd like to discuss?",
                          "Hmm,", "That's quite intriguing,", "Let's shift our focus for a moment,",
                          "Is there anything else on your mind?", "Feel free to continue the discussion.",
                          "Well, I trust it was an enriching learning experience,",
                          "What else would you like to share?", "You have my full attention,",
                          "What other thoughts do you have?"]

        self.PrefixList = ["Why do you say that ", "What do you mean that ", "Can you elaborate on that", "Well, "
                                                                                                          "that's interesting. What else do you have to share?",
                           "What happened after that?", "Why do you say that?", "What do you mean by that?",
                           "Can you elaborate on that?", "Well,", "That's interesting. What else do you have to share?",
                           "What happened after that?", "I'm not sure I understand. Can you explain further?",
                           "Could you clarify what you mean by...", "I'd like to learn more about...",
                           "That's fascinating! Tell me more about it.",
                           "I'm intrigued. What else can you share on this topic?",
                           "I'd love to hear more about your perspective on...",
                           "Can you provide more details on that?",
                           "What specific examples or instances can you share?",
                           "I'm interested in the specifics. Could you elaborate?",
                           "Could you share a personal experience related to this?",
                           "Have you ever encountered a situation where...",
                           "What was your experience like in that context?",
                           "Let's discuss this further. What are your thoughts on...",
                           "I'm open to different viewpoints. How do you see it?",
                           "How might this idea relate to other concepts or issues?", "What happened before that?",
                           "And then what followed?", "Could you walk me through the sequence of events?",
                           "I can see how that might be challenging/exciting.",
                           "It sounds like you had quite an experience.",
                           "I understand how that could be confusing/frustrating.",
                           "How does this compare to [related topic]?",
                           "In contrast, what are the differences between [X] and [Y]?",
                           "Can you draw any parallels between this and [another context]?",
                           "Are there alternative ways to approach this?",
                           "Have you considered other options or solutions?",
                           "What are the potential alternatives to [current approach]?",
                           "What do you think the future holds for [topic]?",
                           "How might this impact [industry/society] in the long run?",
                           "What potential developments should we be aware of?"

                           ]
        self.UserInputHistory = []

        self.ReplyFunctionList = [self.generateHedge, self.switch_person,
                                  self.changePersonAndAddPrefix, self.generatePrefix]  # this is what makes Python so powerful
    # End of ChatAgent


if __name__ == '__main__':  # will only be called if this is invoked directly by python, as opposed to included in a larger file

    # version checking
    MIN_PYTHON = (3, 7)
    assert sys.version_info >= MIN_PYTHON, "requires Python 3, run with `python3 eliza.py`"

    # program starts here

    random.seed()  # if given no value, it uses system time
    agent = ChatAgent()
    agent.driverLoop()
