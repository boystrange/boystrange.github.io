---
layout: page
title: Latest News
---

{% for post in site.posts limit:3 %}
<h2>
	{{ post.title }}
	{% if post.link %}
	<small>
		<a href="{{ post.link }}"><i class="fas fa-link"></i></a>
	</small>
	{% endif %}
	{% if post.image %}
	<img src="{{ post.image }}" alt="{{ post.title }}" class="post-image shadow-light"/>
	{% endif %}
</h2>
<h4>{{ post.date | date: "%d %B %Y" }}</h4>
{{ post.content }}
{% endfor %}

<a class="btn" href="{{ "blog/index.html" | relative_url }}">All posts...</a>
