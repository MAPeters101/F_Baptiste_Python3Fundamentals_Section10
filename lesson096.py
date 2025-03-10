widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0},
]

sales_by_widget = {}
for d in widget_sales:
    widget_name = d['name']
    sales = d['sales']
    sales_by_widget[widget_name] = sales
print(sales_by_widget)
