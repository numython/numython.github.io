# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552841674.7248077
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_navigation_links', 'html_feedlinks', 'html_translations']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        meta_generator_tag = _import_ns.get('meta_generator_tag', context.get('meta_generator_tag', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        url_type = _import_ns.get('url_type', context.get('url_type', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        use_base_tag = _import_ns.get('use_base_tag', context.get('use_base_tag', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        theme_color = _import_ns.get('theme_color', context.get('theme_color', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(feeds_translations.head(classification=None, kind='index', other=False)))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n            <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.js" integrity="sha256-SoEATAB7PgNWyyK100I7yQXYm5V08k5SFupDP0h72MY=" crossorigin="anonymous"></script>\n\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n            <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.js" integrity="sha256-SoEATAB7PgNWyyK100I7yQXYm5V08k5SFupDP0h72MY=" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/baguetteBox.min.js"></script>\n')
            __M_writer('        <script src="/assets/js/moment-with-locales.min.js"></script>\n        <script src="/assets/js/fancydates.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.css" integrity="sha256-GrjD69ygFQ+lWqlAOC6LzoNUE4jKrvgkQJrtIukHAi4=" crossorigin="anonymous" />\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer('            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.css" integrity="sha256-GrjD69ygFQ+lWqlAOC6LzoNUE4jKrvgkQJrtIukHAi4=" crossorigin="anonymous" />\n')
            else:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/baguetteBox.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst_base.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(str(text))
                __M_writer(' <b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(classification=None, kind='index', other=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 0, "37": 2, "38": 3, "39": 4, "40": 75, "41": 102, "42": 134, "43": 157, "44": 161, "45": 169, "51": 5, "82": 5, "83": 9, "84": 10, "85": 11, "86": 12, "87": 14, "88": 15, "89": 17, "90": 18, "91": 20, "92": 23, "93": 24, "94": 27, "95": 27, "96": 27, "97": 30, "98": 31, "99": 31, "100": 31, "101": 33, "102": 34, "103": 34, "104": 34, "105": 36, "106": 37, "107": 38, "108": 38, "109": 38, "110": 39, "111": 40, "112": 40, "113": 40, "114": 40, "115": 40, "116": 42, "117": 43, "118": 43, "119": 44, "120": 44, "121": 45, "122": 46, "123": 48, "124": 48, "125": 48, "126": 49, "127": 49, "128": 51, "129": 52, "130": 53, "131": 53, "132": 53, "133": 53, "134": 53, "135": 53, "136": 53, "137": 56, "138": 57, "139": 58, "140": 58, "141": 58, "142": 60, "143": 61, "144": 62, "145": 62, "146": 62, "147": 64, "148": 65, "149": 65, "150": 65, "151": 67, "152": 68, "153": 69, "154": 70, "155": 71, "156": 71, "157": 71, "158": 73, "159": 74, "160": 74, "166": 77, "176": 77, "177": 78, "178": 79, "179": 80, "180": 85, "181": 86, "182": 88, "183": 89, "184": 90, "185": 93, "186": 94, "187": 98, "188": 101, "189": 101, "190": 101, "196": 105, "207": 105, "208": 106, "209": 107, "210": 108, "211": 111, "212": 112, "213": 114, "214": 115, "215": 116, "216": 118, "217": 119, "218": 122, "219": 126, "220": 127, "221": 130, "222": 131, "228": 136, "242": 136, "243": 137, "244": 138, "245": 139, "246": 139, "247": 139, "248": 141, "249": 142, "250": 143, "251": 143, "252": 143, "253": 143, "254": 143, "255": 143, "256": 143, "257": 144, "258": 145, "259": 145, "260": 145, "261": 145, "262": 145, "263": 148, "264": 149, "265": 150, "266": 151, "267": 151, "268": 151, "269": 151, "270": 151, "271": 151, "272": 151, "273": 152, "274": 153, "275": 153, "276": 153, "277": 153, "278": 153, "284": 159, "292": 159, "293": 160, "294": 160, "300": 163, "313": 163, "314": 164, "315": 165, "316": 166, "317": 166, "318": 166, "319": 166, "320": 166, "321": 166, "322": 166, "328": 322}}
__M_END_METADATA
"""
