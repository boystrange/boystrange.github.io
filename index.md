---
layout: page
title: Latest News
---

{% for post in site.posts limit:3 %}
<h4>{{ post.date | date: "%d %B %Y" }}</h4>
<h2>
	{{ post.title }}
	{% if post.link %}
	<small>
		<a href="{{ post.link }}"><i class="fas fa-link"></i></a>
	</small>
	{% endif %}
</h2>
{{ post.content }}
{% endfor %}

<a class="btn" href="{{ "blog/index.html" | relative_url }}">All posts...</a>
