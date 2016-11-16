---
layout: post
title: 45 Conversor
date: 2016-11-16 
---

Il·lustrem com utilitzar un codi per tal de convertir **segons** a **hores** i **minuts**.

```python
#!/usr/bin/env python
num=int(input("Introdueix el nombre en segons\n"))
ho=(int(num/3600))
minu=int((num-(ho*3600))/60)
seg=num-((ho*3600)+(minu*60))
print(str(ho)+"h "+str(minu)+"m "+str(seg)+"s")
```

### Entrada

```text
$ Introduexi el nombre en segons
123456
```

### Eixida

```text
34h 17m 36s
```
