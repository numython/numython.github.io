# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476762018.585
_enable_loop = True
_template_filename = u'c:/users/adminis/documents/blog/nikolab/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(abs_link(_link("root", None, langname))))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        title = context.get('title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        description = context.get('description', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html ')
        __M_writer(u"prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer(u'og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer(u'fb: http://ogp.me/ns/fb#\n')
        __M_writer(u"' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer(u'vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer(u'    <base href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(filters.html_escape(unicode(description)))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer(u'        <title>')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</title>\n')
        else:
            __M_writer(u'        <title>')
            __M_writer(filters.html_escape(unicode(title)))
            __M_writer(u' | ')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</title>\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    <meta content="')
        __M_writer(unicode(theme_color))
        __M_writer(u'" name="theme-color">\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n    <link rel="canonical" href="')
        __M_writer(unicode(abs_link(permalink)))
        __M_writer(u'">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if prevlink:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        if nextlink:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer(u'"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer(u'        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('index_atom', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(unicode(_link('index_atom', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 67, "23": 71, "24": 92, "25": 115, "26": 125, "32": 117, "42": 117, "43": 119, "44": 120, "45": 121, "46": 121, "47": 121, "48": 121, "49": 121, "50": 121, "51": 121, "52": 124, "58": 3, "86": 3, "87": 6, "88": 7, "89": 8, "90": 10, "91": 11, "92": 13, "93": 14, "94": 15, "95": 17, "96": 18, "97": 21, "98": 21, "99": 21, "100": 24, "101": 25, "102": 25, "103": 25, "104": 27, "105": 28, "106": 28, "107": 28, "108": 30, "109": 31, "110": 32, "111": 32, "112": 32, "113": 33, "114": 34, "115": 34, "116": 34, "117": 34, "118": 34, "119": 36, "120": 37, "121": 37, "122": 38, "123": 38, "124": 39, "125": 39, "126": 40, "127": 40, "128": 42, "129": 43, "130": 44, "131": 44, "132": 44, "133": 44, "134": 44, "135": 44, "136": 44, "137": 47, "138": 48, "139": 49, "140": 49, "141": 49, "142": 51, "143": 52, "144": 53, "145": 53, "146": 53, "147": 55, "148": 56, "149": 56, "150": 56, "151": 58, "152": 59, "153": 59, "154": 60, "155": 61, "156": 62, "157": 63, "158": 63, "159": 63, "160": 65, "161": 66, "162": 66, "168": 69, "173": 69, "174": 70, "175": 70, "181": 73, "189": 73, "190": 74, "191": 75, "192": 76, "193": 77, "194": 78, "195": 80, "196": 81, "197": 84, "198": 85, "199": 88, "200": 89, "206": 94, "217": 94, "218": 95, "219": 96, "220": 96, "221": 96, "222": 97, "223": 98, "224": 99, "225": 100, "226": 100, "227": 100, "228": 100, "229": 100, "230": 102, "231": 103, "232": 103, "233": 103, "234": 106, "235": 107, "236": 108, "237": 109, "238": 109, "239": 109, "240": 109, "241": 109, "242": 111, "243": 112, "244": 112, "245": 112, "251": 245}, "uri": "base_helper.tmpl", "filename": "c:/users/adminis/documents/blog/nikolab/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl"}
__M_END_METADATA
"""
