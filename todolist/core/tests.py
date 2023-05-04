from django.test import TestCase
class FeriadosTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tarefas')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'tarefas')

    def test_template_tarefas(self):
        self.assertTemplateUsed(self.resp, 'index.html')