---
layout: page
title: Blog
---

<p>
  Please be aware that links from outdated posts may be broken.
</p>

{% for post in site.posts %}
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
<h4 class="date">{{ post.date | date: "%d %B %Y" }}</h4>

{{ post.content }}
{% endfor %}
