# -*- coding: utf-8 -*-
from netvisor.responses.companies import (
    CompanyListResponse,
    GetCompanyInformationResponse,
)
from ..utils import get_response_text


def test_company_list_response():
    xml = get_response_text('CompanyList.xml')
    response = CompanyListResponse(xml)

    assert response.parse() == {
        'objects': [
            {
                'is_active': u'1',
                'name': u'ACME',
                'business_code': u'1234567-8'
            }
        ]
    }


def test_get_company_information_response():
    xml = get_response_text('GetCompanyInformation.xml')
    response = GetCompanyInformationResponse(xml)

    assert response.parse() == {
        'name': u'General Motors Finland',
        'business_code': u'1234567-8',
        'type': u'Osakeyhtiö',
        'responsible_person_authorization_rule': (
            u'Yhteisösääntöjen mukaan toiminimen kirjoittavat hallituksen '
            u'puheenjohtaja, toimitusjohtaja ja toimitusjohtajan sijainen '
            u'kukin yksin.'
        ),
        'established_date': u'2009-12-31',
        'terminated_date': u'2009-12-31',
        'most_recent_change_date': u'2009-12-31',
        'is_active': u'1',
        'current_special_status': None,
        'domicile': u'Helsinki',
        'activity_description': u'Kebab',
        'street_address': {
            'street': u'Esimerkkikatu 123',
            'postal_code': u'00100',
            'post_office': u'Helsinki',
        },
        'postal_address': {
            'street': None,
            'postal_code': u'00002',
            'post_office': u'Helsinki',
        },
        'email': u'info@generalmotors.fi',
        'phone': u'020 1234567',
        'fax': u'(09) 5551234',
        'registered_person_roles': [
            {
                'nationality': u'FI',
                'identifier': u'Toimitusjohtaja',
                'type': u'Yhtiön muu johto',
                'established_date': u'2009-12-31',
                'name': u'Gunnar Peterson',
            }
        ],
        'registered_names': [
            {
                'established_date': u'2009-12-31',
                'terminated_date': u'2009-12-31',
                'type': u'Päätoiminimi',
                'name': u'Pekan yritys Oy',
                'is_active': u'1'
            }
        ],
        'stats': {
            'employer_register_status': u'never_registered',
            'revenue_size': u'100-200',
            'staff_size': u'4-9',
            'vat_register_status': u'currently_registered',
            'standard_industrial_classification2008': u'Kaivostoiminta',
            'tax_prepayment_register_status': u'previously_registered',
        }
    }
