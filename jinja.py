import jinja2
import webbrowser

dataList = [
    {
        'col1': 'Row 1 Column 1 Data',
        'col2': 'Row 1 Column 2 Data',
        'col3': 'Row 1 Column 3 Data',
    },
    {
        'col1': 'Row 2 Column 1 Data',
        'col2': 'Row 2 Column 2 Data',
        'col3': 'Row 2 Column 3 Data',
    },
    {
        'col1': 'Row 3 Column 1 Data',
        'col2': 'Row 3 Column 2 Data',
        'col3': 'Row 3 Column 3 Data',
    },
]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))

template = environment.get_template('templates/template.html.j2')

renderedPage = template.render(title='Test Page', data=dataList)

outputFileName = 'output/index.html'

with open (outputFileName, 'w') as outputFile:
    outputFile.write(renderedPage)

webbrowser.open(outputFileName)
