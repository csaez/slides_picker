Especificaciones picker_data 
============================

### Version 0.2

    {
        "filetype": "picker_data",
        "version": 0.2,
        "charname": "",
        "color_table": {key: value, ...},
        "anim_table": {key: value, ...},
        "selectors": (
            {"name": "",
            "targets": (anim_table key, ...),
            "color": color_table key,
            "points": ((x1, y1), (x2, y2), ...)},
            ...),
    }

Donde:

* points: `list` of (x, y) coordinates


### Version 0.1

    {
        "filetype": "picker_data",
        "version": 0.1,
        "charname": "",
        "color_table": {key: value, ...},
        "anim_table": {key: value, ...},
        "selectors": ({"name": "", "targets": (anim_table key, ...), "color": color_table key}, ...),
    }

Donde:

* filetype: `str` que determina el tipo de información
* version: `float` que determina la versión
* charname: `str` que representa el nombre del personaje (namespace)
* color_table: `dict` con tabla de colores
    * key: `str` alias del color
    * value: `tuple` componentes RGB normalizados (de 0.0 a 1.0)
* anim_table: `dict` aliases de control
    * key: `str` alias
    * value: `str` con el nombre del nodo correspondiente
* selectors: `list` / `tuple` de selectores
    * item: `dict` que representa la informacion de un botón selector
        * name: `str` que representa el nombre del botón
        * targets: `list`/`tuple` de aliases a seleccionar (anim_table)
        * color: `str` con el 'alias' correspondiente en color_table
