prompt = """
This is a mandatory tool for, at-least, instantiation of a 'notes.md' file and a 'notes_agent' LLM 
    chatbot instantiation for each (set of) [${{positioning}} and associated ${{artifact}}]
    to yield (per each ${{cognos}} instantiation):
        [${{positioning}}, ${{artifact}}, ${{notes.md}}]
"""
ret = "`Return:` = [${{positioning}}, ${{artifact}}, ${{notes.md}}]"
return_dict = [ret]
print(return_dict[0])
