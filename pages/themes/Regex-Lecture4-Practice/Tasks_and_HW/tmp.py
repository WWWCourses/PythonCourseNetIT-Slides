import re

def strip_all_tags(html):
    """Remove all HTML tags from the input string."""
    tag_re = re.compile(r'<[^>]+>')
    return tag_re.sub('', html)

def normalize_spaces(data):
    """Replace multiple spaces with a single space and trim leading and trailing spaces"""
    space_re = re.compile(r'\s+')
    return space_re.sub(' ', data).strip()

html = '''
<div class="ac-head">
    <button class="btn btn-link" data-toggle="collapse" data-target="#collapse2" aria-expanded="true" aria-controls="collapse2">
        <span>
        02                          </span>
    <div>Променливи в Питон. (семестър 1)  (12.03.2020 в 18:30 ч.)</div>
    <div style="font-size:14px;">Модул: Основи на Питон, Продължителност: <b>3 учебни часа</b></div>
    </button>
</div>
'''

# Strip HTML tags
data = strip_all_tags(html)
print('\n', '~' * 10, 'After stripping tags', '~' * 10)
print(data)

# Clean up multiple spaces
data_cleaned = normalize_spaces(data)
print('\n', '~' * 10, 'After space cleaning', '~' * 10)
print(data_cleaned)
