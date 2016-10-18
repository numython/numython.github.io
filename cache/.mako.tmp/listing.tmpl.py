# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476762398.725
_enable_loop = True
_template_filename = u'c:/users/adminis/documents/blog/nikolab/lib/site-packages/nikola/data/themes/base/templates/listing.tmpl'
_template_uri = u'listing.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'ui', context._clean_inheritance_tokens(), templateuri=u'crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(ui.bar(crumbs)))
        __M_writer(u'\n')
        if folders or files:
            __M_writer(u'<ul>\n')
            for name in folders:
                __M_writer(u'    <li><a href="')
                __M_writer(filters.url_escape(unicode(name)))
                __M_writer(u'"><i class="icon-folder-open"></i> ')
                __M_writer(filters.html_escape(unicode(name)))
                __M_writer(u'</a>\n')
            for name in files:
                __M_writer(u'    <li><a href="')
                __M_writer(filters.url_escape(unicode(name)))
                __M_writer(u'.html"><i class="icon-file"></i> ')
                __M_writer(filters.html_escape(unicode(name)))
                __M_writer(u'</a>\n')
            __M_writer(u'</ul>\n')
        if code:
            __M_writer(u'    <h1>')
            __M_writer(unicode(title))
            __M_writer(u'\n')
            if source_link:
                __M_writer(u'            <small><a href="')
                __M_writer(unicode(source_link))
                __M_writer(u'">(')
                __M_writer(unicode(messages("Source")))
                __M_writer(u')</a></small>\n')
            __M_writer(u'        </h1>\n    ')
            __M_writer(unicode(code))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "46": 2, "47": 3, "52": 24, "58": 4, "74": 4, "75": 5, "76": 5, "77": 6, "78": 7, "79": 8, "80": 9, "81": 9, "82": 9, "83": 9, "84": 9, "85": 11, "86": 12, "87": 12, "88": 12, "89": 12, "90": 12, "91": 14, "92": 16, "93": 17, "94": 17, "95": 17, "96": 18, "97": 19, "98": 19, "99": 19, "100": 19, "101": 19, "102": 21, "103": 22, "104": 22, "110": 104}, "uri": "listing.tmpl", "filename": "c:/users/adminis/documents/blog/nikolab/lib/site-packages/nikola/data/themes/base/templates/listing.tmpl"}
__M_END_METADATA
"""
