---
layout: post
title:  "Работа над ошибками в JavaScript"
date:   2020-05-13 18:59:00 +0000
categories: JavaScript
---

Есть массив из 1800 объектов. Нужно выбрать все, которые содержат группу `confluence-users`. Сам массив выглядит так:

```javascript
const users = [ {
  "name" : "Mako",
  "email" : "mail1@mail.com",
  "admin" : false,
  "profileUpdatable" : false,
  "internalPasswordDisabled" : true,
  "groups" : [ "readers" ]
}, {
  "name" : "Arasy",
  "email" : "mail2@mail.com",
  "admin" : false,
  "profileUpdatable" : false,
  "internalPasswordDisabled" : true,
  "groups" : [ "confluence-users", "readers", "confluence-developers" ]
}, {
  "name" : "Eliza",
  "email" : "mail3@mail.com",
  "admin" : false,
  "profileUpdatable" : false,
  "internalPasswordDisabled" : true,
  "groups" : [ "readers", "confluence-users" ]
}, {
  "name" : "Fany",
  "email" : "mail4@mail.com",
  "admin" : false,
  "profileUpdatable" : false,
  "internalPasswordDisabled" : true
}]
```

Код на JavaScript, который фильтрует массив по содержимому `groups` и собирает массив логинов (поле `name`). Сам код мне подсказали на StackOverflow:

```javascript
const confluence_user_names = users
  .filter(user => user.groups.includes('confluence-users'))
  .map(user => user.name);
console.log(confluence_user_names);
```

В идеале. Но нет. Получаем ошибку:

```javascript
TypeError: Cannot read property 'includes' of undefined

    at Array.filter
```

И где-то тут у меня пришло понимание самих ошибок. Здесь мы видим ошибку, указывающую на то, что не у всех объектов есть нужное поле `groups`. Да, для этого есть решение, но времени и опыта у меня не было. Просто пробежался по массиву глазами и удалил 5 проблемных объектов.