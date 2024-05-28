# lib/testing/person_test.py

import io
import sys
from person import Person

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name='Guido', job='Engineer')
        assert(type(guido) == Person)

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="", job="Engineer")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name=123, job='Engineer')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="A" * 26, job='Engineer')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n"

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person(name="Guido", job='Engineer')
        assert guido.name == "Guido"

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters.'''
        guido = Person(name="guido van rossum", job='Engineer')
        assert guido.name == "Guido Van Rossum"

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="Guido", job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Job must be in list of approved jobs.\n"

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(name="Guido", job="Engineer")
        assert guido.job == "Engineer"
