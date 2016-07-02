---
layout: page
title: Posts
---

{% comment %}
  Displays a list of posts broken down by year.
{% endcomment %}

{% for post in site.posts %}
  {% capture currentyear %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% if currentyear != year %}
    {% unless forloop.first %}
    {% endunless %}
<ul>
    <h1>{{ currentyear }}</h1>
</ul>
    {% capture year %}{{ currentyear }}{% endcapture %}
  {% endif %}
  <li><a href="/python/{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}

