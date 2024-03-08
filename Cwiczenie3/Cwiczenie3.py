# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(-|\+)?[0-9]+(\.[0-9]+)?"

test_str = ("A regular expression (shortened as regex or regexp),[1] sometimes referred to as rational expression,[2][3] is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching algorithms for \"find\" or \"find and replace\" operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory.\n\n"
	"The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language. They came into common use with Unix text-processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax. -90\n"
	"PI=3.1415\n"
	"test1=-234.567\n"
	"test2=+987.654\n"
	"Regular expressions are used in search engines, in search and replace dialogs of word processors and text editors, in text processing utilities such as sed and AWK, and in lexical analysis. Regular expressions are supported in many programming languages. Library implementations are often called an \"engine\",[4][5] and many of these are available for reuse. ")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
input()