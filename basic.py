from deeppavlov.skills.pattern_matching_skill import PatternMatchingSkill
from deeppavlov.agents.default_agent.default_agent import DefaultAgent
from deeppavlov.agents.processors.highest_confidence_selector import HighestConfidenceSelector

hello = PatternMatchingSkill(responses=['Hello world!'], patterns=["hi", "hello", "good day"])
bye = PatternMatchingSkill(['Goodbye world!', 'See you around'],patterns=["bye", "chao", "see you"])
fallback = PatternMatchingSkill(["I don't understand, sorry", 'I can say "Hello world!"'])



agent = DefaultAgent([hello, bye, fallback], skills_selector=HighestConfidenceSelector())

print("Hello this is Deeppavlov assistant")

s = input()
x=[]
while s!="exit":
   x.insert(0,s)
   print(agent(x))
   s=input()

   
#print(agent(['Hello', 'Bye', 'Or not']))
