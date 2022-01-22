from django.http import HttpResponse
import html


def render_list(list_of_object, no_data_message="<No Records>"):
    string_rows = []

    for obj in list_of_object:
        string_rows.append(str(obj))

    message = "\n".join(string_rows)
    if not message:
        message = no_data_message
    response = HttpResponse(message)
    response.headers['Content-Type'] = 'text/plain'
    return response


def render_list_html(list_of_object, no_data_message="<No Records>"):
    string_rows = []

    for obj in list_of_object:
        string_rows.append(html.escape(str(obj)))

    message = "<br>".join(string_rows)
    if not message:
        message = no_data_message
    response = HttpResponse(message)
    return response
