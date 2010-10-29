import re, time


from pygments import highlight
from pygments.formatters import HtmlFormatter



try:
    set
except NameError:
    from sets import Set as set

from pygments.lexer import Lexer, RegexLexer,ExtendedRegexLexer, bygroups, include, do_insertions
from pygments.token import Text, Comment, Operator, Keyword, Name, \
     String, Number, Punctuation, Literal, Generic

from pygments.lexer import RegexLexer
from pygments.token import *

class RebolLexer(ExtendedRegexLexer):
    """
    A REBOL <http://www.rebol.com/> lexer.
    version 0.0.1 - David Oliva
    """
    name = 'REBOL'
    aliases = ['rebol']
    filenames = ['*.r', '*.r3'] 
    mimetypes = ['text/x-rebol']

    flags = re.IGNORECASE | re.MULTILINE
    
    re.IGNORECASE

    escape_re = r'(?:\^\([0-9a-fA-F]{1,4}\)*)'
    
    def word_callback(lexer, match, ctx):
        word = match.group(1)
        last = match.group(2)

        if re.match(".*:$",word):
            yield match.start(), Generic.Subheading, word
        elif re.match(
            r'(native|alias|all|any|as-string|as-binary|bind|bound\?|case'
            r'|catch|checksum|comment|debase|dehex|exclude|difference|disarm'
            r'|either|else|enbase|foreach|remove-each|form|free|get'
            r'|get-env|if|in|intersect|loop|minimum-of|maximum-of'
            r'|mold|new-line|new-line\?|not|now|prin|print'
            r'|reduce|compose|construct|repeat|reverse|save|script\?'
            r'|set|shift|switch|throw|to-hex|trace|try|type\?|union|unique|unless'
            r'|unprotect|unset|until|use|value\?|while|compress|decompress|secure'
            r'|open|close|read|read-io|write-io|write|update|query|wait|input\?'
            r'|exp|log-10|log-2|log-e|square-root|cosine|sine|tangent|arccosine'
            r'|arcsine|arctangent|protect|lowercase|uppercase|entab|detab|connected\?'
            r'|browse|launch|stats|get-modes|set-modes|to-local-file|to-rebol-file'
            r'|encloak|decloak|create-link|do-browser|bind\?|hide|draw'
            r'|show|size-text|textinfo|offset-to-caret|caret-to-offset|local-request-file'
            r'|rgb-to-hsv|hsv-to-rgb|crypt-strength\?|dh-make-key|dh-generate-key'
            r'|dh-compute-key|dsa-make-key|dsa-generate-key|dsa-make-signature'
            r'|dsa-verify-signature|rsa-make-key|rsa-generate-key|rsa-encrypt)$',word):
            yield match.start(), Name.Builtin, word
        elif re.match(
            r'(unset\?|error\?|datatype\?|native\?|action\?|routine\?|op\?|function\?'
            r'|object\?|struct\?|library\?|port\?|any-type\?|any-word\?|any-function\?'
            r'|number\?|series\?|any-string\?|any-block\?|word\?|set-word\?'
            r'|get-word\?|lit-word\?|refinement\?|none\?|logic\?|integer\?|decimal\?'
            r'|money\?|time\?|date\?|char\?|pair\?|event\?|tuple\?|bitset\?'
            r'|string\?|issue\?|binary\?|file\?|email\?|url\?|tag\?|image\?'
            r'|block\?|paren\?|path\?|set-path\?|lit-path\?|hash\?|list\?|add'
            r'|subtract|multiply|divide|remainder|power|and~|or~|xor~|same\?'
            r'|equal\?|strict-equal\?|not-equal\?|strict-not-equal\?|greater\?'
            r'|lesser\?|greater-or-equal\?|lesser-or-equal\?|minimum|maximum'
            r'|negate|complement|absolute|random|odd\?|even\?|negative\?|positive\?'
            r'|zero\?|head|tail|head\?|tail\?|next|back|skip|at|index\?|length\?'
            r'|pick|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth'
            r'|tenth|last|path|find|select|make|to|thru|copy|insert|remove|change)$',word):
            yield match.start(), Name.Function, word
        elif re.match(
            r'(error|source|input|license|help|install|echo|Usage|with|func'
            r'|throw-on-error|function|does|has|context|probe|\?\?|as-pair'
            r'|mod|modulo|round|repend|about|set-net|append|join|rejoin|reform'
            r'|remold|charset|array|replace|move|extract|forskip|forall|alter'
            r'|first+|also|take|for|forever|dispatch|attempt|what-dir|change-dir'
            r'|clean-path|list-dir|dirize|rename|split-path|delete|make-dir'
            r'|delete-dir|in-dir|confirm|dump-obj|upgrade|what|build-tag'
            r'|build-markup|decode-cgi|read-cgi|write-user|save-user|set-user-name'
            r'|protect-system|parse-xml|cvs-date|cvs-version|do-boot|get-net-info'
            r'|desktop|layout|scroll-para|get-face|alert|set-face|uninstall'
            r'|unfocus|request-dir|center-face|do-events|net-error|decode-url'
            r'|parse-header|parse-header-date|parse-email-addrs|import-email'
            r'|send|build-attach-body|resend|show-popup|hide-popup|open-events'
            r'|find-key-face|do-face|viewtop|confine|find-window|insert-event-func'
            r'|remove-event-func|inform|dump-pane|dump-face|flag-face|deflag-face'
            r'|clear-fields|read-net|vbug|path-thru|read-thru|load-thru|do-thru'
            r'|launch-thru|load-image|request-download|do-face-alt|set-font'
            r'|set-para|get-style|set-style|make-face|stylize|choose|hilight-text'
            r'|hilight-all|unlight-text|focus|scroll-drag|clear-face|reset-face'
            r'|scroll-face|resize-face|load-stock|load-stock-block|notify|request'
            r'|flash|request-color|request-pass|request-text|request-list|request-date'
            r'|request-file|dbug|editor|link-relative-path|emailer)$',word):
            yield match.start(), Keyword.Namespace, word
        elif re.match(
            r'(halt|quit|do|load|q|recycle|call|run|ask|parse|view|unview|'
            r'return|exit|break)$', word):
            yield match.start(), Name.Exception, word
        elif re.match('REBOL$', word):
            yield match.start(), Generic.Heading, word
        elif re.match("to-.*", word):
            yield match.start(), Keyword, word
        elif re.match('(\+|-|\*|/|//|\*\*|and|or|xor|=\?|=|==|<>|<|>|<=|>=)$',
                      word):
            yield match.start(), Operator, word
        elif re.match(".*\?$", word):
            yield match.start(), Keyword, word
        elif re.match(".*\!$", word):
            yield match.start(), Keyword.Type, word
        elif re.match("'.*", word):
            yield match.start(), Name.Variable.Instance, word # lit-word
        elif re.match("#.*", word):
            yield match.start(), Name.Label, word # issue
        elif re.match("%.*", word):
            yield match.start(), Name.Decorator, word # file
        else:
            yield match.start(), Name.Variable, word

        ctx.pos = match.start(2)

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'#"', String.Char, 'char'),
            (r'#{[0-9a-fA-F]*}', Number.Hex),
            (r'2#{', Number.Hex, 'bin2'),
            (r'64#{[0-9a-zA-Z+/=\s]*}', Number.Hex),
            (r'"', String, 'string'),
            (r'{', String, 'string2'),
            (r';#+.*\n', Comment.Special),
            (r';\*+.*\n', Comment.Preproc),
            (r';.*\n', Comment),
            (r'%"', Name.Decorator, 'stringFile'),
            (r'%[^(\^{^")\s\[\]]+', Name.Decorator),
            (r'<[a-zA-Z0-9:._-]*>', Name.Tag),
            (r'<[^(<>\s")]+', Name.Tag, 'tag'),
            (r'[+-]?([a-zA-Z]{1,3})?\$\d+(\.\d+)?', Number.Float), # money!
            (r'[+-]?\d+\:\d+(\:\d+)?(\.\d+)?', String.Other), # time
            (r'\d+\-[0-9a-zA-Z]+\-\d+(\/\d+\:\d+(\:\d+)?'
             r'([\.\d+]?([+-]?\d+:\d+)?)?)?', String.Other), # date!
            (r'\d+(\.\d+)+\.\d+', Keyword.Constant), # tuple!
            (r'\d+[xX]\d+', Keyword.Constant), # pair!
            (r'[+-]?\d+(\'\d+)?([\.,]\d*)?[eE][+-]?\d+', Number.Float),
            (r'[+-]?\d+(\'\d+)?[\.,]\d*', Number.Float),
            (r'[+-]?\d+(\'\d+)?', Number),
            #(r'[\(|\)]', Generic.Strong),
            (r'[\[\]\(\)]', Generic.Strong),
            (r'[a-zA-Z]+[^(\^{"\s:)]*://[^(\^{"\s)]*', Name.Decorator), #url!
            (r'mailto:[^(\^{"@\s)]+@[^(\^{"@\s)]+', Name.Decorator), #url!
            (r'[^(\^{"@\s)]+@[^(\^{"@\s)]+', Name.Decorator), #email!
            #(r'!=|==|<<|>>|[-~+/*%=<>&^|.]', Operator),
            #(r'[a-zA-Z]\:\/\/',Keyword),
            (r'comment\s', Comment,'comment'),
            (r'/[^(\^{^")\s/[\]]*', Name.Attribute),
            (r'([^(\^{^")\s/[\]]+)(?=[:({"\s/\[\]])', word_callback),
            (r'([^(\^{^")\s]+)', Text),
            ],
        'string': [
            (r'[^(\^")]+', String),
            (escape_re, String.Escape),
            (r'[\(|\)]+', String),
            (r'\^.', String.Escape),
            (r'"', String, '#pop'),
            ],
        'string2': [
            (r'[^(\^{^})]+', String),
            (escape_re, String.Escape),
            (r'[\(|\)]+', String),
            (r'\^.', String.Escape),
            (r'{', String, '#push'),
            (r'}', String, '#pop'),  
        ],
        'stringFile': [
            (r'[^(\^")]+', Name.Decorator),
            (escape_re, Name.Decorator),
            (r'\^.', Name.Decorator),
            (r'"', Name.Decorator, '#pop'),
            ],
        'char': [
            (escape_re + '"', String.Char, '#pop'),
            (r'\^."', String.Char, '#pop'),
            (r'."', String.Char, '#pop'),
        ],
        'tag': [
            (escape_re, Name.Tag),
            (r'"', Name.Tag, 'tagString'),
            (r'[^(<>\r\n")]+', Name.Tag),
            (r'>', Name.Tag, '#pop'),
        ],
        'tagString': [
            (r'[^(\^")]+', Name.Tag),
            (escape_re, Name.Tag),
            (r'[\(|\)]+', Name.Tag),
            (r'\^.', Name.Tag),
            (r'"', Name.Tag, '#pop'),
        ],
        'tuple': [
            (r'(\d+\.)+', Keyword.Constant),
            (r'\d+', Keyword.Constant, '#pop'),
        ],
        'bin2': [
            (r'\s+', Number.Hex),
            (r'([0-1]\s*){8}', Number.Hex),
            (r'}', Number.Hex, '#pop'),
        ],
        'comment': [
            (r'"', Comment, 'commentString1'),
            (r'{', Comment, 'commentString2'),
            (r'\[', Comment, 'commentBlock'),
            (r'[^(\s{\"\[]+', Comment, '#pop'),
        ],
        'commentString1': [
            (r'[^(\^")]+', Comment),
            (escape_re, Comment),
            (r'[\(|\)]+', Comment),
            (r'\^.', Comment),
            (r'"', Comment, '#pop'),
        ],
        'commentString2': [
            (r'[^(\^{^})]+', Comment),
            (escape_re, Comment),
            (r'[\(|\)]+',Comment),
            (r'\^.', Comment),
            (r'{', Comment, '#push'),
            (r'}', Comment, '#pop'), 
        ],
        'commentBlock': [
            (r'\[', Comment, '#push'),
            (r'\]', Comment, '#pop'),    
            (r'[^(\[\])]*', Comment),
        ],

        }



            


code = "x: 1 x{} 1 size? Len\n"\
    ';##Special comment\n'\
    ';**Preproc\n'\
    'print "Hello ^"World" while if 1 1-2 #"^(11)" #{aa}\n'\
    '1 + (x / 4.5) * 1E-4\n'\
    '1:0 1:1:1 -0:1.1\n'\
    '1-Feb-2009 1-Feb-2009/2:24:46+1:0\n'\
    '1.1.1.200\nto integer!\n---: 1\n'\
    '64#{aGVsbG8=}\n'\
    '%xx/s %"^""\n'\
    '$1 -$1.2 USA$100\n'\
    'http:// dns:// tcp://127.0.0.1\n'\
    'aaa@bbb.cz\n'\
    '1 == 3 xor x\n'\
    '\'print\n'\
    '<a> <a href="a()">\n'\
    '2#{0000 00000} 2#{}\n'\
    'bla ;test\n'\
    '{a{b}c} x/(1 + n)/y b/:1 \n'\
    'return 11.0.1\n1x1\n ask suffix? %bla.swf\n'\
    'reduce [\'now 10x200]\n'\
    '#include \n'\
    'ask? 1-jan-2001 xxx? [1] xxx?[ xxx?{x}'+"""
comment {
xxx 23
s: sds
}
comment [
    x: copy []
]
style: %default
out: rejoin [{
<html>
<head>
  <title>Pygments &mdash; Python syntax highlighter</title>
  <link rel="stylesheet" href="} style {.css">
</head>
<body>
<div class="syntax"><pre>
}]
css: read/lines join style %.css
foreach line css [
    parse line [".syntax ." copy c to " " thru "/*" copy t to "*/" to end (
        append out rejoin ["<span class=" c ">" t "</span>^/"])
    ]
]
write join style %.html join out "</pre></div></body></html>"
comment now
comment {bla}
comment [quit]
halt

]"""

#print code
#print re.match('(print|prin|ask\?)$',"ask?")
#p = ['print','prin','ask\?']
#print 'ask?' in p
time.clock()
#for i in range(1, 5000):
#   re.match('(print|prin)$',"prin")
    #'prin' in p
formatter = HtmlFormatter(linenos=True, cssclass="syntax")
result = highlight(code, RebolLexer(), formatter)
#print result
html = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>
  <title>Pygments &mdash; Python syntax highlighter</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
""" +result+"</body></html>"
f = open( "out.html", "w" )
f.write( html )
f.close()


    
print time.clock()