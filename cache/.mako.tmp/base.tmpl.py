# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1652047798.302618
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'belowtitle', 'sourcelink', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\r\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\r\n</head>\r\n<body>\r\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\r\n\r\n<!-- Menubar -->\r\n\r\n<nav class="navbar navbar-inverse navbar-static-top">\r\n    <div class="container"><!-- This keeps the margins nice -->\r\n        <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-navbar" aria-controls="bs-navbar" aria-expanded="false">\r\n            <span class="sr-only">')
        __M_writer(str(messages("Toggle navigation")))
        __M_writer('</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('">\r\n')
        if logo_url:
            __M_writer('                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo">\r\n')
        __M_writer('\r\n')
        if show_blog_title:
            __M_writer('                <span id="blog-title">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\r\n')
        __M_writer('            </a>\r\n        </div><!-- /.navbar-header -->\r\n        <div class="collapse navbar-collapse" id="bs-navbar" aria-expanded="false">\r\n            <ul class="nav navbar-nav">\r\n                ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\r\n                ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\r\n            </ul>\r\n')
        if search_form:
            __M_writer('                ')
            __M_writer(str(search_form))
            __M_writer('\r\n')
        __M_writer('\r\n            <ul class="nav navbar-nav navbar-right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\r\n')
        if show_sourcelink:
            __M_writer('                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('\r\n')
        __M_writer('                ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\r\n            </ul>\r\n        </div><!-- /.navbar-collapse -->\r\n    </div><!-- /.container -->\r\n</nav>\r\n\r\n<!-- End of Menubar -->\r\n\r\n<div class="container" id="content" role="main">\r\n    <div class="body-content">\r\n        <!--Body content-->\r\n        <div class="row">\r\n            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <!--End of body content-->\r\n\r\n        <footer id="footer">\r\n            ')
        __M_writer(str(content_footer))
        __M_writer('\r\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\r\n        </footer>\r\n    </div>\r\n</div>\r\n\r\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\r\n    <!-- fancy dates -->\r\n    <script>\r\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\r\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\r\n    </script>\r\n    <!-- end fancy dates -->\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer("\r\n    <script>\r\n    baguetteBox.run('div#content', {\r\n        ignoreClass: 'islink',\r\n        captions: function(element) {\r\n            return element.getElementsByTagName('img')[0].alt;\r\n    }});\r\n    </script>\r\n")
        __M_writer(str(body_end))
        __M_writer('\r\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def belowtitle():
            return render_belowtitle(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(translations) > 1:
            __M_writer('                    <li>')
            __M_writer(str(base.html_translations()))
            __M_writer('</li>\r\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "66": 2, "67": 3, "68": 4, "69": 4, "70": 5, "71": 5, "76": 8, "77": 9, "78": 9, "79": 12, "80": 12, "81": 20, "82": 20, "83": 25, "84": 25, "85": 26, "86": 27, "87": 27, "88": 27, "89": 27, "90": 27, "91": 29, "92": 30, "93": 31, "94": 31, "95": 31, "96": 33, "97": 37, "98": 37, "99": 38, "100": 38, "101": 40, "102": 41, "103": 41, "104": 41, "105": 43, "110": 49, "111": 50, "112": 51, "117": 51, "118": 53, "119": 53, "120": 53, "121": 65, "122": 65, "127": 66, "128": 71, "129": 71, "130": 72, "131": 72, "132": 77, "133": 77, "134": 80, "135": 80, "136": 81, "137": 81, "138": 81, "139": 81, "144": 84, "145": 92, "146": 92, "147": 93, "148": 93, "154": 6, "163": 6, "169": 45, "181": 45, "182": 46, "183": 47, "184": 47, "185": 47, "186": 49, "192": 51, "206": 66, "220": 84, "234": 220}}
__M_END_METADATA
"""
