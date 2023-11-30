from django.test import TestCase
from todoapp.models import Tag, TodoList


class TagModelTest(TestCase):

    def test_tag_name_case_insensitive(self):
        Tag.objects.create(name='テストタグ')
        tag = Tag.objects.get(name='テストタグ')
        self.assertEqual(tag.name, 'テストタグ')


class TodoListTest(TestCase):

    def setUp(self):
        self.todo_list = TodoList.objects.create(
            title='Test 1Title',
            description='Desc.',
            due_date='2024-12-31',
            status='Open'
        )
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.tag2 = Tag.objects.create(name='Tag 2')
        self.todo_list.tags.add(self.tag1)
        self.todo_list.tags.add(self.tag2)

    def test_todo_list_created(self):
        self.assertTrue(self.todo_list.pk)

    def test_todo_list_title(self):
        self.assertEqual(self.todo_list.title, 'Test 1Title')

    def test_todo_list_description(self):
        self.assertEqual(self.todo_list.description, 'Desc.') 
 
    def test_todo_list_due_date(self):
        self.assertEqual(self.todo_list.due_date, '2024-12-31')

    def test_todo_list_status(self):
        self.assertEqual(self.todo_list.status, 'Open')

    def test_todo_list_tags(self):
        self.assertEqual(self.todo_list.tags.count(), 2)
        self.assertTrue(self.tag1 in self.todo_list.tags.all())
        self.assertTrue(self.tag2 in self.todo_list.tags.all())
