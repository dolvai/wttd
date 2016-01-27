from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name= 'Ivaldo de Paula', cpf='12345678901',
                    email='ivaldosicchieri@yahoo.com.br',phone='16-98153-0680')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ivaldosicchieri@yahoo.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ivaldo de Paula',
            '12345678901',
            'ivaldosicchieri@yahoo.com.br',
            '16-98153-0680',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)