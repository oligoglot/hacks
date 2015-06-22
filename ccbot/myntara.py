__author__ = 'sundar'

from pyparsing import *

def processOrderQuery(tokens):
	print 'order', tokens

def processExchangeQuery(tokens):
	print 'exchange', tokens

def processReturnsQuery(tokens):
	print 'returns', tokens

def processRefundQuery(tokens):
	print 'refund', tokens

def processQuery(tokens):
	print tokens[1][1], tokens[0],
	if len(tokens) == 3 and len(tokens[2]) == 2:
		print tokens[2][1]
	else:
		print

def processGreeting(tokens):
	print tokens[0]

greeting = oneOf('hi hello', caseless = True)
greeting.setParseAction(processGreeting)
qword = oneOf('what when where how', caseless = True)
ender = oneOf('? .')
iword = Optional(Suppress(Word(alphas))) 
ignorable = ((iword + iword + iword) | (iword + iword) | (iword))

order_withnum = qword + SkipTo(CaselessLiteral('order'), include = True) + SkipTo(Word(nums), include = True)
order_nonum = qword + SkipTo(CaselessLiteral('order'), include = True) + Suppress(Regex(r'[^0-9]+')) + StringEnd()
order = order_withnum | order_nonum
#order = qword + SkipTo(CaselessLiteral('order'), include = True) + iword + Combine(Optional(Word(nums)) + Optional(Suppress(ender))) + StringEnd()
order.setParseAction(processQuery)

exchange_withnum = qword + SkipTo(CaselessLiteral('exchange'), include = True) + SkipTo(Word(nums), include = True)
exchange_nonum = qword + SkipTo(CaselessLiteral('exchange'), include = True) + Suppress(Regex(r'[^0-9]+')) + StringEnd()
exchange = exchange_withnum | exchange_nonum
exchange.setParseAction(processQuery)

return_withnum = qword + SkipTo(CaselessLiteral('return'), include = True) + SkipTo(Word(nums), include = True)
return_nonum = qword + SkipTo(CaselessLiteral('return'), include = True) + Suppress(Regex(r'[^0-9]+')) + StringEnd()
returns = return_withnum | return_nonum
#returns = qword + SkipTo(CaselessLiteral('return'), include = True) + iword + Combine(Optional(Word(nums)) + Optional(Suppress(ender))) + StringEnd()
returns.setParseAction(processQuery)

refund_withnum = qword + SkipTo(CaselessLiteral('refund'), include = True) + SkipTo(Word(nums), include = True)
refund_nonum = qword + SkipTo(CaselessLiteral('refund'), include = True) + Suppress(Regex(r'[^0-9]+')) + StringEnd()
refund = refund_withnum | refund_nonum
#refund = qword + SkipTo(CaselessLiteral('refund'), include = True) + iword + Combine(Optional(Word(nums)) + Optional(Suppress(ender))) + StringEnd()
#refund = qword + Optional(Suppress(Word(alphas))) + Optional(Suppress(CaselessLiteral('my'))) + Optional(Suppress(Word(alphas))) + CaselessLiteral('refund') + Optional(Suppress(Word(alphas))) + Optional(Word(nums))
refund.setParseAction(processQuery)

other = Regex(r'.*')
query = (greeting | order | exchange | returns | refund | other)

msg = ''
while(not msg == 'bye'):
	msg = raw_input().strip()
	#print msg
	if msg != 'hi' and msg != 'bye' and not msg.endswith('?') and not msg.endswith('.'):
		msg = msg + '?'
	query.parseString(msg)
	#print
