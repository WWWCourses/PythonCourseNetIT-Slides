import re

''' Description:
	From an HTML code we want to remove tags, and repeated whitespaces, in order to extract the text only
'''

def strip_all_tags(html):
	rx = re.compile(r'(?s)<.+?>')
	return rx.sub('',html)

def strip_mult_spaces(data,count):
	rx = re.compile(r'\s{' + str(count) + ',}')
	return rx.sub(' ',data)

html = '''<div class="ac-head">
			<button class="btn btn-link" data-toggle="collapse" data-target="#collapse2"
			aria-expanded="true" aria-controls="collapse2">
				<span>
				02                          </span>
			<div>Променливи в Питон. (семестър 1)  (12.03.2020 в 18:30 ч.)</div>
			<div style="font-size:14px;">Модул: Основи на Питон, Продължителност: <b>3 учебни часа</b></div>
			</button>
		</div>
'''

data = strip_all_tags(html)
print('\n', '~'*10, 'after stripped tags', '~'*10)
print(data)

data_cleaned=strip_mult_spaces(data,2)
print('\n', '~'*10,'after space cleaning', '~'*10)
print(data_cleaned)