from odoo.tests import TransactionCase, tagged

@tagged('test_local')
class TestCourse(TransactionCase):
    def test_some_action(self):

        record = self.env['course.course']
            .create({'nombre': 'value', 
                     'duration': 10, 
                        'min_age': 18,
                            'price': 100, 
                            'amount_discount': 20
                     
                     })
        
        with self.assertQueryCount(11):
            record.calculate_total_price()

        
        self.assertEqual( record.total_price, 80   )


@tagged('test_local')
class TestStudent(TransactionCase):
    def test_some_action(self):

        record = self.env['course.student']
            .create({'name': 'value', 
                     'dni': '12345678A',
                        'age': 14

                     })
        
        with self.assertRaises(ValidationError):
            record._check_minimum_age()
       

