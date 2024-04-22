SCHEMA = {
    'doc': 'A sales reading.',
    'name': 'Sales',
    'namespace': 'test',
    'type': 'record',
    'fields': [
        {'name': 'client', 'type': 'string'},
        {'name': 'purchase_date', 'type': 'string'},
        {'name': 'product', 'type': 'string'},
        {'name': 'price', 'type': 'long'},
    ],
}