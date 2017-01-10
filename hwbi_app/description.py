from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import links_left
import os
import hwbi_app.views


def description_page(request, model='none', header='none'):
    #viewmodule = importlib.import_module('.views', 'models.' + model)
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(current_dir)
    #viewmodule = importlib.import_module('views')
    #header = viewmodule.header
    header = 'HWBI'    

    #proj_path = os.environ['PROJECT_PATH']
    #template_path = os.environ['TEMPLATE_PATH']
    #text_file2 = open(os.path.join(os.environ['PROJECT_PATH'], 'models/' + model + '/' + model + '_text.txt'), 'r')
    #text_file2 = open(os.path.join(template_path  + "/" + model + '/' + model + '_text.html'), 'r')
    #text_file2 = open(os.path.join(template_path  + "/" + model + '/' + model + '_text.html'), 'r')
    xx = render_to_string(model + '_text.html')
    #xx = text_file2.read()
    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': header + ' Description'})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL'],
        'MODEL': model,
        'PAGE': 'description'})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': header + ' Overview',
        'TEXT_PARAGRAPH': xx})
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list(model)
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)
    return response
