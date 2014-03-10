# -*- coding: utf-8 -*-
from netvisor.responses.sales_payments import SalesPaymentListResponse
from ..utils import get_response_text


def test_sales_payment_list_response():
    xml = get_response_text('SalesPaymentList.xml')
    response = SalesPaymentListResponse(xml)

    assert response.parse() == {
        'objects': [
            {
                'id': u'165',
                'name': u'Matti Mallikas',
                'date': u'7.2.2014',
                'amount': u'250',
                'foreign_currency_amount': None,
                'reference_number': u'1094',
                'invoice_number': u'1',
                'bank_status': {
                    'is_ok': '0',
                    'error_code': u'ERROR_IN_DUE_DATE',
                    'error_description': u'Eräpäivä virheellinen'
                }
            }
        ]
    }