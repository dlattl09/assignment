# 자료구조
# 사용자에게 받은 infix를 profix로 변환시키면서 계산을 수행한다.

# Stack define
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return len(self.items)==0
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def size(self):
		return len(self.items)

# Stack에서의 top과 다음 요소
def secondtop(self):
	top = opStk.pop()
	secondtop = opStk.pop()
	get_secondtop = secondtop
	opStk.push(secondtop)
	opStk.push(top)
	return get_secondtop

def top(s):
	top = s.pop()
	get_top = top
	s.push(top)
	return get_top

# 스택의 우선순위
def order_op(operator):
	if ((operator == '+') or (operator == '-')): return 11
	elif ((operator == '*') or (operator =='/') or (operator == '%')): return 22
	elif operator == '(': return 10
	elif operator ==')' : return 40

# caculation
def cal(a,b,operator):
	if operator == '+' : return int(b)+int(a)
	elif operator == '-' : return int(b)-int(a)
	elif operator == '*' : return int(b)*int(a)
	elif operator == '/' : return int(b)/int(a)
	elif operator == '%' : return int(b)%int(a)

##############################

print('------------------------------------------------------------------')
print('| Implementing an Algorithm for Arithmetic Expression Evaluation |')
print('------------------------------------------------------------------')
opStk = Stack()  # 연산자 스택
valStk = Stack() # 피연산자 스택
exp = list(input('enter your Arithmetic expression : ')) # 사용자가 수식 입력
s = Stack()
for i in range(len(exp)-1,-1,-1):
	a = str(exp[i])
	s.push(a)           #수식 스택으로 구현
if s.size()==0: print('ERROR') # 사용자가 아무것도 입력 안했을 때 : 오류 메세지

for i in range(s.size()):
	exp_stack = s.pop()
	if exp_stack in ['0','1','2','3','4','5','6','7','8','9']:
		valStk.push(exp_stack)
	elif exp_stack in ['+','-','*','/','%','(',')']:
		opStk.push(exp_stack)
	if(valStk.size()==0) and(opStk.size()!=0): print('ERROR')
	elif ((valStk.size()!=0) and (opStk.size()!=0) and ((valStk.size())<opStk.size())):
		if top(opStk)==')':
			a=valStk.pop()
			operator_b = opStk.pop()
			operator = opStk.pop()
			operator_f = opStk.pop()
			b = valStk.pop()
			c = cal(a,b,operator)
			valStk.push(c)
	elif ((valStk.size()!=0) and (opStk.size()!=0)) and ((valStk.size()) ==(opStk.size())):
		if opStk.size()>=2:
			if order_op(top(opStk))<order_op(secondtop(opStk)):
				a = valStk.pop()
				operator1 = opStk.pop()
				operator2 = opStk.pop()
				b = valStk.pop()
				c = cal(a,b,operator2)
				opStk.push(operator1)
				valStk.push(c)


if opStk.size()!=0:
	 for i in range(opStk.size()):
		a = valStk.pop()
		operator = opStk.pop()
		b = valStk.pop()
		c = cal(a,b,operator)
		valStk.push(c)

if valStk.size()!=0:
	answer = valStk.pop()
	print('computer's answer = : ' , answer)
