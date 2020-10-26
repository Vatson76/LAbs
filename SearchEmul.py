start_string = '''About Shakespeare: William Shakespeare (baptised 26 April 1564 – died 23 April 1616) was an
English poet and playwright, widely regarded as the greatest writer in the English language and the
world's pre-eminent dramatist. He is often called England's national poet and the "Bard of Avon" (or
simply "The Bard"). His surviving works consist of 38 plays, 154 sonnets, two long narrative poems, and
several other poems. His plays have been translated into every major living language, and are performed
more often than those of any other playwright. Shakespeare was born and raised in Stratford-uponAvon. At the age of 18 he married Anne Hathaway, who bore him three children: Susanna, and twins
Hamnet and Judith. Between 1585 and 1592 he began a successful career in London as an actor, writer,
and part owner of the playing company the Lord Chamberlain's Men, later known as the King's Men. He
appears to have retired to Stratford around 1613, where he died three years later. Few records of
Shakespeare's private life survive, and there has been considerable speculation about such matters as
his sexuality, religious beliefs, and whether the works attributed to him were written by others.
Shakespeare produced most of his known work between 1590 and 1613. His early plays were mainly
comedies and histories, genres he raised to the peak of sophistication and artistry by the end of the
sixteenth century. Next he wrote mainly tragedies until about 1608, including Hamlet, King Lear, and
Macbeth, considered some of the finest examples in the English language. In his last phase, he wrote
tragicomedies, also known as romances, and collaborated with other playwrights. Many of his plays
were published in editions of varying quality and accuracy during his lifetime, and in 1623 two of his
former theatrical colleagues published the First Folio, a collected edition of his dramatic works that
included all but two of the plays now recognised as Shakespeare's. Shakespeare was a respected poet
and playwright in his own day, but his reputation did not rise to its present heights until the nineteenth
century. The Romantics, in particular, acclaimed Shakespeare's genius, and the Victorians heroworshipped Shakespeare with a reverence that George Bernard Shaw called "bardolatry". In the
twentieth century, his work was repeatedly adopted and rediscovered by new movements in scholarship
and performance. His plays remain highly popular today and are consistently performed and
reinterpreted in diverse cultural and political contexts throughout the world. Source: Wikipedia'''

def action(dict1, task, dict2):
    if task == 'and':
        return(dict1|dict2)
    elif task == 'or':
        return(dict1&dict2)
    elif task == 'not':
        return(dict1 - dict2)

strings = start_string.split('\n')
words = []

for string in strings:
    words.extend(string.split(' '))
listofwords = []

while words:
    word = words.pop(0)
    if word in listofwords:
        pass
    else:
        listofwords.append(word)

#список слов
listofwords = [word.replace('(', '').replace(')', ''.replace(',', '').replace('.', '')) for word in listofwords]

# Ищем в каких строках есть эти слова
dictofwords = {}
for word in listofwords:
    listofins = []
    for i, string in enumerate(strings):
        if word in string:
            listofins.append(i)
    dictofwords[word] = set(listofins)

search_task = input('Введите запрос \n')
search_task = search_task.split(' ')

I = iter(search_task)
try:
    res = action(dictofwords[next(I)], next(I), dictofwords[next(I)])
    while I:
        res = action(res, next(I), dictofwords[next(I)])
except StopIteration:
    pass

print(res)
