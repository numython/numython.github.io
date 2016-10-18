# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476762397.805
_enable_loop = True
_template_filename = u'themes/blogtxt/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        license = _import_ns.get('license', context.get('license', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body>\n<div id="wrapper">\n    <div id="container">\n        <div id="content">\n            <div id="header">\n                <h1 id="blog-title">\n                    <a href="')
        __M_writer(unicode(blog_url))
        __M_writer(u'" title="')
        __M_writer(unicode(blog_title))
        __M_writer(u'">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n                </h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer(u'\n            </div>\n        <div class="hfeed">\n            <!--Body content-->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n            <!--End of body content-->\n        </div><!-- .hfeed -->\n    </div><!-- #content -->\n</div><!-- #container -->\n\n<div id="primary" class="theme_sidebar">\n    <ul>\n')
        for url, text in navigation_links[lang]:
            __M_writer(u'            <li><h3><a href="')
            __M_writer(unicode(rel_link(permalink, url)))
            __M_writer(u'">')
            __M_writer(unicode(text))
            __M_writer(u'</a></h3>\n            ')
            __M_writer(unicode(template_hooks['menu']()))
            __M_writer(u'\n            ')
            __M_writer(unicode(template_hooks['menu_alt']()))
            __M_writer(u'\n')
        __M_writer(u'        <li>')
        __M_writer(unicode(license))
        __M_writer(u'\n        <li>')
        __M_writer(unicode(search_form))
        __M_writer(u'\n    </ul>\n</div><!-- #primary .theme_sidebar -->\n\n<div id="footer">\n    <span id="theme-link"><a href="http://www.plaintxt.org/themes/blogtxt/" title="blog.txt theme for WordPress" rel="follow designer">blog.txt</a> \'theme by <span class="vcard"><a class="url fn n" href="http://scottwallick.com/" title="scottwallick.com" rel="follow designer"><span class="given-name">Scott</span><span class="additional-name"> Allan</span><span class="family-name"> Wallick</span></a></span></span>\n    <small>')
        __M_writer(unicode(content_footer))
        __M_writer(u'\n            ')
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n </small><p>\n</div><!-- #footer -->\n\n</div><!-- #wrapper -->\n    ')
        __M_writer(unicode(body_end))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'                <small>\n                    ')
            __M_writer(unicode(messages("Also available in:")))
            __M_writer(u'&nbsp;\n')
            for langname in translations.keys():
                if langname != lang:
                    __M_writer(u'                            <a href="')
                    __M_writer(unicode(_link("index", None, langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname]["LANGUAGE"]))
                    __M_writer(u'</a>\n')
            __M_writer(u'                </small>\n')
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"135": 5, "141": 18, "23": 2, "26": 0, "155": 19, "156": 20, "154": 18, "158": 21, "159": 22, "160": 23, "161": 24, "162": 24, "163": 24, "164": 24, "165": 24, "166": 27, "167": 29, "173": 167, "157": 21, "56": 2, "57": 3, "58": 3, "59": 4, "60": 4, "65": 7, "66": 8, "67": 8, "68": 16, "69": 16, "70": 16, "71": 16, "72": 16, "73": 16, "78": 29, "83": 33, "84": 41, "85": 42, "86": 42, "87": 42, "88": 42, "89": 42, "90": 43, "91": 43, "92": 44, "93": 44, "94": 46, "95": 46, "96": 46, "97": 47, "98": 47, "99": 53, "100": 53, "101": 54, "102": 54, "103": 59, "104": 59, "105": 60, "106": 60, "107": 61, "108": 61, "114": 33, "127": 5}, "uri": "base.tmpl", "filename": "themes/blogtxt/templates/base.tmpl"}
__M_END_METADATA
"""
