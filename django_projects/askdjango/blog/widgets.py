import re
from django import forms
from django.conf import settings
from django.template.loader import render_to_string


class NaverMapPointWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        parent_html = super().render(name, value, attrs)

        width = str(self.attrs.get('width', 800))  # 800, 100%
        height = str(self.attrs.get('height', 600))
        if width.isdigit():
            width += 'px'
        if height.isdigit():
            height += 'px'

        context = dict(attrs, **self.attrs)

        # default point : 강남역
        context['base_lat'] = '37.497921'
        context['base_lng'] = '127.027636'

        context['naver_client_id'] = settings.NAVER_CLIENT_ID
        context['width'] = width
        context['height'] = height

        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context['base_lat'] = lat
                context['base_lng'] = lng
            except (IndexError, ValueError):
                pass

        html = render_to_string('blog/naver_map_point_widget.html', context)

        return parent_html + html

