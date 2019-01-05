def header():
    print('CASH RECEIPT')
    print('------------------------------')


def body():
    print('Charged to____________________')
    print('Received by___________________')


def footer():
    print('------------------------------')
    print('\u00A9', 'SoftUni')


def print_receipt():
    header()
    body()
    footer()


print_receipt()
