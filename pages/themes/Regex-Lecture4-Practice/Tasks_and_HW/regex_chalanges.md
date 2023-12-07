## Python Homework Assignment: Regular Expression Challenges

### Objective
Utilize Python's `re` module to solve a series of text manipulation challenges, demonstrating your mastery of regular expressions.

### Tasks
You are provided with a series of strings. Your task is to write Python functions using regular expressions to transform these strings as specified.

1. **Email Anonymizer:**
   - **Input:** A string containing email addresses.
   - **Output:** The same string but with email addresses replaced by `"[email]"`.
   - **Example Input:** `"Contact us at support@example.com"`
   - **Example Output:** `"Contact us at [email]"`

2. **Date Formatter:**
   - **Input:** A string containing dates in various formats (e.g., `DD-MM-YYYY`, `MM/DD/YYYY`, `YYYY.MM.DD`).
   - **Output:** The same string but with all dates converted to `YYYY-MM-DD` format.
   - **Example Input:** `"Event date: 12/05/2023 or 05.12.2023"`
   - **Example Output:** `"Event date: 2023-05-12 or 2023-05-12"`

3. **Phone Number Standardizer:**
   - **Input:** A string containing phone numbers in various formats.
   - **Output:** The string with phone numbers standardized to `(XXX) XXX-XXXX` format.
   - **Example Input:** `"Call +1-123-456-7890 for assistance"`
   - **Example Output:** `"Call (123) 456-7890 for assistance"`

4. **Whitespace Normalizer:**
   - **Input:** A string with irregular spacing (extra spaces, tabs, newlines).
   - **Output:** The same string with all whitespace sequences replaced by a single space.
   - **Example Input:** `"This  text   contains irregular    spacing."`
   - **Example Output:** `"This text contains irregular spacing."`

5. **HTML Tag Remover:**
   - **Input:** A string containing HTML tags.
   - **Output:** The string with all HTML tags removed.
   - **Example Input:** `"<p>This is a <b>bold</b> move!</p>"`
   - **Example Output:** `"This is a bold move!"`

### Testing
Make sure your implementation passes next test cases:

```python
import unittest
import your_module  # Replace with the name of your Python file containing the regex functions

class TestRegexFunctions(unittest.TestCase):

    def test_email_anonymizer(self):
        self.assertEqual(your_module.anonymize_emails("Contact us at support@example.com"), "Contact us at [email]")
        self.assertEqual(your_module.anonymize_emails("Email me at john.doe123@example.org for details."), "Email me at [email] for details.")
        self.assertEqual(your_module.anonymize_emails("No emails in this string."), "No emails in this string.")

    def test_date_formatter(self):
        self.assertEqual(your_module.format_date("Event on 12/05/2023"), "Event on 2023-05-12")
        self.assertEqual(your_module.format_date("Due date is 31-12-2023"), "Due date is 2023-12-31")
        self.assertEqual(your_module.format_date("The date 2023.01.01 marks a new year."), "The date 2023-01-01 marks a new year.")

    def test_phone_number_standardizer(self):
        self.assertEqual(your_module.standardize_phone("Call +1-123-456-7890 for assistance"), "Call (123) 456-7890 for assistance")
        self.assertEqual(your_module.standardize_phone("My number is 123.456.7890"), "My number is (123) 456-7890")
        self.assertEqual(your_module.standardize_phone("Emergency number: 1234567890"), "Emergency number: (123) 456-7890")

    def test_whitespace_normalizer(self):
        self.assertEqual(your_module.normalize_whitespace("This  text   has  extra   spaces"), "This text has extra spaces")
        self.assertEqual(your_module.normalize_whitespace("Line with\nnew line character"), "Line with new line character")
        self.assertEqual(your_module.normalize_whitespace("Tab\tcharacter\ttest"), "Tab character test")

    def test_html_tag_remover(self):
        self.assertEqual(your_module.remove_html_tags("<p>Some <b>bold</b> text</p>"), "Some bold text")
        self.assertEqual(your_module.remove_html_tags("No <a href='link'>HTML</a> tags!"), "No HTML tags!")
        self.assertEqual(your_module.remove_html_tags("<div><span>Nested <i>tags</i></span></div>"), "Nested tags")

if __name__ == '__main__':
    unittest.main()
```